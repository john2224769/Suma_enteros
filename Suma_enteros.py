# Programa No. 2: Programa para calcular la suma de los primeros n numeros enteros positivos 
import math

print("-----------------------------")
print("------- Suma enteros --------")
print("-----------------------------")
print(" ")

#input 
n=input("Ingrese la cantidad de numeros enteros a sumar ")
n=int (n)
print(" ")

#processing 
S=(n*(n+1))/2

#Output 
print("----------------- Resultado--------------")
print("La suma de los primeros "+str (n) + " enteros positivos es: "+str (S))
print(" ")