"""生成 appletv/README.md（Apple TV 专区）。由 build.py 调用。"""
import json
A = json.load(open('appletv/apps.json', encoding='utf-8'))
P = json.load(open('appletv/playlists.json', encoding='utf-8'))
GH = 'https://ghproxy.net/'
REPO_M3U = 'https://raw.githubusercontent.com/passionsu-su/lx-music/main/appletv/iptv-tested.m3u'
PAGES_M3U = 'https://passionsu-su.github.io/lx-music/appletv/iptv-tested.m3u'
def lk(a): return f"[打开]({a['url']})" + (f" · [源码]({a['src']})" if a.get('src') and a['src'] != a['url'] else '')
L = ['# 📺 Apple TV 专区：IPTV 直播 · 浏览器 · B 站 · 音乐\n',
f"> 直播源每周一由 GitHub Actions 自动检测（最近检测：{P['updated']}）。免费的排在前面。\n>\n> ⚠️ 检测机器在海外、没有 IPv6，「仅国内可播」和 IPv6 频道会被误判失效，所以下面的可用数**只少不多**，国内实际能播的更多。\n",
'## 一、直播源（直接填进播放器）\n',
'### ⭐ 本仓库合并好的「已测可用」列表\n',
f"已逐个频道探测、去重并按 央视 / 卫视 / 港澳台 / 影视 / 体育 / 春晚 / 地方 分组，共 **{P['merged_count']}** 个频道（" + '、'.join(f'{k} {v}' for k, v in P['merged_by_cat'].items()) + '）。已内置 EPG 节目单地址。\n',
'| 用途 | 地址 |', '|---|---|',
f'| 首选（GitHub Pages，国内一般可直连） | `{PAGES_M3U}` |',
f'| 备用（raw） | `{REPO_M3U}` |',
f'| 备用（国内加速） | `{GH + REPO_M3U}` |',
'\n### 上游订阅源（自动更新，频道更多）\n',
'| 名称 | 订阅地址 | 频道数 | 本周探测可播 | 类型 |', '|---|---|---|---|---|']
for p in P['playlists']:
    typ = 'IPv6（需家宽 IPv6）' if p['ipv6'] else 'IPv4'
    alt = f"<br>备用 `{p['alt']}`" if p.get('alt') else ''
    L.append(f"| {p['name']} | `{p['url']}`{alt} | {p.get('channels', 0)} | {p.get('alive', 0)} | {typ} |")
L += ['\n### EPG 节目单\n', '| 名称 | 地址 |', '|---|---|'] + [f"| {e['name']} | `{e['url']}` |" for e in P['epg']]
L += ['\n> 用法：播放器里「添加播放列表 / 订阅」→ 粘贴 m3u 地址；EPG 填到「节目单 / XMLTV」。家里宽带有 IPv6 的，优先用范明明 IPv6 源，画质最好。\n',
'## 二、IPTV 播放器（tvOS）\n', '| App | 价格 | 支持格式 | 国区 | 说明 | 链接 |', '|---|---|---|---|---|---|']
L += [f"| {a['name']} | {a['price']} | {a['fmt']} | {a['cn']} | {a['note']} | {lk(a)} |" for a in A['iptv']]
L += ['\n> 推荐组合：**Fjord**（全免费）或 **APTV**（中文、国区）+ 上面的「已测可用」列表 + 范明明 EPG。\n',
'## 三、浏览器（TestFlight / 开源）\n', '| App | 价格 | 说明 | 链接 |', '|---|---|---|---|']
L += [f"| {a['name']} | {a['price']} | {a['note']} | {lk(a)} |" for a in A['browser']]
L += ['\n## 四、第三方 B 站客户端\n', '| App | 价格 | 说明 | 链接 |', '|---|---|---|---|']
L += [f"| {a['name']} | {a['price']} | {a['note']} | {lk(a)} |" for a in A['bilibili']]
L += ['\n## 五、免费音乐 App\n', '| App | 价格 | 说明 | 链接 |', '|---|---|---|---|']
L += [f"| {a['name']} | {a['price']} | {a['note']} | {lk(a)} |" for a in A['music']]
L += ['\n> 洛雪音乐目前没有 tvOS 版。想在 Apple TV 上听：用 **Vibefy**，或在 iPhone 上用 LX 的 iOS 构建（见主页客户端表）再 AirPlay 到 Apple TV。\n',
'## 六、TestFlight 安装方法\n',
'1. iPhone 和 Apple TV 都从 App Store 安装 **TestFlight**，并登录**同一个** Apple ID。',
'2. 在 iPhone 上用 Safari 打开 TF 链接，点「接受」。',
'3. 打开 Apple TV 上的 TestFlight，找到该 App 点「安装」。',
'4. TF 版 90 天过期，到期在 TestFlight 里更新即可；显示「名额已满」就过几天再试。',
'\n**自签 IPA（ATV-Bilibili 等）**：Mac 装 Sideloadly 或 atvloadly，用自己的 Apple ID 签名装到 Apple TV；免费 ID 7 天需重签。\n',
'## 免责声明\n', '本页只整理公开链接，不存储任何音视频。直播源来自网络公开仓库，可用性随时变化，请只观看你有权收看的内容。TestFlight / 自签应用为第三方作品，请自行甄别。\n']
open('appletv/README.md', 'w', encoding='utf-8').write('\n'.join(L))
