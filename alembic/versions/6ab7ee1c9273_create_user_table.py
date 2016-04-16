"""create user table

Revision ID: 6ab7ee1c9273
Revises: 
Create Date: 2016-04-07 01:18:55.804328

"""

# revision identifiers, used by Alembic.
revision = '6ab7ee1c9273'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op

def upgrade():
    conn = op.get_bind()
    conn.execute(' \
        CREATE TABLE users ( \
            id SERIAL PRIMARY KEY, \
            name VARCHAR(255), \
            application VARCHAR(255), \
            date TIMESTAMP \
        )' \
    )

def downgrade():
    conn = op.get_bind()
    conn.execute('DROP TABLE users')
