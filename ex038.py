n1 = float(input("Valor 1: "))  # + - / *
n2 = float(input("Valor 2: "))

operacao = input("Digite a operação(+,-,/,*): ")

match operacao:
    case "+":
        print(f"{n1} + {n2} = {n1 + n2}")
    case '-':
        print(f"{n1} - {n2} = {n1 - n2}")
    case '/':
        print(f"{n1} / {n2} = {n1 / n2}")
    case '*':
        print(f"{n1} * {n2} = {n1 * n2}")
    case _:
        print("Operação não reconhecida")
