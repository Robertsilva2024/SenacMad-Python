#numero primo # for é pra parar a variavel
inicio = 0
fim = 100
for i in range(inicio,fim + 1):
    if i > 1:
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            print(i)


