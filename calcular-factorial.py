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

mensaje=  input("igrese un numero: ")
numero_factorial=  int(mensaje)

iterador = 1
factorial_del_numero = 1

while iterador < numero_factorial:
    factorial_del_numero = factorial_del_numero * numero_factorial
    numero_factorial -= iterador

print(factorial_del_numero)