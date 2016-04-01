"""Contains the user requests handler"""

import tornado.web

class UserHandlerAsync(tornado.web.RequestHandler):
    """Handler of user actions requests"""

    def get(self):
        self.write('OK')

    def data_received(self, chunk):
        pass
