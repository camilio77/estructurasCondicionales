#identificar caracter
ca = input("ingrese caracter: ")
if(ca >= "0" and ca <= "9"):
    print("El caracter es un numero")
elif(ca >= "a" and ca <= "z"):
    print("El caracter es una letra minuscula")
elif(ca >= "A" and ca <= "Z"):
    print("El caracter es una letra mayuscula")
else:
    print("El caracter no es ni letra ni numero")