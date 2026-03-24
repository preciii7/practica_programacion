"""
Nivel 1
"""
print("#################################################")
print("#1 Imprime los números del 1 al 10 usando for.")
print("#################################################")
for i in range(1,11):
    print(i)

print("#################################################")
print("#2 Imprime los números del 10 al 1 usando while.")
print("#################################################")
c=10
while c>0:
    print(c)
    c-=1
print("#################################################")
print("#3 Imprime solo los números pares del 1 al 20.")
print("#################################################")
for i in range(1,11):
    print(i*2)
print("#################################################")
print("#4 Imprime solo los números impares del 1 al 20.")
print("#################################################")
for i in range(0,10):
    print((i*2)+1)

print("#################################################")
print("#5 Calcula la suma de los números del 1 al 100.")
print("#################################################")
c=0
for i in range(0,101):
    c+=i
print(c)

print("#################################################")
print("Pide un número al usuario e imprime su tabla de multiplicar del 1 al 10.")
print("#################################################")
c = int(input("Ingresa numero: "))
for i in range(1,11):
    print(c*i)
print("#################################################")
print("Cuenta cuántas letras tiene una palabra usando un loop.")
print("#################################################")
c = input("Ingresa palabra: ")
for i in range(1,len(c)+1):
    print(i)
print("#################################################")
print("Recorre una lista de strings e imprime cada nombre en una línea.")
print("#################################################")
ls = ["A", "B", "C"]
for i in ls:
    print(i)
"""
Nivel 2
"""
print("#################################################")
print("Imprime los números del 1 al 30, pero: SI el número es múltiplo de 3, imprime Fizz SI es múltiplo de 5, imprime Buzz SI es múltiplo de ambos, imprime FizzBuzz")
print("#################################################")

for i in range(1,31):
    if i%3 == 0 and i%5==0:
        print("FizzBuzz")
    elif i %3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
print("##########################################################")
print("Recorre una lista de números y cuenta cuántos son positivos.")
print("########################################################### ")
ls = [1,-1,2,-4]
c=0
for i in ls:
    if i>0:
        c+=1
print(c)

print("##########################################################")
print("Recorre una lista de números y encuentra el mayor")
print("########################################################### ")
ls = [1,-1,2,-4]
c=min(ls)
for i in ls:
    if i>c:
        c=i
print(c)

print("##########################################################")
print("Recorre una lista de números y encuentra el menor")
print("########################################################### ")
c = 0
for i in ls:
    if i < c:
        c=i
print(c)

print("##########################################################")
print("Dada una palabra, cuenta cuántas vocales tiene")
print("########################################################### ")

insertar = "murcielago"
c = 0
for i in insertar:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        c+=1
print(c)

"""
Nivel 3
"""
print("########################################################### ")
print("Dada una lista de números, calcula la suma total sin usar sum().")
print("########################################################### ")

ls = [1,2,3]
c=0
for i in ls:
    c+=i
print(c)

print("########################################################### ")
print("#Cuenta cuántas veces aparece un número específico en una lista.")
print("########################################################### ")
ls = [1,2,1,2,1,3,2,3,3,2,1,1]
k = {}
for i in set(ls):
  c = 0
  for j in range(len(ls)):
    if i == ls[j]:
      c+=1
  k[i]=c

print(k)     

print("########################################################### ")
print("#Dada una lista de palabras, imprime solo las palabras con más de 5 letras.")
print("########################################################### ") 
ls = ["hola", "soy", "eres", "estar", "estrella"]
for i in ls:
    if len(i) >5:
        print(i)

#otra manera de hacerlo
c=0
ls1=[]
for i in range(len(ls)):
    c=0
    for j in ls[i]:
        c+=1
    if c>5:
        print(i)

         
