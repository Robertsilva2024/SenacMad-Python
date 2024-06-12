cont = 1
somasal = 0
mdsal = 0
salmaior = 0
salariomenor = 100000
nomemaior =''
nomemenor = ''# soma dos salarios maior e menor
while cont<=6:
    nome = input('nome')
    salario = float(input('salario'))
    somasal = somasal+salario
    if (salario>salmaior):
        nomemaior=nome
        salmaior=salario
    if (salario<salariomenor):
        nomemenor=nome
        salariomenor=salario
    cont = cont+1
mdsal = somasal/6
print('nome maior salario:',nomemaior)
print('maior salario:',salmaior)
print('nome menor salario:',nomemenor)
print('menor salario:',salariomenor)
print('media salario:',mdsal)

