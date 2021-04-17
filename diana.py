cities = ['Москва', 'Париж', 'Лондон']



users = [{'name': 'Иван', 'age': 35},

         {'name': 'Мария', 'age': 22},

         {'name': 'Соня', 'age': 20}]



tourists = [{'user': users[0], 'city': cities[2]},

            {'user': users[1], 'city': cities[0]},

            {'user': users[2], 'city': cities[1]}]



city = input('Введите город: ')



if city.capitalize() == cities[2]:

    print('Турист', users[0].get('name'), 'возвраст', users[0].get('age'), '. Посетил город ', cities[2])



if city.capitalize() == cities[1]:

    print('Турист', users[2].get('name'), 'возвраст', users[2].get('age'), '. Посетил город ', cities[1])



if city.capitalize() == cities[0]:

    print('Турист', users[1].get('name'), 'возвраст', users[1].get('age'), '. Посетил город ', cities[0])