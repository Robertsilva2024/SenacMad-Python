# menu de opções
print('Bem vindo!')
print('Ao Aplicativo:')
print('|_itau_|')
print('Formas acesso Disponiveis No itaú são:')
print('opção 1 - Depositos')
print('opção 2 - saques')
print('opção 3 - Pix')
print('Escolha uma dessas opções!!','\n')

op = int(input('digite a opção desejada'))
op2 = 1
op3 = 2
op4 = 3
if(op==op2):
    print('vc escolheu a opção 1:Deposito','\n')
elif(op==op3):
    print('voce escolheu a opção 2:Saque','\n')
elif (op == op4):
    print('voce escolheu a opção 3:Pix','\n')
elif(op != op4):
    print('invalido')


opcao1 = float(input('digite o valor que será depositado:'))
opcao2 = float(input('digite o valor a ser sacado:'))
opcao3 = float(input('digite o valor do pix para sua conta'))
saque =  opcao2 - 2000
deposito = opcao1 + opcao2
pix = opcao1 + opcao3
saldoanterior = 2000
saldoatual = opcao1 + opcao2 + opcao3


# condições a serem feitas
if (opcao1 > 0):
    print('Foi depositado com sucesso obrigado!!','\n')
elif(opcao1 == 0):
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
print('o Deposito foi de R$',opcao1,'Reias e aumentou para R$:',deposito)
print('já O saque foi de R$',opcao2,'Reais e Diminuil para R$',saque)
print('E o pix foi de R$',opcao3,'Reais e aumentou para R$',pix,'\n')
print('Saldo anterior foi de R$:',saldoanterior,'mil Reias')
print('Saldo atual é de R$:',saldoatual,'mil','Reias','\n')

# extrato
comprodeposito = opcao1
comprosaque = opcao2
compropix = opcao3

# amostra recente geral
print('Deposito atual e de R$',comprodeposito,'Reias')
print('o Saque Feito atualmente foi de R$',comprosaque,'Reais')
print('o Comprovante do Pix foi de R$',compropix,'Reais')

# Grafico matplotib em Barras
import matplotlib.pyplot as plt
opcoesconta = ['Deposito','Saque','Pix']
valores = [opcao1,opcao2,opcao3]

plt.bar(opcoesconta,valores)
plt.title('Grafico de Barras Bancario')
plt.xlabel('Formas de Uso Mais Recentes até agora:')
plt.ylabel('Valores'.upper())
plt.show()

