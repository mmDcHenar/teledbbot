from sys import argv
import redis
from re import search

userid = redis.Redis()
username = redis.Redis(db=1)

with open(argv[1]) as users:
    for user in users:
        data = search('''{'id': (.*)?, 'username': '(.*)?', 'phone': '(.*)?'}''', user)
        if data:
            try:
                userid.set(data[1], data[3]+';'+data[2])
            except Exception as e:
                input(str(e)+'\n\nsomethings wrong! press Enter to continue...')
                userid.set(data[1], data[3]+';'+data[2])
            try:
                username.set(data[2].lower(), data[3]+';'+data[1])
            except Exception as e:
                input(str(e)+'\n\nsomething wrong! press Enter to continue...')
                username.set(data[2].lower(), data[3]+';'+data[1])
            print(data[3])
input('\n\nLoaded: '+argv[1])

