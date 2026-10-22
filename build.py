import json
d=json.load(open('data.json'))
html=r'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>洛雪音乐 · 客户端与音源一键复制</title>
<style>
:root{--bg:#0f1115;--card:#181b22;--line:#2a2f3a;--txt:#e8eaef;--sub:#9aa3b2;--acc:#4ade80;--acc2:#60a5fa}
*{box-sizing:border-box}body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--txt)}
.wrap{max-width:1080px;margin:0 auto;padding:28px 16px 60px}
h1{font-size:26px;margin:0 0 6px}.lead{color:var(--sub);margin:0 0 22px;font-size:14px}
.tabs{display:flex;gap:8px;margin-bottom:16px;flex-wrap:wrap}
.tab{padding:8px 16px;border-radius:999px;border:1px solid var(--line);background:var(--card);color:var(--txt);cursor:pointer;font-size:14px}
.tab.on{background:var(--acc);color:#05230f;border-color:var(--acc);font-weight:600}
.bar{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-bottom:14px}
.bar label{color:var(--sub);font-size:13px;display:flex;gap:6px;align-items:center;cursor:pointer}
input[type=search]{flex:1;min-width:180px;padding:9px 12px;border-radius:10px;border:1px solid var(--line);background:var(--card);color:var(--txt)}
.btn{padding:8px 14px;border:0;border-radius:9px;background:var(--acc2);color:#04162e;font-weight:600;cursor:pointer;font-size:13px;white-space:nowrap}
.btn.g{background:var(--acc);color:#05230f}.btn.ghost{background:transparent;border:1px solid var(--line);color:var(--txt)}
.grid{display:grid;gap:12px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px 16px}
.row{display:flex;justify-content:space-between;gap:10px;align-items:center;flex-wrap:wrap}
.name{font-weight:600;font-size:15px}.meta{color:var(--sub);font-size:12px;margin-top:3px}
.url{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:12px;color:#b8c2d6;word-break:break-all;margin-top:8px;background:#11141a;padding:8px 10px;border-radius:8px}
.tag{display:inline-block;font-size:11px;padding:2px 8px;border-radius:999px;margin-left:6px;vertical-align:middle}
.t1{background:#14532d;color:#86efac}.t2{background:#3b2a0b;color:#fbbf24}
.files{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}
.files a{font-size:12px;padding:5px 10px;border-radius:8px;background:#11141a;border:1px solid var(--line);color:var(--txt);text-decoration:none}
.files a:hover{border-color:var(--acc2)}
.toast{position:fixed;left:50%;bottom:28px;transform:translateX(-50%) translateY(20px);background:var(--acc);color:#05230f;padding:10px 18px;border-radius:999px;font-weight:600;opacity:0;transition:.25s;pointer-events:none}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.hint{color:var(--sub);font-size:12px;margin-top:20px;line-height:1.7}
a{color:var(--acc2)}
</style></head><body><div class="wrap">
<h1>🎵 洛雪音乐 · 客户端 & 音源</h1>
<p class="lead">点按钮即可复制音源链接，粘贴到「设置 → 自定义源 → 在线导入」。音源每周自动检测，最近检测 __UPDATED__ · <a href="https://github.com/passionsu-su/lx-music">GitHub 仓库</a></p>
<div class="tabs"><button class="tab on" data-v="src">音源接口</button><button class="tab" data-v="cli">客户端下载</button></div>
<div id="src">
 <div class="bar"><input type="search" id="q" placeholder="搜索音源…">
 <label><input type="checkbox" id="px"> 使用国内加速链接 (ghproxy)</label>
 <button class="btn g" id="all">复制全部可用</button></div>
 <div class="grid" id="slist"></div>
</div>
<div id="cli" style="display:none">
 <div class="bar"><input type="search" id="q2" placeholder="搜索客户端 / 平台（如 iOS、mac）…">
 <label><input type="checkbox" id="px2"> 下载走 ghproxy 加速</label></div>
 <div class="grid" id="clist"></div>
 <p class="hint">iOS 版均为未签名 IPA，需用 AltStore / SideStore / TrollStore 等自签安装；官方暂无 iOS 版。魔改版为第三方作品，请自行甄别。</p>
</div>
<p class="hint">本页仅整理链接，不存储任何文件。音源来自网络，可用性随时变化，请支持正版音乐。</p>
</div><div class="toast" id="t">已复制</div>
<script>
const D=__DATA__;const P="https://ghproxy.net/";
const $=s=>document.querySelector(s);
function toast(m){const t=$('#t');t.textContent=m;t.classList.add('show');clearTimeout(t._h);t._h=setTimeout(()=>t.classList.remove('show'),1400)}
async function copy(txt,msg){try{await navigator.clipboard.writeText(txt)}catch(e){const a=document.createElement('textarea');a.value=txt;document.body.appendChild(a);a.select();document.execCommand('copy');a.remove()}toast(msg||'已复制')}
const su=u=>($('#px').checked&&u.includes('raw.githubusercontent'))?P+u:u;
const esc=s=>s.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function rs(){const q=$('#q').value.trim().toLowerCase();
 $('#slist').innerHTML=D.sources.filter(s=>!q||(s.name+s.key).toLowerCase().includes(q)).map(s=>`<div class="card"><div class="row"><div><div class="name">${esc(s.name)}<span class="tag ${s.ok?'t1':'t2'}">${s.ok?'可用':'失效'}</span></div><div class="meta">${s.key} · 版本 ${esc(s.version||'-')} · 检测于 ${s.checked}</div></div><button class="btn" data-u="${esc(s.url)}">复制链接</button></div><div class="url">${esc(su(s.url))}</div></div>`).join('')}
function rc(){const q=$('#q2').value.trim().toLowerCase();const px=$('#px2').checked;
 $('#clist').innerHTML=D.clients.filter(c=>!q||(c.name+c.platform+c.type).toLowerCase().includes(q)).map(c=>`<div class="card"><div class="row"><div><div class="name">${esc(c.name)}<span class="tag ${c.type=='官方'?'t1':'t2'}">${c.type}</span></div><div class="meta">${esc(c.platform)} · ${esc(c.version)}${c.date?' · '+c.date:''}</div></div><a class="btn ghost" href="${c.repo}" target="_blank" rel="noopener">项目主页</a></div><div class="files">${c.files.map(f=>`<a href="${px&&f[1].includes('/releases/download/')?P+f[1]:f[1]}" target="_blank" rel="noopener">⬇ ${esc(f[0])}</a>`).join('')}</div></div>`).join('')}
document.addEventListener('click',e=>{const b=e.target.closest('[data-u]');if(b)copy(su(b.dataset.u))});
$('#all').onclick=()=>copy(D.sources.filter(s=>s.ok).map(s=>su(s.url)).join('\n'),'已复制全部可用音源 '+D.sources.filter(s=>s.ok).length+' 条');
['#q','#px'].forEach(s=>$(s).addEventListener('input',rs));['#q2','#px2'].forEach(s=>$(s).addEventListener('input',rc));
document.querySelectorAll('.tab').forEach(t=>t.onclick=()=>{document.querySelectorAll('.tab').forEach(x=>x.classList.toggle('on',x==t));$('#src').style.display=t.dataset.v=='src'?'':'none';$('#cli').style.display=t.dataset.v=='cli'?'':'none'});
rs();rc();
</script></body></html>'''
open('index.html','w').write(html.replace('__DATA__',json.dumps(d,ensure_ascii=False)).replace('__UPDATED__',d['updated']))

P="https://ghproxy.net/"
L=["# 🎵 洛雪音乐（LX Music）客户端 & 音源合集\n",
f"> 客户端链接来自各项目 GitHub Releases；音源每周一由 GitHub Actions 自动检测并更新（最近检测：{d['updated']}）。\n>\n> 🌐 **一键复制网页**：https://passionsu-su.github.io/lx-music/\n>\n> 📺 **Passion Music TV**：内置音源、手机扫码一键导入，见下表「自建」行。\n",
"## 一、客户端下载\n","| 名称 | 类型 | 平台 | 最新版本 | 发布日期 | 下载 | 项目主页 |","|---|---|---|---|---|---|---|"]
for c in d['clients']:
    dl="<br>".join(f"[{n}]({u})" for n,u in c['files'])
    L.append(f"| {c['name']} | {c['type']} | {c['platform']} | [{c['version']}]({c['release']}) | {c['date'] or '-'} | {dl} | [GitHub]({c['repo']}) |")
L+=["\n> 🇨🇳 国内下载慢：在任意下载链接前加 `https://ghproxy.net/` 加速。\n>\n> 🍎 iOS 版均为**未签名 IPA**，需用 AltStore / SideStore / 巨魔(TrollStore) / 爱思助手等自签安装。官方暂无 iOS 版。\n",
"## 二、音源接口\n","使用方法：洛雪音乐 → 设置 → 自定义源 → 在线导入 → 粘贴下方链接。\n",
"| 音源名称 | 标识 | 版本 | 状态 | 原始链接 | 加速链接（国内） |","|---|---|---|---|---|---|"]
for s_ in d['sources']:
    u=s_['url']; px=f"`{P+u}`" if 'raw.githubusercontent' in u else '-'
    L.append(f"| {s_['name']} | `{s_['key']}` | {s_['version'] or '-'} | {'✅ 可用' if s_['ok'] else '❌ 失效'} | `{u}` | {px} |")
L+=["\n## 三、相关资源\n",
"- [洛雪音乐官方文档](https://lxmusic.toside.cn/)",
"- [pdone/lx-music-source（音源合集，每日健康检测）](https://github.com/pdone/lx-music-source)",
"- [Macrohard0001/lx-ikun-music-sources（音源与安装包收集）](https://github.com/Macrohard0001/lx-ikun-music-sources)",
"- [lx-music-sync-server（数据同步服务）](https://github.com/lyswhut/lx-music-sync-server)",
"- [lx-music-api-server（Python 解析接口服务器）](https://github.com/MeoProject/lx-music-api-server)",
"\n## 免责声明\n","本仓库仅做链接整理，不存储任何音频或程序文件。音源来自网络，可用性随时变化，请支持正版音乐。魔改版为第三方作品，请自行甄别安全性。\n"]
open('README.md','w').write("\n".join(L))
json.dump({"updated":d['updated'],"sources":d['sources']},open('sources.json','w'),ensure_ascii=False,indent=1)
