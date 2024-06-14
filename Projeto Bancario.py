# menu de opções
print('Bem vindo!,Ao')
print('{:=^31}'.format('|_Aplicativo_|'))
print("""|------------|          
         |   BANCO    |  
         |  I T A Ú   |       
         | ^^^^^^^^^^ |            
         |------------|           """)
print('Formas acesso Disponiveis No itaú são:')
print('opção 1 - Deposito')
print('opção 2 - saque')
print('opção 3 - Pix')
print('opção 4 - Recarga')
print('Temos Recarga da: Tim,Vivo,Claro')
print('Escolha uma dessas opções Por favor!!','\n')
opcaobanco = 'itau'
op = int(input('digite a opção desejada'))
op2 = 1
op3 = 2
op4 = 3
op5 = 5

if(op==op2):
    print('vc escolheu a opção 1:Deposito','\n')
elif(op==op3):
    print('voce escolheu a opção 2:Saque','\n')
elif (op == op4):
    print('voce escolheu a opção 3:Pix','\n')
elif(op == op5):
    print('vc escolheu Recarga')
    print('qual operadora Tim,vivo ou claro')
elif(op != op5):
    print('invalido')

opcao1 = float(input('digite o valor que será depositado:'))
opcao2 = float(input('digite o valor a ser sacado:'))
opcao3 = float(input('digite o valor do pix para sua conta'))
opcao4 = str(input('digite a operadora Escolhida:'))
opcao5 = float(input('digite a recarga a ser enviada de R$:'))
print('Recarga Realiza com Sucesso!!')

deposito = opcao1 + opcao2
saque = opcao2 - 2000
pix = opcao1 + opcao3
recarga = opcao4
saldoanterior = 2000
saldoatual = opcao1 + opcao3
saldosobrado = opcao1 + opcao3 - opcao2 - opcao5

# condições a serem feitas
if (opcao1 > 0):
    print('depositado Realizado com sucesso obrigado!!','\n')
elif(opcao1 == 0):
    print('Deposito invalido!!','\n')
elif(saque<=2000):
    print('Saque Retirado com sucesso!','\n')
elif(saque==0):
    print('Saque invalido!!','\n')
elif(opcao3 > 0):
    print('Pix Realizado com sucesso na sua conta','\n')
else:
    print('não Realizado Digite novamente!!','\n')

# mostra o novo deposito,saque e pix com o valor digitado
print('O Deposito foi de R$',opcao1,'Reias e aumentou para R$:',deposito)
print('E O saque foi de R$',opcao2,'Reais e Diminuil para R$',saque)
print('já o pix foi de R$',opcao3,'Reais e aumentou para R$',pix,)
print('A Recarga Feita atualmente foi de',opcao5,'Reais')
print('A opção escolhida de Recarga foi A:',recarga,'\n')
print('Saldo anterior foi de R$:',saldoanterior,'mil Reias')
print('O Saldo atual é de R$',saldoatual)
print('E o Resto que Sobrou foi de R$:',saldosobrado,'Reias','\n')

# extrato
comprodeposito = opcao1
comprosaque = opcao2
compropix = opcao3
comprorecarga = opcao5

# amostra recente geral
print('Deposito atual foi de R$',comprodeposito,'Reias')
print('O Saque Feito atualmente foi de R$',comprosaque,'Reais')
print('O Comprovante do Pix foi de R$',compropix,'Reais')
print('E Por ultimo a Recarga que foi de',opcao5,'Reais','na',recarga)

# Grafico matplotib em Barras
import matplotlib.pyplot as plt
opcoesconta = ['Deposito','Saque','Pix','Recarga']
valores = [opcao1,opcao2,opcao3,opcao5]

plt.bar(opcoesconta,valores)
plt.title('Grafico de Barras Financeiro')
plt.xlabel('Formas de Uso Mais Recentes até agora:')
plt.ylabel('Valores'.upper())
plt.show()

