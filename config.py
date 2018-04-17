# -*- coding:utf-8 -*-
# 配置参数

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


# 为了让项目的配置文件能适应不同环境（开发、测试、线上），抽取不同环境下的配置到配置类的子类，
# 让实例能根据当前开发环境选择不同的配置子类从而选择不同的配置

# 但这种方式仍有缺点：业务模块的初始化文件里的代码，仍然要根据环境的不同而进行更改，
# 而在真正的开发过程中，通过测试后的业务模块是不能轻易更改的，(而业务逻辑模块以外的代码是可以更改的)
# 更改之后，又必须进行从新测试，增加了很大的测试工作量，所以，需要解决这个问题（工厂设计模式）

class Development(Config):
    """开发模式下的配置"""
    pass


class Production(Config):
    """生产环境、上线、部署之后的配置"""

    # 部署正式运行之后，就不能再用调试模式了
    DEBUG = False

    # 项目上线以后的mysql数据库：可能跟开发时的数据库不一样
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/db_iHome'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class UnitTest(Config):
    """测试环境"""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/db_iHome_unittest'

# 工厂设计模式的工厂：
configs = {
    'dev': Development,
    'prod': Production,
    'test': UnitTest
}