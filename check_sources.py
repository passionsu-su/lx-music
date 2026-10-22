"""每周检测音源：可用性、@name/@version，并自动发现 pdone/lx-music-source 新增音源。"""
import json, re, datetime, urllib.request
UA={"User-Agent":"Mozilla/5.0 lx-music-checker"}
def get(url, timeout=25):
    req=urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read().decode('utf-8','replace')
def meta(txt, key):
    m=re.search(r'@'+key+r'\s+(.+)', txt[:3000]); return m.group(1).strip() if m else None
d=json.load(open('data.json', encoding='utf-8'))
today=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
# 自动发现 pdone 新音源目录
try:
    _, txt = get("https://api.github.com/repos/pdone/lx-music-source/contents/")
    known={s['url'] for s in d['sources']}
    for it in json.loads(txt):
        if it['type']!='dir' or it['name'].startswith('.'): continue
        u=f"https://raw.githubusercontent.com/pdone/lx-music-source/main/{it['name']}/latest.js"
        if u not in known:
            d['sources'].append({"name":it['name'],"key":it['name'],"version":None,"url":u,"ok":False,"checked":today,"tv_enable":False})
            print("发现新音源", u)
except Exception as e:
    print("发现新音源失败", e)
changed=False
for s in d['sources']:
    try:
        code, txt = get(s['url'])
        ok = code==200 and len(txt)>200 and ('@name' in txt[:3000] or 'lx' in txt) and not txt.lstrip().startswith('<')
        name, ver = meta(txt,'name'), meta(txt,'version')
    except Exception as e:
        ok, name, ver = False, None, None
        print("失败", s['url'], e)
    if ok:
        if ver and ver!=s.get('version'): print("版本更新", s['name'], s.get('version'), '->', ver); s['version']=ver; changed=True
        if s['name']==s['key'] and name: s['name']=name; changed=True
    if ok!=s.get('ok'): changed=True
    s['ok']=ok; s['checked']=today
d['updated']=today
json.dump(d, open('data.json','w', encoding='utf-8'), ensure_ascii=False, indent=1)
open('.sources_changed','w').write('1' if changed else '0')
print("changed" if changed else "no change")
