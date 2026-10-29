#!/usr/bin/env python3
"""Offline, project-scoped installer and capability inventory. No network or shell execution."""
import argparse
import json
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- base-builder:start -->'
END = '<!-- base-builder:end -->'

def safe_path(root, path):
    path.relative_to(root)
    for item in (path, *path.parents):
        if item == root:
            break
        if item.is_symlink():
            raise ValueError(f'Refusing symlink destination: {item}')
    if not path.resolve().is_relative_to(root):
        raise ValueError(f'Destination escapes target: {path}')
    return path

def instruction_text(path, relative_skill):
    current = path.read_text() if path.exists() else ''
    block = f'{START}\nFor Base development tasks, read `{relative_skill}/SKILL.md` and only the relevant references. Preserve the user’s task and existing repository instructions. This installs guidance, not tools or deployment permission.\n{END}'
    if START in current or END in current:
        if current.count(START) != 1 or current.count(END) != 1:
            raise ValueError(f'Malformed managed block: {path}')
        a,b=current.index(START),current.index(END)
        if a>b:
            raise ValueError(f'Reversed managed block: {path}')
        # Preserve edits instead of silently replacing a user's modified instructions.
        if current[a:b+len(END)] != block:
            raise ValueError(f'Changed managed block: {path}; merge manually')
        return current.encode()
    return (current + ('\n' if current else '') + block + '\n').encode()

def install(target, client, apply=False):
    if client not in ('codex','claude','both'):
        raise ValueError('Client must be codex, claude, or both')
    target = Path(target).expanduser().resolve()
    if target.exists() and not target.is_dir():
        raise ValueError('Target must be a directory')
    source = ROOT/'skills/base-builder'
    if not (source/'SKILL.md').is_file():
        raise ValueError('Package skill is missing')
    changes = {}
    clients = [('codex','.agents','AGENTS.md'),('claude','.claude','CLAUDE.md')]
    for name,folder,instructions in clients:
        if client not in (name,'both'):
            continue
        relative=f'{folder}/skills/base-builder'
        for src in sorted(source.rglob('*')):
            if src.is_symlink():
                raise ValueError(f'Refusing source symlink: {src}')
            if not src.is_file():
                continue
            dest=safe_path(target,target/relative/src.relative_to(source))
            data=src.read_bytes()
            if dest.exists() and (not dest.is_file() or dest.read_bytes()!=data):
                raise ValueError(f'Existing different file: {dest}; merge manually')
            changes[dest]=data
        dest=safe_path(target,target/instructions)
        changes[dest]=instruction_text(dest,relative)
    # Complete preflight before any writes. No force-overwrite option.
    planned=[str(p.relative_to(target)) for p,d in changes.items() if not p.exists() or p.read_bytes()!=d]
    if apply:
        for dest,data in changes.items():
            if dest.exists() and dest.read_bytes()==data:
                continue
            dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_bytes(data)
    return planned

def doctor(target):
    target=Path(target).expanduser().resolve()
    return {
        'target':str(target),
        'executables_on_PATH':{name:bool(shutil.which(name)) for name in ('git','gh','node','pnpm','forge','cast','anvil','python3','codex','claude')},
        'skill_files_present':{client:(target/folder/'skills/base-builder/SKILL.md').is_file() for client,folder in [('codex','.agents'),('claude','.claude')]},
        'mcp_connection':'NOT_TESTED: run client MCP inventory then a real docs read',
        'rpc_chain_and_capabilities':'NOT_TESTED',
        'versions_dependencies_credentials':'NOT_TESTED',
        'deployment_authorization':'NOT_INFERRED',
        'note':'Presence is not compatibility or readiness. This command does not execute discovered binaries.'
    }

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    commands=parser.add_subparsers(dest='command',required=True)
    p=commands.add_parser('install');p.add_argument('--target',required=True);p.add_argument('--client',choices=['codex','claude','both'],default='both');p.add_argument('--apply',action='store_true')
    p=commands.add_parser('doctor');p.add_argument('--target',default='.')
    args=parser.parse_args()
    try:
        if args.command=='install':
            result={'mode':'APPLY' if args.apply else 'DRY_RUN','files':install(args.target,args.client,args.apply),'mcp':'not configured; follow README'}
        else:
            result=doctor(args.target)
        print(json.dumps(result,indent=2,ensure_ascii=False))
    except (ValueError,OSError) as exc:
        print(f'ERROR: {exc}',file=sys.stderr);return 1
    return 0
if __name__=='__main__':sys.exit(main())
