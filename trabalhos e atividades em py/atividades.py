#Exercício 1 - código para de área de um retângulo
base = int(input("Digite o valor da base: "))

alt = int(input("Digite o valor da alt: "))

área = base * alt

print(f"O valor da base é: {área}cm²")
#usar tanto o int quanto o float, mas nunca esquecer!

# Exercício 2 - código para calculo de soma entre 2 valores
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

soma = num1 + num2

print(f"O resultado da soma será: {soma}")

# Exercício 3 - conversão de Ceslsius para Fahrenheit
C = int(input("Digite a temperatura em Celsius: "))

Fahrenheit = (C * 9/5) + 32

print(f"{C} °C é igual a {Fahrenheit}°F")

#Exercício 4 - conversão de Real para Dólar
real = float(input("Receba o valor em reais: "))

dolar = 5.05

cambio = real/dolar

print(f"{real} é equivalente a {cambio}")

#Excercício 5 - calculo de media de nota
Nota1 = float(input("Digite o valor da primeira nota: "))
Nota2 = float(input("Digite o valor da segunda nota: "))
Nota3 = float(input("Digite o valor da terceira nota: "))

Media = (Nota1 + Nota2 + Nota3) /3

print(f"A média das notas é: {Media}")

#Exercício 6 - tabuada de um numero até o 10
Num = int(input("Coloque um número e veja a tabuada dele até o 10: "))

print(f"{Num} x 1 = {Num*1}")
print(f"{Num} x 2 = {Num*2}")
print(f"{Num} x 3 = {Num*3}")
print(f"{Num} x 4 = {Num*4}")
print(f"{Num} x 5 = {Num*5}")
print(f"{Num} x 6 = {Num*6}")
print(f"{Num} x 7 = {Num*7}")
print(f"{Num} x 8 = {Num*8}")
print(f"{Num} x 9 = {Num*9}")
print(f"{Num} x 10 = {Num*10}")

#Exercício 7 - Estrutura condicional de X e Y
x = int(input("Digite o valor de x:"))
y = int(input("Digite o valor de y"))

if x > y:
  print("x é maior do que y")
elif x < y:
  print("y é maior do que y")
else:
  print("x é igual a y")

#Execício 8 - Estrutura de repetição
numero = 1

print(numero)
numero = numero + 1
print(numero)
numero = numero + 1
print(numero)
numero = numero + 1
print(numero)
numero = numero + 1
print(numero)
numero = numero + 1
print(numero)
numero = numero + 1
print(numero)
numero = numero + 1

numero = 1

for numero in range(1, 21):
    print(numero)
    numero = numero + 1

#um = atribuição dois == comparação

#Exercício 9 
num1 = int(input("Digite o primeiro número inteiro:"))

if -1 > num1:
    print("O número digitado é negativo")
elif num1 > 0:
    print("O numero digitado é positivo")
else:
    print("O numero digitado é neutro")

#Exercícios 10 - menor de idade, terceira idade, maior de idade
age = int(input("Qual sua idade?:"))

if age > 18 and age < 60:
    print("Voce é maior de idade")

elif age < 18:
    print("Voce é menor de idade")

else:
    print("Voce é terceira idade")

#Exerrecício 11 - par ou impar
num = int(input("Coloque um numero: "))
if num % 2 == 0:
  print("O numero é par")
else:
  print("O numero é impar")

#Exercício 12 
  idade = int(input("Digite sua idade: "))
if idade > 10 and idade < 12:
  print("Sub 11")
elif idade > 13 and idade < 15:
  print("Sub 13")
elif idade > 15 and idade < 17:
  print("Sub 15")
elif idade > 17 and idade < 19:
  print("Sub 18")

#Exercicio 13
nome = input("Qual seu nome?")

idade = int(input("Digite sua idade: "))
if idade > 10 and idade < 13:
  print(f"Jogador: {nome} - Sub 11")
elif idade > 12 and idade < 15:
  print(f"Jogador: {nome} - Sub 13")
elif idade > 14 and idade < 17:
  print(f"Jogador: {nome} - Sub 15")
elif idade > 16 and idade < 19:
  print(f"Jogador: {nome} - Sub 17")

#Exercicio 14
x = 5
y = 10

if not (x > 0 and y < 5):
  print("A condição é verdadeira.")
else:
  print("A condição é falsa.")

#Exercício 15
nome = input("Digite o nome do aluno: ")

Nota1 = float(input("Digite o valor da primeira nota: "))
while Nota1 < 0 and Nota1 > 100:
    print("Nota inválida")

Nota2 = float(input("Digite o valor da segunda nota: "))
while Nota2 < 0 and Nota2 > 100:
  print("Nota inválida")

Nota3 = float(input("Digite o valor da terceira nota: "))
while Nota3 < 0 and Nota3 > 100:
  print("Nota inválida")

Nota4 = float(input("Digite o valor da quarta nota: "))
while Nota4 < 0 and Nota4 > 100:
  print("Nota inválida")

Media = (Nota1 + Nota2 + Nota3 + Nota4) /4

