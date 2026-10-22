"""构建前拉取最新内置音源：读取 lx-music 仓库 main 分支 sources.json，下载可用音源到 assets/builtin_sources。"""
import json, os, re, hashlib, urllib.request
OUT = os.path.join(os.path.dirname(__file__), '..', 'app', 'src', 'main', 'assets', 'builtin_sources')
LIST = ["https://raw.githubusercontent.com/passionsu-su/lx-music/main/sources.json",
        "https://passionsu-su.github.io/lx-music/sources.json"]
def get(u):
    with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=30) as r:
        return r.read().decode('utf-8', 'replace')
data = None
for u in LIST:
    try: data = json.loads(get(u)); break
    except Exception as e: print("list failed", u, e)
if not data:
    print("keep existing snapshot"); raise SystemExit(0)
os.makedirs(OUT, exist_ok=True)
for f in os.listdir(OUT): os.remove(os.path.join(OUT, f))
items, seen, h = [], set(), hashlib.sha1()
for s in data['sources']:
    if not s.get('ok'): continue
    try: txt = get(s['url'])
    except Exception as e: print("skip", s['url'], e); continue
    m = re.search(r'@name\s+(.+)', txt[:3000]); name = m.group(1).strip() if m else s['name']
    if name in seen: continue
    seen.add(name)
    fn = re.sub(r'[^a-zA-Z0-9_-]', '_', s['key']) + '.js'
    open(os.path.join(OUT, fn), 'w', encoding='utf-8').write(txt)
    h.update(txt.encode())
    items.append({"file": fn, "name": name, "version": s.get('version'), "url": s['url'], "ok": True, "enable": bool(s.get('tv_enable'))})
    print("bundled", name)
json.dump({"version": h.hexdigest()[:12], "sources": items}, open(os.path.join(OUT, 'index.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
