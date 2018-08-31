from views import index

urlpatterns = [
    (r'/', index.MainHandler),
    (r'/read',index.ReadData),
    (r'/today',index.TodayData),
    (r'/todaylist',index.TodayListData),
    (r'/range_k_line',index.ReadKLine),
]
