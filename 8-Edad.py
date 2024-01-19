#identificar tu edad
from time import localtime
t = localtime()
print("ingrese su fecha de nacimiento.")
dia = int(input("dia: "))
mes = int(input("mes: "))
año = int(input("año: "))
dh = t.tm_mday
mh = t.tm_mon
ah = t.tm_year
ed = ah - año
if(mes <= mh):
    if(dia <= dh):
        print(f"tienes {ed} años")
    else:
        ed = ed - 1
        print(f"tienes {ed} años")
else:
    ed = ed - 1
    print(f"tienes {ed} años")
    