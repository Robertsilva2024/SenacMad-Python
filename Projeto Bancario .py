# menu de opções
print('Bem vindo!')
print('Ao Aplicativo:')
print('|_itau_|','\n')
print('Formas acesso Disponiveis No itaú são:')
print('opção 1 - Depositos')
print('opção 2 - saques')
print('opção 3 - Pix')
print('Escolha uma dessas opções!!','\n')

op1 = int(input('digite a opção desejada'))
O = 'Depositos'
s = 'Saques'
p = 'Pix'
if(O != s != p ):
    print('vc escolheu a opção 1: Deposito','\n')
elif(s != O != p):
    print('voce escolheu a opção 2: Saque')
else:
    print('vcoce escolheu a opção 3: Pix')

opcao1 = float(input('digite o valor que será depositado:'))
opcao2 = float(input('digite o valor a ser sacado:'))
opcao3 = float(input('digite o valor do pix para sua conta'))
saque =  opcao2 - 2000
deposito = opcao1 + 2000
pix = opcao3 + 2000
saldoanterior = 2000
saldoatual = 2000 - opcao2

# condições a serem feitas
if (opcao1 > 0):
    print('Foi depositado com sucesso obrigado!!','\n')
elif(opcao1==0):
    print('Deposito invalido!!','\n')
elif(saque<=2000):
    print('Saque Retirado com sucesso!','\n')
elif(saque==0):
    print('Saque invalido!!','\n')
elif(opcao3 > 0):
    print('Pix Realizado com sucesso na sua conta','\n')
else:
    print('não realizado Digite novamente!!','\n')

# mostra o novo deposito,saque e pix com o valor digitado
print('O saque De R$',opcao2,'Reais - os',saldoanterior,'Mil Deu menos de:',saque,'reias','\n')
print('já o Deposito de R$',opcao1,'Reias + os',saldoanterior,'mil:aumentou para R$:',deposito,'\n')
print('E pix de R$',opcao3,'+ os',saldoanterior,'mil:aumentou para R$',pix,'\n')
print('Saldo anterior foi de R$:',saldoanterior,'mil','\n')
print('Saldo atual é de R$:',saldoatual,'mil','\n')

# extrato
comprodeposito = opcao1
comprosaque = opcao2
compropix = opcao3

# amostra recente geral
print('Deposito Feito R$',comprodeposito)
print('Saque Feito atualmente foi de R$',comprosaque,'Reais')
print('E o Comprovante do Pix e de R$',compropix,'Reais')



