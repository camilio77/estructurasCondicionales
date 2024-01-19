#comprobar datos de un set de tenis
pa = int (input("ingrese los partidos ganados por el tenista a: "))
pb = int ( input("ingrese los partidos ganados por el tenista b: "))
if((pa >= 6) and ((pa - pb) >= 2)) or ((pa == 7) and (pb == 6)):
    s = (pa == 7)
    a = (pb >= 5)
    if((s==True) and (a ==True)):
        print("el ganador del set es el tenista a")
    elif(s==False):
        print("el ganador del set es el tenista a")
    else:
        print("el resultado es invalido")
elif (((pa == 5) and (pb == 5)) or ((pa == 6) and (pb ==6))) or ((pa <= 5) and (pb <=5)) or ((pa == 5) and (pb == 6)) or ((pa == 6) and (pb == 5)):
    print("el set aun no acaba")
elif((pb >= 6) and ((pb - pa) >= 2)) or ((pb == 7) and (pa == 6)):
    s = (pb == 7)
    a = (pa >= 5)
    if((s==True) and (a ==True)):
        print("el ganador del set es el tenista b")
    elif(s==False):
        print("el ganador del set es el tenista b")
    else:
        print("el resultado es invalido")
else:
    print("el resultado es invalido")
