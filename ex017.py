a = int(input('A:'))
b = int(input('B:'))
c = int(input('C:'))

if (a<b+c) and (a>b-c):
    print('É um triângulo!')
if (a==b) and (b==c):
    print('do tipo:equilatero')
elif (a==b) or (b==c) or (a==c):
    print('do tipo:Isósceles')
elif (a!=b) and (b!=c) and (a!=c):
    print('do tipo:Escaleno')
else :
    print('Não é um triangulo')

