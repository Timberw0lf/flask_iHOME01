# -*- coding:utf-8 -*-
import redis


class Config(object):
    """配置参数"""

    DEBUG = True

    # 秘钥
    SECRET_KEY = 'q7pBNcWPgmF6BqB6b5VICF7z7pI+90o0O4CaJsFGjzRsYiya9SEgUDytXvzFsIaR'

    # 配置mysql数据库：真实开发应该写数据库的真实ip地址
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/db_iHome_01'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置redis数据库：实际开发也必须填写真实的redis数据库ip
    # 模仿mysql数据库，实际上redis的配置参数，不是从Config中默认读取的
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # 配置session参数
    # 指定session存储到redis
    SESSION_TYPE = 'redis'
    # 指定要使用的redis的位置
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 是否使用secret_key签名session_data
    SESSION_USE_SIGNER = True
    # 设置session的过期时间
    PERMANENT_SESSION_LIFETIME = 3600 * 24  # 有效期为一天