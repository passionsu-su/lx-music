# 📺 Apple TV 专区：IPTV 直播 · 浏览器 · B 站 · 音乐

> 直播源每周一由 GitHub Actions 自动检测（最近检测：2026-11-12）。免费的排在前面。
>
> ⚠️ 检测机器在海外、没有 IPv6，「仅国内可播」和 IPv6 频道会被误判失效，所以下面的可用数**只少不多**，国内实际能播的更多。

## 一、直播源（直接填进播放器）

### ⭐ 本仓库合并好的「已测可用」列表

已逐个频道探测、去重并按 央视 / 卫视 / 港澳台 / 影视 / 体育 / 春晚 / 地方 分组，共 **333** 个频道（央视 24、卫视 24、港澳台 43、影视 27、体育 7、春晚 38、地方/其他 170）。已内置 EPG 节目单地址。

| 用途 | 地址 |
|---|---|
| 首选（GitHub Pages，国内一般可直连） | `https://passionsu-su.github.io/lx-music/appletv/iptv-tested.m3u` |
| 备用（raw） | `https://raw.githubusercontent.com/passionsu-su/lx-music/main/appletv/iptv-tested.m3u` |
| 备用（国内加速） | `https://ghproxy.net/https://raw.githubusercontent.com/passionsu-su/lx-music/main/appletv/iptv-tested.m3u` |

### 上游订阅源（自动更新，频道更多）

| 名称 | 订阅地址 | 频道数 | 本周探测可播 | 类型 |
|---|---|---|---|---|
| vbskycn/iptv（IPv4，自动更新） | `https://live.zbds.top/tv/iptv4.m3u`<br>备用 `https://raw.githubusercontent.com/vbskycn/iptv/master/tv/iptv4.m3u` | 431 | 131 | IPv4 |
| Guovin/iptv-api 测速结果 | `https://raw.githubusercontent.com/Guovin/iptv-api/gd/output/result.m3u` | 1619 | 134 | IPv4 |
| suxuang/myIPTV（IPv4） | `https://raw.githubusercontent.com/suxuang/myIPTV/main/ipv4.m3u` | 1225 | 101 | IPv4 |
| APTV 官方示例源（Kimentanm/aptv） | `https://raw.githubusercontent.com/Kimentanm/aptv/master/m3u/iptv.m3u` | 120 | 44 | IPv4 |
| hujingguang/ChinaIPTV（自动更新） | `https://raw.githubusercontent.com/hujingguang/ChinaIPTV/main/cnTV_AutoUpdate.m3u8` | 46 | 25 | IPv4 |
| iptv-org 中文频道（全球公开源） | `https://iptv-org.github.io/iptv/languages/zho.m3u` | 228 | 62 | IPv4 |
| iptv-org 台湾 | `https://iptv-org.github.io/iptv/countries/tw.m3u` | 34 | 10 | IPv4 |
| iptv-org 香港 | `https://iptv-org.github.io/iptv/countries/hk.m3u` | 18 | 1 | IPv4 |
| 范明明 fanmingming/live（IPv6，画质好） | `https://live.fanmingming.cn/tv/m3u/ipv6.m3u`<br>备用 `https://raw.githubusercontent.com/fanmingming/live/main/tv/m3u/ipv6.m3u` | 82 | 14 | IPv6（需家宽 IPv6） |
| suxuang/myIPTV（IPv6） | `https://raw.githubusercontent.com/suxuang/myIPTV/main/ipv6.m3u` | 862 | 40 | IPv6（需家宽 IPv6） |
| Free-TV/IPTV（全球免费频道，英文为主） | `https://raw.githubusercontent.com/Free-TV/IPTV/master/playlist.m3u8` | 2197 | 1192 | IPv4 |

### EPG 节目单

| 名称 | 地址 |
|---|---|
| 范明明 EPG（央视/卫视全） | `https://live.fanmingming.cn/e.xml` |
| 112114 EPG | `https://epg.112114.xyz/pp.xml` |

