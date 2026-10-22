# Passion Music（Android TV）

基于 [bmizhou/lx-music-tv](https://github.com/bmizhou/lx-music-tv)（Apache-2.0）构建的电视版音乐播放器，修改内容：

- 应用名改为 **Passion Music**，TV 桌面横幅改为 Passion Music
- 包名改为 `com.passion.music.tv`，可与原版共存
- Release 包使用仓库内 `keystore/passion-music.p12` 签名，后续版本可覆盖升级
- GitHub Actions 自动构建并发布 APK 到 Releases

使用：设置 → 播放源管理 → 导入洛雪 JS 音源（音源链接见 main 分支 README / 一键复制网页）。
