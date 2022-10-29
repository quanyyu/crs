import gevent
from gevent import monkey
monkey.patch_all()

import requests

def get_baidu():
    rsp = requests.get("https://api.baidu.com")
    print(rsp.text)
    return rsp.text

if __name__ == '__main__':
    f1 = gevent.spawn(get_baidu)
    print("11")
    f1.join()