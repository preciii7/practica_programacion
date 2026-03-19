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

