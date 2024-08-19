
""" 
Ejercicios de jonhy
"""

# sDni = "2040143154"
# sDni2 = 2040143154
# secuencia = "2345672345"
# print(sDni)
# print(type(sDni))
# print(sDni[2])
# print(sDni2)
# print(type(sDni2))
# vectorRever = reversed(vector)

# vectorRever = sorted(vector, reverse=1)

# for vector in reversed()

# rVector = vector
# vector.__reversed__()

# revSecuencia = ""
# for k in secuencia[::-1]:
#     revSecuencia+= k
    
# print(revSecuencia)
# 5432765432
# --------------------
# x = sDni[0] #2040143154
# s = revSecuencia[0] # 5432765432

# h = int(x)*int(s)
# print(h)


# --------------------
# dniPorSecuencia = 0
# k = 0
# for i in sDni:
#     dniInt = i
#     # print(dniInt)
#     # int(dniInt)
#     # print(type(dniInt))
#     secInt = revSecuencia[k]
#     # print(secInt)
#     # int(secInt)
#     # print(type(secInt))
#     dniPorSecuencia += int(dniInt) * int(secInt)
#     dniInt * 0
#     # str(dniInt)
#     secInt * 0
#     # str(secInt)
#     k += 1
#     print(dniPorSecuencia)

# print(dniPorSecuencia)


# -------------------
# for i in sDni:
#     g = i # sDni = "2040143154"
#     print(g)

# --------------------
# --------------------

# Transcrita

dni1=input("Ingresa el DNI carajo:")

sexo=input("Ingrese M para hombre, F para mujer, E para empresa:")

def calCuil(d,s):
    dni = d
    secuencia = "2345672345"

    revSecuencia = ""
    for k in secuencia[::-1]:
        revSecuencia+= k

    # strDni = str(d) #Ahora el dni es un string

    numSexo = 0
    sS = ""
    if s == "M"or "m":
        numSexo = 20
        sS = str(numSexo)
    if s == "F"or"f":
        numSexo = 27
        sS = str(numSexo)
    if s == "E"or"e":
        numSexo = 30
        sS = str(numSexo)

    sexMasDni = sS+dni
    dniSecuenciaCalculo = 0
    k = 0

    for i in sexMasDni:
        dniInt = i
        secInt = revSecuencia[k]
        dniSecuenciaCalculo += int(dniInt) * int(secInt)
        dniInt * 0
        secInt * 0
        k += 1

    n = dniSecuenciaCalculo % 11

    j = 11-n
    print(dniSecuenciaCalculo)
    m = str(j)
    #-------------------
    #Apratir de aca se puede manejar el cuil como uno quiera
    #Puedo sacarlo con un print, puedo gurdarlo en una variable, etc.
    #-------------------
    print(sS,dni,m,sep ='-')
    cuit = sS+'-'+dni+'-'+m
    print(cuit)

calCuil(dni1,sexo)