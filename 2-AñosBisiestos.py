#calcular año bisiesto
año = int(input("ingrese un año: "))
if (año % 4 == 0):
    if(año > 1582):
        if(año % 100 == 0):
            if((año % 400 == 0)):
                print("el año es bisiesto")
            else:
                print("el año no es bisiesto")
        else:
            print("el año es bisiesto")
    else:
        print("el año es bisiesto")
else:
    print("el año no es bisiesto")