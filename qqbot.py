from spider import *
import requests
import json
import time
api = 'https://sc.ftqq.com/SCU99459T0f4dcd6a01a0a9e5696490e07a05eacc5ecdd6b648de6.send'
#server酱的api接口，将{YOUR_KEY}替换成自己的，不需要的可以删除所有带api的语句，仅用于程序出错的通知

def send_msg(msg):
    data = {
        'user_id': '',#qq号(int) 可替换成qq群'group_id':''
        'message': msg,
        'auto_escape': False
    }
    r = requests.post('http://127.0.0.1:5700/send_private_msg', data=data)#qq群：将send_private_msg替换为send_group_msg
    ret = json.loads(r.text)
    if ret['retcode'] != 0:
        data = {
            "text": 'locbot炸了',
            "desp": '发送失败！'
        }
        requests.post(api, data=data)
    else:
        print('发送成功！')
if __name__=="__main__":
     raw_urls,raw_titles=get_urls()
     while(True):
        urls,titles=get_urls()
        if urls is None:
            data = {
                "text": 'locbot炸了',
                "desp": 'cookie没了'
            }
            requests.post(api, data=data)
        print('抓取成功')
        for i in range(10):
            if urls[i] not in raw_urls:
                raw_urls.append(urls[i])
                raw_titles.append(titles[i])   
                send_msg(titles[i]+'\n'+urls[i])
        time.sleep(30)















