md= 0
sit = 0
def calcularmedia (n1,n2,n3,n4):
    md = (n1+n2+n3+n4)/4
    if(md >=7):
        sit= 'aprovado'
    elif(md<5):
        sit = 'reprovado'
    else:
        sit = 'recuperação'
    return md,sit
n1 = float(input('N1:'))
n2 =float(input('N2:'))
n3 = float(input('N3:'))
n4 = float(input('N4:'))
md = calcularmedia(n1,n2, n3, n4)
print(md)
print(sit)
