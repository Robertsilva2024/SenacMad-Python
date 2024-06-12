soma=0 # ele pega o numero 0 e soma com o numeros digtado pelo usurio
x = [1,2,3,4,5,6,7,8,9,10] # aqui diz que é de 1 até 10
for x in x:
    num = int(input('numero'))
    soma = soma + num
    x=x+1
    print('soma',soma)




