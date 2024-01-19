#identicar cual calabra es mas larga
pa = (input("digite una palabra: "))
pa2 = (input("digite otra palabra: "))
a = len(pa)
b = len(pa2)
if(a > b):
    print(f"la palabra {pa} tiene {a - b} letras mas que {pa2}")
elif(b > a):
    print(f"la palabra {pa2} tiene {b - a} letras mas que {pa}")