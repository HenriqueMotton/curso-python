

# def eh_primo(numero: int) -> bool:
#     if numero < 2:
#         return False
#     for i in range(2, int(numero ** 0.5) + 1):
#         if numero % i == 0:
#             return False
#     return True

# def main():
#     try:
#         numero = int(input("Digite um número inteiro para verificar se é primo: "))
#         if eh_primo(numero):
#             print(f"{numero} é um número primo.")
#         else:
#             print(f"{numero} não é um número primo.")
#     except ValueError:
#         print("Por favor, digite um número inteiro válido.")

def primeira():
    numero1 = 5
    numero2 = 10
    nome = str(input("Qual o seu nome?\n"))

    print(f"Olá {nome}: 10 + 5 = ", numero1 + numero2)

def variaveis():
    nome: str = "Park"
    numeroStr: str = "5"
    idade: int = 26
    altura: float = 1.60
    tem_carteira: bool = True

    # print("Tipo: ", type(nome))
    print("Valor: ", int(numeroStr) + int(numeroStr))

def main():
    # primeira()
    variaveis()

if __name__ == "__main__":
    main()
