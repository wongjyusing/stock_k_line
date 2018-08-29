import tornado.httpserver
import tornado.ioloop
import tornado.web
from applications import NewApp
import config




if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(NewApp())
    http_server.bind(config.options['port'])
    http_server.start()
    tornado.ioloop.IOLoop.current().start()
    
