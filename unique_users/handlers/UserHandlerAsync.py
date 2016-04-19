"""Contains the user requests handler"""

import tornado.web
import json
import psycopg2
import os

class UserHandlerAsync(tornado.web.RequestHandler):
    """Handler of user actions requests"""

    def prepare(self):
        """Connect to the database before request."""

        try:
            self.conn = psycopg2.connect(
                database=os.getenv('DB_NAME', 'vagrant'),
                user=os.getenv('DB_USER', 'vagrant'),
                password=os.getenv('DB_PASSWORD', 'vagrant'),
                host=os.getenv('DB_HOST', 'db'),
            )
            self.cursor = self.conn.cursor()
        except psycopg2.Error:
            self.send_error()

    def post(self):
        """Handles the user creation."""

        data = json.loads(self.request.body)
        self.cursor.execute("""
            INSERT INTO users (
                name,
                application,
                date
            ) VALUES (
                %(name)s,
                %(application)s,
                CURRENT_TIMESTAMP
            )
        """, data)
        self.set_status(201)

    def on_finish(self):
        """Close the connection to the database."""

        if 'conn' not in locals():
            return

        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def data_received(self, chunk):
        pass
