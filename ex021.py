n = 1
for n in range(1,3):
    a = int(input('A:'))
    b = int(input('B:'))
    c = int(input('C:'))

if (a < b + c) and (b < a + c) and (c < b + c):
    print('Triangulo')
if (a == b) and (b == c):
    print("Equilatero")
elif (a == b) or (b == c) or (a == c):
    print('do tipo:Isósceles')
elif (a != b) and (b != c) and (a != c):
    print('do tipo:Escaleno')
else:
    print('Não é um triangulo')
n=n+1
