# Hostloc-qqbot
A qqbot for hostloc

语言：Python 3.7.6
主要库：requests lxml

# 运行
第一次运行先执行pip install -r requirements.txt，程序需要自行替换参数！！**详情见注释**目前对小白不怎么友善，后期改进，有问题可以发issue或者[email](mailto:lemoon@lemoon.ml)
## cookie需手动获取
试了半天被loc封了IP，暂且先手动吧。
打开[https://www.hostloc.com/forum.php?mod=forumdisplay&fid=45&filter=author&orderby=dateline](https://www.hostloc.com/forum.php?mod=forumdisplay&fid=45&filter=author&orderby=dateline)
按F12打开开发者工具，选择network，按Ctrl+R重新载入，在搜索框搜索"forum.php"，选择，找到Request Header里面的cookie替换即可
