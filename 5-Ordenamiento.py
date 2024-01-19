#ordenar secuencia de numeros
a = int(input("cuantos numeros desea ordenar (2 - 3 - 4): "))
b = 1
num = []
while(b <= a):
    num.append(int(input("ingrese un numero: ")))
    b = b + 1
num.sort()
print(f"la lista ordenada de menor a mayor es: \n {num} ")