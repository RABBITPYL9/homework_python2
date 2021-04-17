cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[2]},
            {'user': users[1], 'city': cities[0]},
            {'user': users[2], 'city': cities[1]}]

city = input('Введите город: ').capitalize()

if city in cities:
    index = cities.index(city)
    for i in tourists:
        if cities[index] == i['city']:
            user_index = i['user']
            city_visited = i['city']
            names = user_index['name']
            ages = user_index['age']
            print(f'Турист {names} возраст {ages}.Посетил город {city_visited}')  
        
            
 #f'Турист {user_index['name']} возраст {user_index['age']}.Посетил город {i['city']})       