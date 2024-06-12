idade = int(input('qual é a sua idade'))

print('Classificação etéria:')

if(idade >= 0 and idade <= 11):
    print("criança")
elif(idade >=12 and idade <=18):
    print('Adolescente')
elif(idade >= 19 and idade<=24):
    print("jovem")
elif(idade >= 25 and idade<= 40):
    print('Adulto')
elif(idade >=41 and idade <=60) :
    print('Meia idade')
elif(idade > 60):
  print('idoso')




