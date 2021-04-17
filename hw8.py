import pandas
import collections
slovar = {}
open_log = pandas.read_excel('logs.xlsx', sheet_name='log')
log_data_dict = open_log.to_dict(orient='records')
slovar = log_data_dict
slov_rez = {}
top1 = {}
top2 = {}
top3 = {}
top4 = {}
top5 = {}
top6 = {}
top7 = {}
for element in slovar:
    slovar = element['Браузер']#создаем список в словарь со всеми браузерами
    if slovar in slov_rez.keys(): 
        slov_rez[slovar] += 1
        for k, v in slov_rez.items():
            if v > 450:
                #print(k)
                top1 = k
            elif v > 240:
                
                top2 = k
            elif v > 185:

                top3 = k
            elif v > 160:
                
                top4 = k
            elif v > 143:
                
                top5 = k
            elif v > 90:
                
                top6 = k
            elif v > 50:

                top7 = k
                

        
    else:
        slov_rez[slovar] = 1

print(top1)
print(top2)
print(top3)
print(top4)
print(top5)
print(top6)
print(top7)


