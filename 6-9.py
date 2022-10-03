# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)
from collections import ChainMap

data = {
    0: {"name": "alex",
        "surname": "lev",
        "phone": 12345678,
        "email": "dasdas@mail.com"
    },
    1: {"name": "vik",
        "surname": "sol",
        "phone": 12345678,
        "email": None
    },
    2: {"name": "anna",
        "surname": "qwerty",
        "ephone": 12345678,
        None: "123ws@mail.com"
    }
}

for key, user in data.copy().items():
    if user.get('email'):
        del data[key]
print(data)

#     for i in data.items():
#        if {"mail"} is None:
        #print(v)

