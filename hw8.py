import pandas
import collections
slovar = {}
open_log = pandas.read_excel('logs.xlsx', sheet_name='log')
log_data_dict = open_log.to_dict(orient='records')
slovar = log_data_dict
slov_rez = {}
for element in slovar:
    slovar = element['Браузер']#создаем список в словарь со всеми браузерами
    if slovar in slov_rez.keys(): 
        slov_rez[slovar] += 1
    else:
        slov_rez[slovar] = 1

maximum = 0
item_title = ''
for k, v in slov_rez.items():
    if v > maximum:
        maximum = v
        item_title = k
print(f'Самый популярный браузер: {item_title}')

