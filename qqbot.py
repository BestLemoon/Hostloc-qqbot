from spider import *
import requests
import json
import time
api = 'https://sc.ftqq.com/{YOUR_KEY}.send'
#server酱的api接口，将{YOUR_KEY}替换成自己的，不需要的可以删除所有带api的语句，仅用于程序出错的通知
def send_msg(msg):
    data = {
        'group_id': '',#qq群号(int) 可替换成个人'user_id':''
        'message': msg,
        'auto_escape': False
    }
    r = requests.post('http://127.0.0.1:5700/send_group_msg', data=data)#个人：将send_group_msg替换为/send_private_msg
    ret = json.loads(r.text)
    if ret['retcode'] != 0:#qq发送状态
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
        for i in range(len(urls)):
            if urls[i] not in raw_urls:
                raw_urls.append(urls[i])
                raw_titles.append(titles[i])
                send_msg(titles[i]+'\n'+urls[i])
        time.sleep(5)















