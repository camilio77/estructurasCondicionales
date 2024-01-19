#verificar si la division es exacta
dividendo = int ( input("digite el dividendo: \n"))
divisor = int ( input("digite el divisor: \n"))
d = dividendo / divisor
a = d - (int(d))
if(a == 0 ):
    print("la division es exacta.")
    print(f"Cociente: {d}")
    print("Resto: 0")
else:
    print("la division no es exacta")
    co = round(d)
    if(d > co):
        print(f"Cociente: {co}")
    else:
        co = co - 1
        print(f"Cociente: {co}")
    res = d - (int(d))
    print(f"Resto: {res}")