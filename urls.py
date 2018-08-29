from views import index

urlpatterns = [
    (r'/', index.MainHandler),
    (r'/read',index.ReadData),
]
