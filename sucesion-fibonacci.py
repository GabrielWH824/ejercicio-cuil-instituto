# def suces_fibonacci(limite):
#     # limite = num2 #Voy a guardar el militador por ejempo 16
#     if  <= limite: 
#         return 1
#     else:
#         return 0 + suces_fibonacci(55)

# suces_fibonacci(55)


def suce_fibonacci(limite):
	if limite == 0: #caso base 1
		# print(limite)
		return 0
	elif limite == 1: #caso base 2
		# print(limite)
		return 1
	else:
		# print(limite)
		return suce_fibonacci(limite - 1) + suce_fibonacci(limite - 2)
	
# print (suce_fibonacci(8))

# for 0 a 7
for i in range(8 + 1):
	print(suce_fibonacci(i))




# def factorial(numero):
# 	if numero == 0:
# 		return 1
# 	else:
# 		return numero * factorial(numero -1)
	
# print(factorial(5))