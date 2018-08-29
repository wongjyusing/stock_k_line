from tornado.web import Application
from config import settings,options
from urls import urlpatterns

class NewApp(Application):
    def __init__(self):
        handlers = urlpatterns
        # 这里可填写连接数据库代码，并生成游标
        port_num = options['port']
        print('服务器程序启动成功')
        print(f'请打开浏览器输入 http://127.0.0.1:{port_num}')
        print('按下 Ctrl + C 退出服务器程序')
        Application.__init__(self, handlers,**settings)  # , debug=True)

'''

client = pymongo.MongoClient(host='127.0.0.1', port=27017)
#db_auth = client.admin
#db_auth.authenticate('test_user', '123456')
self.db = client['runoob']
'''
