class DEVconfig(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/test'
# 'mysql+pymysql://用户名称:密码@localhost:端口/数据库名称'
# SQLAlchemy 将会记录所有发到标准输出(stderr)的语句，这对调试很有帮助。
    SQLALCHEMY_ECHO = True

# Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
    SQLALCHEMY_TRACK_MODIFICATIONS = True
