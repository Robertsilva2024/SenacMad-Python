tm=0  #execicio de altura,pesomaior,menor,sexo
tf=0
n=1
tpeso=0
taltura=0
tpesom=0
tpesof=0
talturam=0
talturaf=0
malto=0
nomemalto=''
nomempesado=''
mpesado=0
mdpeso=0
mdaltura=0
mdalturaf=0
mdalturam=0
mdpesom=0
while n <= 5:
    nome = input('Nome:')
    sexo = input('Sexo:')
    altura = float(input("Altura:"))
    peso = float(input("Peso:"))
    tpeso=tpeso+peso
    taltura=taltura+altura
    if sexo == "F":
        tf=tf+1
        talturaf=talturaf+altura
        tpesof=tpesof+peso
    if sexo=="M":
        tm=tm+1
        talturam=talturam+altura
        tpesom=tpesom+peso
    if altura>malto:
        malto=altura
        nomemalto=nome
    if peso>mpesado:
        mpesado=peso
        nomempesado=nome
    n = n + 1
mdpeso= tpeso/5
mdaltura = taltura/5
mdalturaf=talturaf/tf
mdalturam=talturam/tm
mdpesof=tpesof/tf
mdpesom=tpesom/tm
print('Md peso:',mdpeso )
print('Md altura:',mdaltura )
print('Md altura Feminina:',mdalturaf )
print('Md altura Masculina:',mdalturam )
print('Md peso Feminina:',mdpesof )
print('Md peso Masculina:',mdpesom )
print('Total masculino:',tm)
print('Total feminino:',tf)
print('Mais alto:', nomemalto)
print('Altura mais alto:', malto)
print('Mais pesado:', nomempesado)
print('Peso mais pesado:', mpesado)



