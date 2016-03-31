import tornado.web

class UserHandlerAsync(tornado.web.RequestHandler):
    def get(self):
        self.write('OK')
