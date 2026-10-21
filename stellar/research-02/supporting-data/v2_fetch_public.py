import concurrent.futures, datetime, json, pathlib, subprocess

root=pathlib.Path(__file__).parent
base='https://amm-api.aqua.network/api/external/v1/pools/'
def get(page):
    url=base+'?page='+str(page)
    data=json.loads(subprocess.check_output(['curl','-L','--max-time','20','-s',url]))
    return page,data
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
    results=list(ex.map(get,range(1,38)))
data={'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'base_url':base,'pages':[{'page':p,'data':d} for p,d in results]}
(root/'v2-aqua-all.json').write_text(json.dumps(data,indent=2))
rows=[x for _,d in results for x in d.get('results',[])]
print('total',len(rows),'count',results[0][1].get('count'),'at',data['retrieved_utc'])
for p in rows:
 if any(t.split(':')[0] in ['USDY','CETES','USTRY','TESOURO','BENJI','USTBL','EUTBL'] for t in p.get('tokens_str',[])): print(json.dumps(p))
