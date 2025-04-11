
#cáculadora de juros simples:ex7
principal = float(input("Digite o valor principal:"))
Taxa = float(input("Di(gite a taxa de juros:"))
Anos = float(input("Digite o número de anos:"))
Montante =principal + (principal* Taxa* Anos/100)
print("o montante é:",Montante)
 
 #Conversão de idade : ex8
idade= input("Digite a sua idade:")
meses = int(idade) * 12
dias = int(idade) * 365
print("A sua idade em meses é:",meses + dias)

#troca de valores : ex9
valor1 = float(input("Digite o primeiro valor:"))
valor2 = float(input("Digite o segundo valor:"))
valor3 = valor1
valor1 = valor2
valor2 = valor3
print("O primeiro valor é:", valor1)
print("O segundo valor é:", valor2)

#calculadora de média ponderada: ex10 
Nota1 = int(input("Digite a primeira nota:"))
Nota2 = int(input("Digite a segunda nota:"))
Nota3 = int(input("Digite a terceira nota:"))

Peso1 = int(input("Digite o peso da primeira nota:"))
Peso2 = int(input("Digite o peso da segunda nota:"))
Peso3 = int(input("Digite o peso da terceira nota:"))

notaPeso =(Nota1*Peso1)+(Nota2*Peso2)+ (Nota3*Peso3)
mediaPonderada = notaPeso/ (Peso1+Peso2+Peso3)
print("A média ponderada é:", mediaPonderada)

