#verificação de número par ou ímpar:ex1
Numero = int(input("Digite um número:"))
if Numero %2 ==0 and Numero != 0:
     print(" O número é par.")
elif  Numero %2 ==1 and Numero != 0: 
     print (" O número é ímpar.")
else: 
    print("O número é zero.") 
#if significa: SE    else significa: SENÃO    elif significa: SENÃO SE

#Maior entre dois números:ex2 
#solicite dois números 
Numero1 = input("Digite o primeiro número:") 
Numero2 = input("Digite o segundo número:")   
#determine qual deles e maior 
if Numero1 > Numero2:
    print(" o número1 é o maior")
elif Numero2 > Numero1: 
    print("o número2 é o maior")
else: 
   print("Os números são iguais")
#mostre o resultado

#verificação de idade para dirigir: ex3
Idade = int(input("Digite sua idade:"))
if Idade >= 18:
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")

#número positivo, negativo ou zero:ex4
Numero = int(input("Digite um número:"))
if Numero > 0:
    print("O número é positivo.")
elif Numero < 0:
    print(" O número é negativo.")
else: 
    print("O número é zero.")

#Classificação de Triângulos: ex5
A = float(input("Digite o primeiro lado do triangulo"))
B = float(input("Digite o segundo lado do triangulo"))
C = float(input("Digite o terceiro lado do triangulo"))
if A == B == C :
  print("O triangulo e equilátero")
elif  A == B or A == C or B == C: 
  print("O triangulo é isósceles")
else: 
  print("O triangulo é escaleno")

#Aprovação em disciplinas: ex6 
nota = float(input("Digite a nota do aluno:"))
if nota >= 7:
   print("Aprovado")
elif nota >= 5:
   print("Recuperação")
else: nota <= 5
print("Reprovado")

#verificação de número divisível por 3 e 5 : ex7
Numero = int(input("Digite um número:"))
if Numero % 3 == 0 or Numero % 5 == 0:
    print("O número é divisível por 3 e 5.")
elif Numero % 3 == 0:
    print("O numero é divisível por 3.")
else: 
    print("O número é divisível por 5.")

#Verificação de vogal ou consoante: ex8 
Letra = input("Digite uma letra:")
if Letra in "aeiou":
    print("A letra é uma vogal")
else: 
    print("A letra é uma consoante")
 

#Cálculo com desconto com condição:ex9 
valor = float(input("Digite o valor do produto:"))
desconto = float(input("Digore o valor do desconto:"))
if desconto >= 0 and desconto <= 100:
 valor_final = valor - (valor*desconto/100)
 print("O valor final do produto é:", valor_final)
else: 
    print("Desconto inválido. O desconto deve ser entre 0 e 100%.")

#Classificação de idade :ex10
idade = int(input("Digite a sua idade:"))
if idade < 12:
    print("Criança")
elif idade < 18:
    print(" Adolescente")
elif idade < 60:
    print("Adulto")
elif idade >= 60:
    print("Idoso")




