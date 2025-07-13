# É um looping

# O 'for' é usado para repetir uma acao varias vezes.
#   Exemplo com range():
#     for i in range(5):
#       print(i) # 0, 1, 2, 3, 4
#     Outro exemplo:
#       nomes = ["Ana", "Bia", "Carlos"]
#       for nome in nomes:
#       print("Ola,", nome)
#     O range pode ter inicio e fim:
#       for i in range(1, 6):
#       print(i) # 1 a 5

def teste():
  for i in range(5):
    print(i)

def frutas():
  frutas = ["maçã", "banana", "uva"]
  for fruta in frutas:
    print(f"Eu gosto de {fruta}")


def main():
  teste()
if __name__ == "__main__":
    main()