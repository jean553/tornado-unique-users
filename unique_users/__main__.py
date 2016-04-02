"""Main module and URLs handler"""

import signal, time

import tornado.ioloop
import tornado.web
import tornado.httpserver

from unique_users.handlers.UserHandlerAsync import UserHandlerAsync

URL_PATTERNS = [
    ("/user", UserHandlerAsync),
]
SHUTDOWN_SECONDS_TIMEOUT = 5

def make_safe_shutdown(application):
    """Attachs signals to the function that
    shutdowns the application gracefully on
    SIGTERM and SIGINT."""

    def safe_shutdown(*args, **keywords):
        """Stops tornado HTTP server, get the current loop instance,
        set the deadline for shutdown (current time + defined timeout),
        calls the recursive shutdown function."""

        application.stop()
        instance = tornado.ioloop.IOLoop.instance()
        deadline = time.time() + SHUTDOWN_SECONDS_TIMEOUT

        def shutdown():
            """Execute this recursive function every second as long
            as I/O loop actions are not all terminated or the limit time
            is not elapsed. Stop the instance."""

            now = time.time()
            if now < deadline and (instance._callbacks or instance._timeouts):
                instance.add_timeout(now + 1, shutdown)
            else:
                instance.stop()

        shutdown()

    signal.signal(signal.SIGINT, safe_shutdown)
    signal.signal(signal.SIGTERM, safe_shutdown)

def make_application():
    """Get the tornado application routes"""
    return tornado.httpserver.HTTPServer(tornado.web.Application(URL_PATTERNS))

if __name__ == '__main__':
    APP = make_application()
    APP.listen(8080)
    make_safe_shutdown(APP)
    tornado.ioloop.IOLoop.current().start()
