#identificar triangulo
c1 = float(input("ingrese la medida en centimetros de un lado del triangulo: \n"))
c2 = float(input("ingrese la medida en centimetros de un lado del triangulo: \n"))
c3 = float(input("ingrese la medida en centimetros de un lado del triangulo: \n"))
if((c1 + c2) < c3) or ((c1 + c3) < c2) or ((c3 + c2) < c1):
    print("el triangulo es invalido")
elif((c1 == c2) and c1 != c3) or ((c1 == c3) and c1 != c2) or ((c3 == c2) and c3 != c1):
    print("el triangulo es isoceles")
elif(c1 == c2 == c3):
    print("el triangulo es equilatero")
elif(c1 != c2 != c3 ):
    print("el triangulo es escaleno")