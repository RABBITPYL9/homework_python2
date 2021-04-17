import os

a = os.environ
print(a)
for valik in a.values():
    if valik == 'Sergey':
        print("NAYDENO", valik)
    #else:
        #print("404")
