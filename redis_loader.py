from sys import argv
import redis
from re import search

r = redis.Redis()
r2 = redis.Redis(db=1)

with open(argv[1]) as users:
    for user in users:
        data = search('''{'id': (.*)?, 'username': '(.*)?', 'phone': '(.*)?'}''', user)
        r.set(data[1], data[3])
        r2.set(data[2], data[3])
        print(data[3])
input('\n\nLoaded: '+argv[1])
