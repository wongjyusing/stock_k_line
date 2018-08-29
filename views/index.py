
from tornado.web import RequestHandler
import tushare as ts

class MainHandler(RequestHandler):
    def get(self):
        #content = ts.get_hist_data('600848').to_json(orient='columns')
        content = ts.get_k_data('600000', ktype='W',).to_json(orient='columns')
        #print(type(content))
        self.write(content)



class ReadData(RequestHandler):
    def get(self):
        self.render('test.html')

'''
content = self.application.db.runoob.find_one()
print(content)
'''
