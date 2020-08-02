# Hostloc-qqbot
A qqbot for hostloc



**2020.8.2 酷Q已死** 


语言：Python 3.7.6
主要库：requests lxml

# 运行
第一次运行先执行pip install -r requirements.txt，程序需要自行替换参数！！**详情见注释** ~~目前对小白不怎么友善，后期改进。~~ 已改进
需配合[CQA](https://cqp.cc/)和[CQHTTP](https://cqhttp.cc/docs/4.15/)插件使用
有问题可以发issue或者[email](mailto:lemoon@lemoon.ml)
~~## cookie需手动获取
试了半天被loc封了IP，暂且先手动吧。
打开[https://www.hostloc.com/forum.php?mod=forumdisplay&fid=45&filter=author&orderby=dateline](https://www.hostloc.com/forum.php?mod=forumdisplay&fid=45&filter=author&orderby=dateline)
按F12打开开发者工具，选择network，按Ctrl+R重新载入，在搜索框搜索"forum.php"，选择，找到Request Header里面的cookie替换即可~~
## 关于cookie
先clone项目，之后在account.json里面输入用户名密码即可自动获取cookie，是否还会触发反爬还有待验证
