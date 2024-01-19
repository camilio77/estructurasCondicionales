#calculadora
n1 = int(input("ingrese numero 1: "))
n2 = int(input("ingrese numero 2: "))
op = (input("seleccione su operacion, suma(+), resta(-), multiplicacion(*), division(/), potencia(**): \n"))
if(op == "+"):
    s = n1 + n2
    print(s)
elif op == "-":
    n = n1 - n2
    print(n)
elif op == "*":
    m = n1 * n2
    print(m)
elif op == "/":
    d = n1 / n2
    print(d)
elif op == "**":
    p = n1 ** n2
    print(p)
else:
    print("error")