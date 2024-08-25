# import math

# de_numero_a_factorizar= input("ingrese un numero entero: ")

# factorial_del_numero = math.factorial(int(de_numero_a_factorizar))

# print(factorial_del_numero)

#------------
# numero_iterable = str(numero)

# cantidad_de_repeticiones= numero

# numero_factorial= 0
# for i in numero_iterable:
#     var_temporal = cantidad_de_repeticiones*(cantidad_de_repeticiones-1)

#     numero_factorial = var_temporal

# print(numero_factorial)

# numerin = 5
# n = 1
# while n < numerin:
#     n = n * (n+1)
#     n += 1

# print(n)

# -----------
# numero1= 5
# nss= 0
# print(nss)
# while numero1:
#     if nss > numero1:
#         print(nss)
#         nss += nss * (nss *1)
#         print(nss)
#         n

# print(nss)

# # -----------
# num=1
# n=5

# # num = num * (n)
# # num = num * (n-1)
# # num = num * (n-2)
# # num = num * (n-3)
# # num = num * (n-4)


# i = 1

# while i < n:
#     # i=0
#     num = num * (n)
#     n -= i
#     # i += 1

# num = input("igrese un numero")
# print(num)

# -------------------------
# Pasado a limpio

# mensaje=  input("igrese un numero: ")
# numero_factorial=  int(mensaje)

# iterador = 1
# factorial_del_numero = 1

# while iterador < numero_factorial:
#     factorial_del_numero = factorial_del_numero * numero_factorial
#     numero_factorial -= iterador

# print(factorial_del_numero)

# y = 0
# factorial_del_numero = 1
# def calcular_factorial(x):


    # seguimos = True
    # letra_de_confirmacion = str(x)
    
    # if letra_de_confirmacion == "S" or "s":
    #     seguimos = True
    # else:
    #     seguimos = False
        
    # mensaje = x #input("igrese un numero: ")

    # if type(numero_factorial) == 'str' :
    #     print("Nos re vimos amigo")
    #     return
    # else:
    # iterador = 1
    # numero_factorial =  int(x)
    
    # while iterador < numero_factorial:
    # factorial_del_numero = factorial_del_numero * numero_factorial
    # numero_factorial -= iterador


    
    #CONDICION PARA QUE SALGA DE LA FUNCION
    # if numero_factorial == 1:
        # return
    
    # calcular_factorial(numero_factorial)
    
    # y += 1
    # if y == numero_factorial:
    #     return
    

# calcular_factorial(input("igrese un numero: "))
# print(factorial_del_numero)


#POR SESOLVER
# ---------------------------
# cualquier_numero = 5
# x = 1
# def factorial(numero,x1):
#     a = numero
#     if numero > 1:
#         x1 = numero * x1 
#         factorial(a - 1, x1)
#     else:
#         return print(x1)
#         # print(x1)

# factorial(cualquier_numero, x)



# ---------------------------
#PASADO A LIMPIO
numero = 5 #Vamos a calcular 5! (por ejemplo)
multiplicador = 1 #Con esta variable vamos a multipicar por el 'numero'

def factorial(x, y):
    mult = x #Aqui guardaremos 5! -> 4! -> 3!
    if x > 1: # y entrara en este bucle hasta que sea 1!
        y = x * y # en el primer bucle seria >> 5 = 5! * 1 >> 20 = 4! * 5 >> 60 = 3! * 20...
        factorial(mult - 1, y) #Aqui la vuelvo a llamar con 'y' siendo el resultado de las multiplicaciones
        # & mult se va a ir reduciendo en -1
    else:
        return print(y)

factorial(numero, multiplicador)