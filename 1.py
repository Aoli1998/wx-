# coding:utf8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from robot import myrobot
from werobot.contrib.flask import make_view

app = Flask(__name__)
app.add_url_rule(rule='/robot/', # WeRoBot 挂载地址
                 endpoint='werobot', # Flask 的 endpoint
                 view_func=make_view(myrobot),
                 methods=['GET', 'POST'])




if __name__ == '__main__':
    app.run(port=8000, debug=True)