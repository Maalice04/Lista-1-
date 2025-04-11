#contagem crescente :ex1
numero = 1
while numero <= 10:
    print(numero)
    numero += 1
#(range= faixa)

#contagem regressiva: ex2 

while numero >= 0: 
    print(numero)
    numero -= 1


#peça 5 numeros e mostre a soma deles: ex3
#somar os números 
soma = 0 
while soma < 5:
    numero = int(input("Digite um número:"))
    soma += numero
#resultado
print("A soma dos números é:",soma)

#tabuada 
numero = int(input("Digite um número para ver a tabuada:"))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#numeros pares entre intervalo
numero1 = input("Digite o primeiro número:")
numero2 = input("Digite o segundo número:")
while numero1 <= numero2:
    if numero1 % 2 == 0: 
        print(numero1)
    numero1 += 1
    
#Adivinhar numeros
numero_secreto = 6
palpite = 3
while palpite != numero_secreto:
   palpite = input("Adivinhe o número secreto:")
if palpite < numero_secreto: 
    print("Muito baixo! Tente outro número maior.") 
elif palpite> numero_secreto:
    print("Muito alto! Tente outro número menor.")
else: 
    print("Parabéns! Você adivinhou o número secreto.")


#fatorial 
numero = int(input("Digite um número para calcular o fatorial:"))
fatorial = 1 
while numero > 1:
    fatorial *= numero 
    numero -= 1
    print("o fatorial é:", fatorial)

#seguencia de fibonacci 
numero = int(input("Digite o número de termos da sequência de Fibonacci:"))
a, b = 0, 1 
while numero > 0:
    print(a, end=" ")
    a, b = b, a + b 
    numero -= 1 

#numeros primos
numero = int(input("Digite um número:"))
primo = True 
while numero > 1: 
    while i < numero: 
        if numero % i == 0:
            primo = False
            break
        i += 1 
        if primo == True:
            print(numero, "é primo")
        else:
            print(numero, "não é primo")

#media de notas com condição de saida 
numero_notas = int(input("Digite o número de notas:"))
soma = 0
while numero_notas > 0:
    nota = float(input("Digite a nota:"))
    soma += nota 
    numero_notas -=1 
    media = soma / numero_notas 
    print("A média das notas é:", media)
