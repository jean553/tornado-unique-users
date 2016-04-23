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

    def get(self, application, month):
        """Get unique users amount by application name and month number."""

        data = dict(
            application=application,
            month=month
        )
        self.cursor.execute("""
            SELECT COUNT(DISTINCT(name))
            FROM users
            WHERE
            application = %(application)s AND
            EXTRACT(MONTH FROM date) = %(month)s
        """, data)
        self.set_status(200)

        result = self.cursor.fetchone()
        self.write(str(result[0]))

    def on_finish(self):
        """Called after response is sent back."""

        self.connection.commit()

    def data_received(self, chunk):
        pass