if Media >= 60:
  print(f"O aluno {nome} ficou com media de {Media} e foi aprovado")	

else:
  print(f"O aluno {nome} ficou com media de {Media} e foi reprovado")

#Exercicio 16
nome = input("Digite o nome do aluno: ")

Nota1 = float(input("Digite o valor da primeira nota: "))
while Nota1 < 0 and Nota1 > 100:
    print("Nota inválida")

Nota2 = float(input("Digite o valor da segunda nota: "))
while Nota2 < 0 and Nota2 > 100:
  print("Nota inválida")

Nota3 = float(input("Digite o valor da terceira nota: "))
while Nota3 < 0 and Nota3 > 100:
  print("Nota inválida")

Nota4 = float(input("Digite o valor da quarta nota: "))
while Nota4 < 0 and Nota4 > 100:
  print("Nota inválida")

Media = (Nota1 + Nota2 + Nota3 + Nota4) /4

if Media >= 60:
  print(f"O aluno {nome} ficou com media de {Media} e foi aprovado")	

else:
  print(f"O aluno {nome} ficou com media de {Media} e foi reprovado")

#exercicio 17
minha_lista = [1, 2, 3, 4, 5, 6]

length = len(minha_lista) #retorna 5

print(length)

#Exercicio 18
minha_lista = [1 , 2 , 3 , 4 , 6 , 7 , 8 , 9 , 10]
#localizar elemento na lista

for lista in minha_lista:
  if lista == 5:
    print("numero encontrado")
  else:
    print("numero nao encontrado")

#exercicio 19 - rascunho da calc.
minha_lista = [1 , 2 , 3 , 4 , 6 , 7]
#localizar elemento na lista

soma = sum(minha_lista)

print(soma)

#exercicio 20
#inverter palavra 
palavra = "Senai"

print(palavra[::-1])

#exercicio 21
minha_lista= [1, 2, 3, 4, 6, 7, 8, 2020, 9, 11, 10]
#localizar elemento na lista
maior = max(minha_lista)
menor = min(minha_lista)
print(maior)
print(menor)

#exercicio 22
minha_lista = [1,2,3,4,5,6,8,10]

maior_elemento = 0

for lista in minha_lista:
  if lista > maior_elemento:
    maior_elemento = lista

print(maior_elemento)

#exercicio 23
minha_lista = [1,2,3,4,5,6,8,10,12,14,16]

contador = 0

for par in range(1,16):
    if par % 2 == 0:
      contador = contador + 1
      print(contador)

#exercicio 24
minha_lista = [1,-2,3,-4,5,-6,-8,10,-11,15,18]

contador = 0

for positivo in minha_lista:
  if positivo > 0:
    contador = contador +1
    print(contador)

#exercicio 25
minha_lista = [1,2,3,4,6,7,8,9]

minha_lista.append(5)

pares = []
for x in minha_lista:
  if x % 2 == 0:
    pares.append(x)

print(pares)

#exercicio 26
minha_lista = [-1,2,-3,-4,6,-7,8,-9]

minha_lista.append(5)

negativos = []
for x in minha_lista:
  if x < 0:
    negativos.append(x)

print(negativos)

#exercio 27 Error Hadling
try:
  nota1 = int(input("Nota 1: "))
except:
  print("Valor inserido é inváldo. Tente somente números inteiros!")

  while True:
    try:
        nota1 = int(input("Nota 1: "))
    break
  except:
    print("Valor inserido é inváldo. Tente somente números inteiros!")

   while True:
    try:
    nota1 = int(input("Nota 1: "))
    if nota1 < 0 or nota1 > 100:
      print("Insira notas entre 0 e 100")
    else:
      break
  except:
   print("Valor inserido é inváldo. Tente somente números inteiros!")

   #exercicio 28
   while True:
    try:
    Idade = int(input("Idade: "))
    if Idade < 0:
      print("Insira uma idade válida")
    else:
      print("Parabéns, sua idade é válida e positiva")
      break
  except:
   print("Idade errada inserida, apenas números inteiros!")

   #basico de função
   def saudacao(nome):
  print(f"Ola, {nome}!")

#chamando a função
  saudacao("Hugo")

#chamando a função e armazenando o resultado de uma variável

#12. Validação de E-mail: Verifique se um endereço de e-mail é válido. Dica: para isso, veja se a string possui @

email = "vitor.sousadocente.senai.br"

is_email_valid = False

for caracter in email:
  if caracter == "@":
    print("Email válido")
    is_email_valid = True
    break

if is_email_valid == False:
  print("Email inválido")

#função
def conversor_moedas(valor,taxa):
  return valor * taxa

valor_em_dolares = 100
taxa_de_cambio = 5.05

resultado = conversor_moedas (valor_em_dolares, taxa_de_cambio)

print(f"{valor_em_dolares} dolares equivalem a {resultado} reais.")

#função
def par_impar(numero):
   if numero % 2 == 0:
      return "par"
   else:
     return "impar"

resultado = par_impar(7)
print(resultado)

def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit
resultado = celsius_to_fahrenheit(30)
print(resultado)