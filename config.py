import os

BASE_DIR = os.path.dirname(__file__)

options = {
    'port':8888
}


settings = {
    'template_path':os.path.join(BASE_DIR, "templates"),
    'static_path':os.path.join(BASE_DIR, "static"),
    'xsrf_cookies':True,
    'debug':True,

    }
