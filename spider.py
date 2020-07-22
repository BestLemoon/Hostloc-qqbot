import requests
from lxml import etree


def get_urls():
    global response
    url = 'https://www.hostloc.com/forum.php?mod=forumdisplay&fid=45&filter=author&orderby=dateline'
    api = 'https://sc.ftqq.com/{YOUR_KEY}.send'
    #server酱的api接口，将{YOUR_KEY}替换成自己的，不需要的可以删除所有带api的语句，仅用于程序出错的通知
    headers = {
        'referer': 'https://www.hostloc.com/forum.php?mod=forumdisplay&fid=45&filter=author&orderby=dateline',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'cookie': ''
    }#cookie为自己摘取的，应该不具有兼容性，若urls和titles没有内容，是触发了反爬机制，后期考虑再改进
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        data = {
            "text": 'locbot炸了',
            "desp": e
        }
        requests.post(api, data=data)
    urls = []
    #print(response.text)
    html = etree.HTML(response.text)
    href = html.xpath('//th[@class="new"]/a[3]/@href')
    for i in range(len(href)):
        href[i]=href[i].replace('&extra=page%3D1%26filter%3Dauthor%26orderby%3Ddateline','')
    titles = html.xpath('//th[@class="new"]/a[3]/text()')
    for i in range(len(href)):
        urls.append('https://www.hostloc.com/' + href[i])
    print(urls,titles)
    return urls, titles
