"""Main module and URLs handler"""

import tornado.ioloop
import tornado.web

from unique_users.handlers.UserHandlerAsync import UserHandlerAsync

URL_PATTERNS = [
    ("/user", UserHandlerAsync),
]

def make_application():
    """Get the tornado application routes"""
    return tornado.web.Application(URL_PATTERNS)

if __name__ == '__main__':
    APP = make_application()
    APP.listen(8080)
    tornado.ioloop.IOLoop.current().start()
