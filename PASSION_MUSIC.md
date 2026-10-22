# Passion Music（Android TV）

基于 [bmizhou/lx-music-tv](https://github.com/bmizhou/lx-music-tv)（Apache-2.0）构建的电视版音乐播放器，修改内容：

- 应用名改为 **Passion Music**，TV 桌面横幅改为 Passion Music
- 包名改为 `com.passion.music.tv`，可与原版共存
- Release 包使用仓库内 `keystore/passion-music.p12` 签名，后续版本可覆盖升级
- GitHub Actions 自动构建并发布 APK 到 Releases

使用：设置 → 播放源管理 → 导入洛雪 JS 音源（音源链接见 main 分支 README / 一键复制网页）。

## v3.0 新增
- **内置音源**：构建时自动从 main 分支 `sources.json` 拉取最新可用音源打包；首次启动全部导入，并自动启用 六音 / Huibq / 野花 / ikun。之后升级只更新脚本内容，保留你的启用状态，删掉的不会再加回。
- **扫码一键导入**：设置 → 播放源管理 → 打开 HTTP 服务器，手机扫屏幕上的二维码，在网页「一键导入音源」里点「导入」，电视直接下载（失败时自动走 ghproxy / jsDelivr 镜像）。也可粘贴任意 JS 音源链接。
- **自动更新**：main 分支每周一检测音源，有变化时自动触发本分支重新打包发布。
