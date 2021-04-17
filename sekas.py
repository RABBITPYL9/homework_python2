cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[2]},
            {'user': users[1], 'city': cities[0]},
            {'user': users[2], 'city': cities[1]}]

#Иван Лондон
#Мария Москва
#Соня Париж

city = input('Введите город: ')
if city.title() == cities[0]:
    print('Турист', users[1].get('name'), 'возраст', users[1].get('age'), 'посетила город', cities[0])
elif city.title() == cities[1]:
        print('Турист', users[2].get('name'), 'возраст', users[2].get('age'), 'посетила город', cities[1])
elif city.title() == cities[2]:
        print('Турист', users[0].get('name'), 'возраст', users[0].get('age'), 'посетила город', cities[2])
else:
    print("Ошибка")
