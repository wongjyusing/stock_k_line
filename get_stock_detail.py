import tushare as ts

content = ts.get_stock_basics().to_json('static/data/detail.json',force_ascii=False)
#content = ts.get_k_data('000007', ktype='D',start='2018-01-01',end='2018-0901').to_json('data.json',force_ascii=False,)

'''
code ,股票代码
name,名称
industry,所属行业
area,地区
pe,市盈率
outstanding,流通股本(亿)
totals,总股本(亿)
totalAssets,总资产(万)
liquidAssets,流动资产
fixedAssets,固定资产
reserved,公积金
reservedPerShare,每股公积金
esp,每股收益
bvps,每股净资
pb,市净率
timeToMarket,上市日期
undp,未分利润
perundp, 每股未分配
rev,收入同比(%)
profit,利润同比(%)
gpr,毛利率(%)
npr,净利润率(%)
holders,股东人数
'''