> 用法：播放器里「添加播放列表 / 订阅」→ 粘贴 m3u 地址；EPG 填到「节目单 / XMLTV」。家里宽带有 IPv6 的，优先用范明明 IPv6 源，画质最好。

## 二、IPTV 播放器（tvOS）

| App | 价格 | 支持格式 | 国区 | 说明 | 链接 |
|---|---|---|---|---|---|
| Fjord IPTV Player | 免费，无内购无广告 | M3U / M3U8 / Xtream | ✅ | 完全免费里体验最完整：直播+EPG+点播海报墙，mpv 内核；tvOS 17+ | [打开](https://apps.apple.com/app/id6788160093) |
| Bro IPTV Player | 免费，开源 MIT | M3U / M3U8 / EPG | ✅ | 开源、无广告无账号，支持 PIN 锁播放列表，界面有简体中文 | [打开](https://apps.apple.com/us/app/bro-iptv-player/id6762360135) · [源码](https://github.com/mikehouse/Apple-TV-Player) |
| APTV | 免费下载 + 内购 | M3U / EPG / 回看 | ✅ | 国人开发、中文最友好，频道实时预览、iCloud 同步；免费版有功能限制 | [打开](https://apps.apple.com/cn/app/aptv/id1630403500) · [源码](https://github.com/Kimentanm/aptv) |
| SenPlayer | 免费下载 + 内购 | M3U / M3U8 / TXT 订阅 | ✅ | IPTV + 网盘 + Emby/Jellyfin 一体，支持 TXT 格式直播源 | [打开](https://apps.apple.com/us/app/senplayer-media-player/id6443975850) |
| VLC | 免费，开源 | 单条流 / m3u 文件 | ✅ | 没有频道列表和 EPG，适合临时测试某条地址能不能播 | [打开](https://apps.apple.com/us/app/vlc-media-player/id650377962) |
| UHF | 免费基础版 + PRO | M3U8 / Xtream / Plex / Jellyfin | ❌ 外区 | 界面最像原生 Apple 风格；国区未上架，需外区 Apple ID | [打开](https://apps.apple.com/us/app/uhf-love-your-iptv/id6443751726) |
| IPTVX | 免费下载 + 内购 | M3U / Xtream / Plex / SMB | ✅ | 影视化界面、多画面，完整功能需付费 | [打开](https://apps.apple.com/us/app/iptvx/id1451470024) |
| Revue | 试用 7 天，买断 $9.99 | M3U / HLS / TS / RTSP | ✅ | 专为运营商 IPTV 组播（udpxy / rtp2httpd）优化，需 tvOS 26 | [打开](https://apps.apple.com/us/app/revue-iptv-stream-player/id6816327004) |
| iPlayTV | 买断 ¥38 / $5.99 | M3U / Xtream / EPG | ✅ | 老牌 Apple TV 专用播放器，网格节目单 | [打开](https://apps.apple.com/us/app/iplaytv-iptv-m3u-player/id1072226801) |

> 推荐组合：**Fjord**（全免费）或 **APTV**（中文、国区）+ 上面的「已测可用」列表 + 范明明 EPG。

## 三、浏览器（TestFlight / 开源）

| App | 价格 | 说明 | 链接 |
|---|---|---|---|
| 糖葫芦浏览器 | 免费 TestFlight | 原生 tvOS 浏览器，遥控器光标/滚动/触摸/拖拽四种模式，可看 B 站、YouTube、腾讯视频网页；爱奇艺等 MSE 视频无法播放 | [打开](https://testflight.apple.com/join/WpRhUUyp) · [源码](https://github.com/never88gone/HSBTVBrowser) |
| 糖葫芦浏览工具（同作者备用通道） | 免费 TestFlight | 主通道满员时用这个 | [打开](https://testflight.apple.com/join/QWne6G6V) · [源码](https://github.com/never88gone/HSBTVBrowser) |
| tvOSBrowser | 免费开源 | WKWebView + 标签页，用私有 API，需 Mac + Xcode 自行编译安装 | [打开](https://github.com/jvanakker/tvOSBrowser) |

## 四、第三方 B 站客户端

| App | 价格 | 说明 | 链接 |
|---|---|---|---|
| ATV-Bilibili-demo | 免费开源 | 最成熟：扫码登录、弹幕、直播、4K/HDR、云视听投屏。作者声明无官方 TF，用 nightly 未签名 IPA + Sideloadly / atvloadly 自签 | [打开](https://github.com/yichengchen/ATV-Bilibili-demo/releases/tag/nightly) · [源码](https://github.com/yichengchen/ATV-Bilibili-demo) |
| Danmu TV | 免费开源 | 新项目，杜比视界/弹幕/手机投屏，需 Xcode 自行编译 | [打开](https://github.com/CurryFishBalls9527/DanmuTV/releases) · [源码](https://github.com/CurryFishBalls9527/DanmuTV) |
| Miao Project | App Store 付费（港区 HK$48） | 功能最全：杜比视界/全景声、点赞投币、多账户；不想自签就买它 | [打开](https://github.com/kanezeng/MiaoProject) |
| MiniBili | 免费 TestFlight | tvOS 版仍在开发，目前只有 iPhone/iPad/Mac/Watch，可先在 iPad 上用再 AirPlay | [打开](https://testflight.apple.com/join/TgcHSGwb) · [源码](https://minibili.zhaohe.org/) |

## 五、免费音乐 App

| App | 价格 | 说明 | 链接 |
|---|---|---|---|
| Vibefy（网易云 tvOS） | 免费 TestFlight，开源 | 网易云扫码登录、每日推荐、歌单、云盘、滚动歌词，Apple TV 上最接近洛雪的体验 | [打开](https://testflight.apple.com/join/zJWvzxAK) · [源码](https://github.com/ZhangDo/NeteaseTVDemo) |
| Primuse | App Store 免费 | NAS / Navidrome / Jellyfin / 网盘 / 网络电台一体，tvOS 原生 | [打开](https://apps.apple.com/us/app/primuse-self-hosted-music/id6761675450) |
| Shelv Player | App Store 免费，开源 GPL-3.0 | Navidrome / Subsonic 客户端，iCloud 同步，tvOS 18.6+ | [打开](https://apps.apple.com/us/app/id6762255865) · [源码](https://github.com/gatzenga/Shelv) |
| Spotify | 免费（含广告） | Apple TV 上唯一有免费档的大厂流媒体，需外区账号 | [打开](https://apps.apple.com/us/app/spotify-music-and-podcasts/id324684580) |

> 洛雪音乐目前没有 tvOS 版。想在 Apple TV 上听：用 **Vibefy**，或在 iPhone 上用 LX 的 iOS 构建（见主页客户端表）再 AirPlay 到 Apple TV。

## 六、TestFlight 安装方法

1. iPhone 和 Apple TV 都从 App Store 安装 **TestFlight**，并登录**同一个** Apple ID。
2. 在 iPhone 上用 Safari 打开 TF 链接，点「接受」。
3. 打开 Apple TV 上的 TestFlight，找到该 App 点「安装」。
4. TF 版 90 天过期，到期在 TestFlight 里更新即可；显示「名额已满」就过几天再试。

**自签 IPA（ATV-Bilibili 等）**：Mac 装 Sideloadly 或 atvloadly，用自己的 Apple ID 签名装到 Apple TV；免费 ID 7 天需重签。

## 免责声明

本页只整理公开链接，不存储任何音视频。直播源来自网络公开仓库，可用性随时变化，请只观看你有权收看的内容。TestFlight / 自签应用为第三方作品，请自行甄别。
