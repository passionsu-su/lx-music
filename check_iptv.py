"""每周检测 Apple TV 直播源：订阅链接可用性 + 逐个频道探测，合并可用频道生成 appletv/iptv-tested.m3u。
注：GitHub Actions 机房在海外且无 IPv6，「仅国内可播」和 IPv6 频道会被判为不可用，所以合并列表偏保守。"""
import json, re, ssl, datetime, urllib.request, concurrent.futures as cf
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
UA = {"User-Agent": "AppleCoreMedia/1.0.0 (Apple TV; tvOS 18)"}
P = 'appletv/playlists.json'
cfg = json.load(open(P, encoding='utf-8'))
today = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')

def get(u, n=None, t=20):
    r = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=t, context=ctx)
    return r.status, (r.read(n) if n else r.read())

def parse(t):
    out, name, grp, logo, tid = [], None, '', '', ''
    for l in t.splitlines():
        l = l.strip()
        if l.startswith('#EXTINF'):
            name = l.rsplit(',', 1)[-1].strip()
            g = lambda k: (re.search(k + r'="([^"]*)"', l) or [None, ''])[1]
            grp, logo, tid = g('group-title'), g('tvg-logo'), g('tvg-id') or g('tvg-name')
        elif l and not l.startswith('#') and re.match(r'^(https?|rtmp|rtsp|rtp|udp)://', l):
            out.append(dict(name=name or '', group=grp, logo=logo, tid=tid, url=l.split('$')[0])); name = None
        elif not l.startswith('#') and re.search(r',https?://', l):
            n, u = l.split(',', 1)
            out.append(dict(name=n.strip(), group='', logo='', tid='', url=u.split('$')[0].split('#')[0].strip()))
    return out

def probe(u):
    if not u.startswith('http') or re.match(r'^https?://\[', u):
        return u, False
    try:
        s, b = get(u, 4096, 8)
        ok = s == 200 and (b.lstrip().startswith(b'#EXTM3U') or b[:1] == b'G' or b[:3] == b'FLV' or b[4:8] == b'ftyp' or len(b) > 1000)
        return u, ok
    except Exception:
        return u, False

chs = {}
for p in cfg['playlists']:
    try:
        s, b = get(p['url'], t=30)
        lst = parse(b.decode('utf-8', 'replace'))
        p.update(reachable=s == 200, channels=len(lst))
        chs[p['key']] = lst
    except Exception as e:
        print('订阅失败', p['url'], e); p.update(reachable=False, channels=0, alive=0); chs[p['key']] = []
urls = sorted({c['url'] for l in chs.values() for c in l})
print(len(urls), 'urls')
with cf.ThreadPoolExecutor(128) as ex:
    res = dict(ex.map(probe, urls))
for p in cfg['playlists']:
    p['alive'] = sum(res.get(c['url'], False) for c in chs[p['key']])
    p['checked'] = today

def cat(c):
    n, g = c['name'], c['group']
    if re.search(r'CCTV|CGTN|央视|中央', n, re.I): return '央视'
    if '卫视' in n: return '卫视'
    if re.search(r'港|澳|台|TVB|翡翠|凤凰|明珠|Taiwan|Hong ?Kong', n + g, re.I): return '港澳台'
    if re.search(r'春晚', g + n): return '春晚'
    if re.search(r'剧|影|电影|movie', g + n, re.I): return '影视'
    if re.search(r'体育|sport', g + n, re.I): return '体育'
    return '地方/其他'
order = ['央视', '卫视', '港澳台', '影视', '体育', '春晚', '地方/其他']
seen, merged = set(), []
for p in cfg['playlists']:
    if not p.get('merge'): continue
    for c in chs[p['key']]:
        if res.get(c['url']) and c['url'] not in seen and '更新' not in c['group']:
            seen.add(c['url']); c['cat'] = cat(c); merged.append(c)
merged.sort(key=lambda c: (order.index(c['cat']), c['name']))
L = ['#EXTM3U x-tvg-url="https://live.fanmingming.cn/e.xml"', f'# Apple TV 可用直播源合集 · 检测于 {today} · {len(merged)} 个频道 · https://github.com/passionsu-su/lx-music']
for c in merged:
    L.append(f'#EXTINF:-1 tvg-id="{c["tid"]}" tvg-name="{c["name"]}" tvg-logo="{c["logo"]}" group-title="{c["cat"]}",{c["name"]}')
    L.append(c['url'])
open('appletv/iptv-tested.m3u', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
cfg['updated'] = today; cfg['merged_count'] = len(merged)
cfg['merged_by_cat'] = {k: sum(c['cat'] == k for c in merged) for k in order}
json.dump(cfg, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('merged', len(merged), cfg['merged_by_cat'])
