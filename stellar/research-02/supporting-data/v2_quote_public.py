import concurrent.futures, datetime, json, pathlib, subprocess
root=pathlib.Path(__file__).parent
tokens={'USDY':'CB3YA656OYIHU57657I5KGSBRHE5I3OZU4VFC22PYAOANFZHEWNYGAGP','USDC':'CCW67TSZV3SSS2HXMBQ5JFGCKJNXKZM7UQUWUZPUTHXSTZLEO7SJMI75'}
def get(q):
    a,b,size=q
    data={'token_in_address':tokens[a],'token_out_address':tokens[b],'amount':str(size*10**7),'slippage':'0','provider_fee':'0','max_depth':4}
    p=root/f'v2-quote-input-{a}-{size}.json';p.write_text(json.dumps(data))
    out=subprocess.check_output(['curl','-L','--max-time','25','-s','-H','Content-Type: application/json','--data-binary','@'+str(p),'https://amm-api.aqua.network/api/external/v1/find-path/'])
    try:r=json.loads(out)
    except:r={'error':out.decode()[:200]}
    return {'input':data,'input_token':a,'output_token':b,'amount_human':size,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'result':r}
qs=[(a,b,n) for a,b in [('USDY','USDC'),('USDC','USDY')] for n in [1000,10000,100000]]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:r=list(ex.map(get,qs))
(root/'v2-aqua-quotes.json').write_text(json.dumps(r,indent=2))
for q in r:
 x=q['result'];print(q['input_token'],q['amount_human'],'->',q['output_token'],'out',int(x.get('amount',0))/10**7,'success',x.get('success'),'pools',x.get('pools'),'time',q['retrieved_utc'],'error',x.get('error'))
