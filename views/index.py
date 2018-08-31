
from tornado.web import RequestHandler
import tushare as ts



# 图像化处理方法
class ReadData(RequestHandler):
    def get(self):
        self.render('home.html')


# k线数据，包含历史数据查询 但不包含复权信息
class MainHandler(RequestHandler):
    def get(self):
        content = ts.get_k_data('000007', ktype='60',).to_json(force_ascii=False)
        self.write(content)



# 实时数据 需要设置时间限制
# 实时全部
class TodayData(RequestHandler):
    def get(self):
        content = ts.get_today_all().to_json(force_ascii=False)
        self.write(content)

# 由于单笔和多笔数据，请求方法参数在于字符串和列表的区别
# 采取列表的形式整合两种方法。方便以后post传参
# 实时多笔数据查询
class TodayListData(RequestHandler):
    def get(self):
        content = ts.get_realtime_quotes(['600848','000581']).to_json(force_ascii=False)
        self.write(content)
