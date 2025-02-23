#jogo da forca
import randomp;#randomizer para escolher uma palavra aleatoria de "palavras.txt"

#inicializa
def abertura():
    print("*********************************");
    print("***Bem vindo ao jogo da Forca!***");
    print("*********************************");

#pede uma letra
def pede_chute():
    chute = input("Qual letra? ");
    chute = chute.strip().upper();
    return chute;

#se acertar marca a letra pro usuário ver
def marca_chute(chute, letras_acertadas, palavra_secreta):
    index = 0;
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra;
        index += 1;

#inicializa uma palavra secreta
def carrega_palavra():
    arquivo = open("palavras.txt", "r");
    palavras = [];
    for linha in arquivo:
        linha = linha.strip();
        palavras.append(linha);
    arquivo.close();
    numero = random.randrange(0, len(palavras));
    palavra_secreta = palavras[numero].upper();
    return palavra_secreta;

#desenha a forca de acordo com os erros
def desenha_forca(erros):
    print("  _______     ");
    print(" |/      |    ");
    if(erros == 1):
        print (" |      (_)   ");
        print (" |            ");
        print (" |            ");
        print (" |            ");
    if(erros == 2):
        print (" |      (_)   ");
        print (" |      \     ");
        print (" |            ");
        print (" |            ");
    if(erros == 3):
        print (" |      (_)   ");
        print (" |      \|    ");
        print (" |            ");
        print (" |            ");
    if(erros == 4):
        print (" |      (_)   ");
        print (" |      \|/   ");
        print (" |            ");
        print (" |            ");
    if(erros == 5):
        print (" |      (_)   ");
        print (" |      \|/   ");
        print (" |       |    ");
        print (" |            ");
    if(erros == 6):
        print (" |      (_)   ");
        print (" |      \|/   ");
        print (" |       |    ");
        print (" |      /     ");
    if (erros == 7):
        print (" |      (_)   ");
        print (" |      \|/   ");
        print (" |       |    ");
        print (" |      / \   ");
    print(" |            ");
    print("_|___         ");
    print();

#mensagem de vencedor
def vencedor():
    print("Parabéns, você ganhou!");
    print("       ___________      ");
    print("      '._==_==_=_.'     ");
    print("      .-\\:      /-.    ");
    print("     | (|:.     |) |    ");
    print("      '-|:.     |-'     ");
    print("        \\::.    /      ");
    print("         '::. .'        ");
    print("           ) (          ");
    print("         _.' '._        ");
    print("        '-------'       ");

#mensagem de perdedor
def perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!");
    print("A palavra era {}".format(palavra_secreta));
    print("    _______________         ");
    print("   /               \        ");
    print("  /                 \       ");
    print("//                   \/\    ");
    print("\|   XXXX     XXXX   | /    ");
    print(" |   XXXX     XXXX   |/     ");
    print(" |   XXX       XXX   |      ");
    print(" |                   |      ");
    print(" \__      XXX      __/      ");
    print("   |\     XXX     /|        ");
    print("   | |           | |        ");
    print("   | I I I I I I I |        ");
    print("   |  I I I I I I  |        ");
    print("   \_             _/        ");
    print("     \_         _/          ");
    print("       \_______/            ");

abertura()
palavra_secreta = carrega_palavra();
letras_acertadas = ["_" for letra in palavra_secreta];#coloca um "_" a cada letra da palavra secreta
print(letras_acertadas);
enforcou = False;
acertou = False;
erros = 0;
while(not enforcou and not acertou):
    chute = pede_chute();
    if(chute in palavra_secreta):
        marca_chute(chute, letras_acertadas, palavra_secreta);
    else:
        erros += 1;
        desenha_forca(erros);
    enforcou = erros == 7;
    acertou = "_" not in letras_acertadas;
    print(letras_acertadas);
if(acertou):
    vencedor();
else:
    perdedor(palavra_secreta);


________________________
maior=0
def obternaior(n1,n2,n3):
    maior=0
    if(n1>n2)and(n1>n3):
        maior+n1
    elif(n2>n1)and(n2>n3):
        maior=n2
    else:
        maior=n3
    return  maior

n1=int(input("n1:"))
n2=int(input("n2:"))
n3=int(input("n3:"))
maior=obternaior(n1,n2,n3)
print(maior)







