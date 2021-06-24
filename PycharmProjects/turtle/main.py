from collections import Counter, OrderedDict, namedtuple, deque

accounts = {
    'saving': 1300,
    'current': 2000
}


def add_balance(name, amount):
    accounts[name] += amount
    print(accounts[name])
    return accounts[name]


transactions = [
    ('saving', 40000),
    ('current', 12000),
    ('saving', -18000),
    ('current', -10000),
    ('saving', -5000),
]


for t in transactions:
    add_balance(name=t[0], amount=t[1])


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


users = [
    {'username': 'gaurav jain', 'password': 'ks271990'},
    {'username': 'jugal kishore jain', 'password': 'shanu@781'}
]

a = [User(data['username'], data['password']) for data in users]
a1 = [User(**data) for data in users]

ages = ['17', '17', '13', '13', '13', '15', '15']

print(Counter(ages))

book = OrderedDict()

book['vistas'] = 'n.c.e.r.t'
book['flamingo'] = 'n.c.e.r.t'
book['indian economic development'] = 'radha bahuguna'

print(book)

book.move_to_end('vistas')

print(book)

book.move_to_end('indian economic development', last=False)

print(book)

book.pop('vistas')

print(book)

book.popitem()

print(book)

me = ('gaurav', '11', 17, 'commerce WEB')

myself = namedtuple('myself', ['name', 'standard', 'age', 'field'])

me = myself('gaurav', '11', 17, 'commerce WEB')

print(me)

print(me.name)
print(me.age)
print(me.standard)
print(me.field)

b = myself(*me)

print(b)

c = myself._make(me)

print(c)
print(c._asdict())
print(c._asdict()['name'])
print(c._asdict()['age'])
print(c._asdict()['standard'])
print(c._asdict()['field'])

friends = deque(('gaurav', 'tushar', 'dhruv', 'sahil', 'lakshya'))

print(friends)

friends.append('hardik')
friends.appendleft('jai mishra')

print(friends)

friends.pop()
friends.popleft()

print(friends)

import re

list_of_emails =[
    'gauravjain@gmail.com',
    'salonijain2011@facebook.com',
    'jaindivyans2000@hotmail.com',
    'dimplegoyal2002@gmail.com'
]

user_name_list = []
domain_name_list = []

for e in list_of_emails:
    splited_data = e.split('@')

    user_name = splited_data[0]
    domain = splited_data[1]

    user_name_list.append(user_name)
    domain_name_list.append(domain)

print(user_name_list)
print(domain_name_list)

print(Counter(user_name_list))
print(Counter(domain_name_list))