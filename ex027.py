n=1
somaidade=0
# ele pega uma soma e soma aproxima ex 16 idade + 15 dá 31 em diante
while n<=10:
    nome=input('nome')
    idade = int(input('idade'))
    somaidade = somaidade + idade
    n=n+1 # éssa expressão é contador e assim vai contando em diante
mediaidade= somaidade/10
print('soma',somaidade)
print('media',mediaidade)