import requests
from lxml import etree

def login():
    session=requests.session()
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }
    url = "https://www.hostloc.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1"
    data = {
        'fastloginfield': 'username',
        'username': 'Lemoon',
        'password': 'Z454599012jude.',
        'quickforward': 'yes',
        'handlekey': 'ls'
    }
    r = session.post(url, data, header)
    return r.cookies
    
def get_urls():
    global response
    url = 'https://www.hostloc.com/forum.php?mod=forumdisplay&fid=45&filter=author&orderby=dateline'
    api = 'https://sc.ftqq.com/SCU99459T0f4dcd6a01a0a9e5696490e07a05eacc5ecdd6b648de6.send'
    #server酱的api接口，将{YOUR_KEY}替换成自己的，不需要的可以删除所有带api的语句，仅用于程序出错的通知
    headers = {
        'referer': 'https://www.hostloc.com/forum.php?mod=forumdisplay&fid=45&filter=author&orderby=dateline',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
        }#新版去除了麻烦的cookie，直接登录即可
    try:
        response = requests.get(url, headers=headers)
        print(response.status_code)
    except Exception as e:
        data = {
            "text": 'locbot炸了',
            "desp": e
        }
        requests.post(api, data=data,cookie=login())
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
