salario = float(input('quanto vc ganha hj?'))

if (salario > 2500):
    aumento = 0.05
    print('O aumento foi de 5%')
elif(salario <= 2500):
    aumento = 0.07
    print('Desconto de 7%')


aumento = (aumento * salario)
novosalario = salario + aumento
print('Salario anterior',salario)
print("Seu novo salario de:",novosalario)
print('o aumento foi de:',aumento)

