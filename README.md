#tornado-unique-users

REST API to handle unique users in a set of users, uploaded with username, app name and date.

The API can add users in the set and returns the amount of unique users by time.

Use Tornado, PostgreSQL, Vagrant, Docker. The REST API uses asynchrone features of Tornado.

## Installation

```
vagrant up --provider docker --no-parallel
``` 

( --no-parallel is used to prevent Vagrant to start the two containers in parallel, as Docker supports it )

```
vagrant ssh dev
sudo pip install tornado
```

## Run

```
vagrant ssh dev
cd /vagrant
python -m "unique_users"
```

## Tests

```
vagrant ssh dev
cd /vagrant/unique_users
tox
```

## Coverage

Start the service (run the tests just after):
```
coverage run -m source=unique_users/ unique_users
```

Check the coverage:
```
coverage report -m
```
