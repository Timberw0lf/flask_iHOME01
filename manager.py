# -*- coding:utf-8 -*-
# 程序入口


from flask import Flask


app = Flask(__name__)


class Config(object):
    """封装配置类"""
    DEBUG = True


app.config.from_object(Config)


@app.route('/')
def index():
    return 'index!'


if __name__ == '__main__':
    app.run(debug=True)
