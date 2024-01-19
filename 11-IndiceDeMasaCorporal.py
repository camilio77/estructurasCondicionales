#detectar riesgo de enfermedad coronaria
edad = int ( input ("ingrese su edad: \n"))
esta = float ( input ("ingrese su estatura en metros: \n"))
peso = int ( input ("ingrese su peso: \n"))
IMC = peso / ((esta)**2)
if (edad < 45):
    if(IMC < 22.0):
        print("su riesgo de padecer enfermedades coronarias es bajo")
    else:
        print("su riesgo de padecer enfermedades coronarias es medio")
else:
    if(IMC < 22.0):
        print("su riesgo de padecer enfermedades coronarias es medio")
    else:
        print("su riesgo de padecer enfermedades coronarias es alto, cuidese")
