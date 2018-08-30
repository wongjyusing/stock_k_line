import tushare as ts

content = ts.get_stock_basics().to_json('static/data/detail.json',force_ascii=False)
