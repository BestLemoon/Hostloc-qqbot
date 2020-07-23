import requests
from lxml import etree
import json


def get_account():
    with open('account.json', encoding='utf-8') as file:
        information = json.load(file)
    return information['username'], information['passwd']


def login():
    username, passwd = get_account()
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }
    url = "https://www.hostloc.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1"
    data = {
        'fastloginfield': 'username',
        'username': username,
        'password': passwd,
        'quickforward': 'yes',
        'handlekey': 'ls'
    }
    r = requests.post(url, data, header)
    return r.cookies


def get_urls():
    global response
    url = 'https://www.hostloc.com/forum.php?mod=forumdisplay&fid=45&filter=author&orderby=dateline'
    api = 'https://sc.ftqq.com/{YOUR_KEY}.send'#server酱推送，自行替换
    headers = {
        'referer': 'https://www.hostloc.com/forum.php?mod=forumdisplay&fid=45&filter=author&orderby=dateline',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        print(response.status_code)
    except Exception as e:
        data = {
            "text": 'locbot炸了',
            "desp": e
        }
        requests.post(api, data=data)
    urls = []
    # print(response.text)
    html = etree.HTML(response.text)
    href = html.xpath('//th[@class="new"]/a[3]/@href')
    for i in range(len(href)):
        href[i] = href[i].replace('&extra=page%3D1%26filter%3Dauthor%26orderby%3Ddateline', '')
    titles = html.xpath('//th[@class="new"]/a[3]/text()')
    for i in range(len(href)):
        urls.append('https://www.hostloc.com/' + href[i])
    print(urls, titles)
    return urls, titles
