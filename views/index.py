
from tornado.web import RequestHandler
import tushare as ts
import sqlite3


# 图像化处理方法
class ReadData(RequestHandler):
    def get(self):
        self.render('home.html')



# k线数据
class MainHandler(RequestHandler):
    def get(self):
        #content = ts.get_hist_data('600848').to_json(orient='columns')
        content = ts.get_k_data('000007', ktype='60',).to_json()
        #print(type(content))
        self.write(content)






# 实时数据 需要设置时间限制

# 实时全部
class TodayData(RequestHandler):
    def get(self):
        content = ts.get_today_all().to_json(force_ascii=False)
        self.write(content)

# 单笔和多笔数据的传参方法是一样的，后期需要进行优化
# 实时单笔数据查询
class TodaySingleData(RequestHandler):
    def get(self):
        content = ts.get_realtime_quotes('000581').to_json(force_ascii=False)
        self.write(content)

# 实时多笔数据查询
class TodaySingleData(RequestHandler):
    def get(self):
        content = ts.get_realtime_quotes(['600848','000980','000981']).to_json(force_ascii=False)
        self.write(content)
