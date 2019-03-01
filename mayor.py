

positivos=0
negativos=0
ceros=0

i=0
for i in range(0,11):
    a=int(input("Introduzca un valor: "))
    if a==0:
        print(a)
        ceros=ceros+1
    elif a>0:
        print(a)
        positivos=positivos+1
    else:
        print(a)
        negativos=negativos+1

print("los positivos son: ",positivos)
print("los positivos son: ",negativos)
print("los positivos son: ",ceros)
