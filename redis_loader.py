from sys import argv
import redis
from re import search

userid = redis.Redis()
username = redis.Redis(db=1)

with open(argv[1]) as users:
    for user in users:
        data = search('''{'id': (.*)?, 'username': '(.*)?', 'phone': '(.*)?'}''', user)
        if data:
            userid.set(data[1], data[3]+';'+data[2])
            username.set(data[2], data[3]+';'+data[1])
            print(data[3])
input('\n\nLoaded: '+argv[1])
