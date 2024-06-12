soma = 0
sub = 0
mult = 0
def calcularsoma(n1,n2):
    soma=n1+n2
    return soma
def calcularsub (n1,n2):
    sub = n1-n2
    return sub
def calcularmult (n1,n2):
    mult= n1*n2
    return mult
n1 = int(input('N1:'))
n2 = int(input('N2:'))
soma=calcularsoma(n1,n2)
sub= calcularsub(n1,n2)
mult= calcularmult(n1,n2)
print(soma,sub,mult)