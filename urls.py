from views import index

urlpatterns = [
    (r'/', index.MainHandler),
    (r'/read',index.ReadData),
    (r'/today',index.TodayData),
    (r'/todaysingle',index.TodaySingleData),

]
