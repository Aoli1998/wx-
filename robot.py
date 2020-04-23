import werobot
import requests
myrobot = werobot.WeRoBot(token='1234')
import json


@myrobot.text
def echo(message):
    msg = message.content
    apiurl = "http://127.0.0.1:5000/search/{}".format(msg)
    response = requests.get(apiurl)
    a = response.text
    print(a)
    return a


# 让服务器监听在 0.0.0.0:8000
myrobot.config['HOST'] = '127.0.0.1'
myrobot.config['PORT'] = 8000
myrobot.run()