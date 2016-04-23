"""Contains the user requests handler"""

import tornado.web
import json

class UserHandlerAsync(tornado.web.RequestHandler):
    """Handler of user actions requests"""

    def initialize(self, connection):
        """Get the database connection before request management"""

        self.connection = connection
        self.cursor = connection.cursor()

    def post(self):
        """Handles the user creation."""

        data = json.loads(self.request.body)
        sql = """
            INSERT INTO users (
                name,
                application,
                date
            ) VALUES (
                %(name)s,
                %(application)s,
        """

        if 'date' not in data:
            sql += 'CURRENT_TIMESTAMP'
        else:
            sql += '(TIMESTAMP %(date)s)'
        sql += ')'

        self.cursor.execute(sql, data)
        self.set_status(201)

    def on_finish(self):
        """Called after response is sent back."""
        self.connection.commit()

    def data_received(self, chunk):
        pass
