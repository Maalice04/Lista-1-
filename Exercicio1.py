#Conversao em Temperatura: Ex3
temperatura = float(input("Digite a temperatura em Celsius:"))
resultado = temperatura * 9/5 + 32 
print("A temperatura em Fahrenheit é:",resultado)

#cálculo de área de um retângulo: ex4
Largura = float(input("Digite a largura do retângulo:"))
Altura = float(input("DIgite a altura do retângulo:"))
Area = Largura + Altura
resultado = Area *2
print("A área do retângulo é:", resultado)

#Cáculo de IMC: ex5
peso = float(input("Digite seu peso em kg:"))
Altura = float(input("Digite sua altura em metros:"))
imc = peso / (Altura* Altura)
print(" seu IMC é:",imc)

#cálculo de Desconto: ex6
preço = float(input("Digite o preço do produto:"))
desconto = float(input("Dugite o desconto:"))
resultado = preço-desconto
print("o preco com o desconto é:", resultado)
