# bilibili_seeker
B站视屏数据爬取
本程序循环爬取了B站编号前一万的视屏及其基本信息，包括：
aid(视频编号)、view(播放量)、danmaku(弹幕数)、reply(评论数)、favorite(收藏数)、coin(硬币数)、share(分享数)
为了避免被封IP，每次爬取都有一定的间隔，同时为了加快爬取速度，使用了python多线程技术。
从效果上看，爬取效率还是挺高的。
可以在此基础上对数拓进行处理，包括获取播放量前十的视屏，评论量前十的视频等。
观看视频的链接为 https://www.bilibili.com/video/av + aid。
(本程序使用python2.7版本完成)
