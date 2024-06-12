 # função que mostra o maior nuemro entre os 3
maior = 0
def obtermaior (n1,n2,n3):
    if(n1>n2):
        maior = n1
    if(n1<n2):
        maior = n2
    else:
         maior = n3
    return maior

n1 = int(input('N1:'))
n2 = int(input('N2:'))
n3 = int(input('N3:'))
maior = obtermaior(n1,n2,n3)
print(maior)