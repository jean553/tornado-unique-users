import tornado.web

import urls

def make_app():
    return tornado.web.Application(urls.url_patterns)
