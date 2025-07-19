#Aula 2

# Exercício 1:
# 1 - Peça dois números ao usuário.
# 2 - Imprima se o primeiro número é maior, menor ou igual ao segundo.


def tarefa_1():
    intnumber1 = int(input("Digite o Primeiro Numero: "))
    intnumber2 = int(input("Digite o Segundo Numero: "))

    if intnumber1 > intnumber2:
        print(f"O Numero {intnumber1} é maior que {intnumber2}")
    elif intnumber1 == intnumber2:
        print(f"Ambos os números são iguais, ou seja, {intnumber2}.")
    else: 
        print(f"O Numero {intnumber2} é maior que {intnumber1}")
    
    return (intnumber1+intnumber2)

# Exercício 2:
# 1 - Pergunte a idade do usuário.
# 2 - Diga se ele é maior de idade (18 anos ou mais) ou menor de idade.

def tarefa_2():
    intIdadeUser = int(input("Quantos anos você tem ?"))

    if intIdadeUser >= 18:
        print(f"Você tem {intIdadeUser}, portanto, é maior de idade")
        return "Acesso Liberado"
    else: 
        print(f"Você é menor de idade, espere mais {18 - intIdadeUser} anos")
 
        return "Acesso Negado"
    

# Exercício 3:

# 1 - Peça um número ao usuário.
# 2 - Diga se ele é positivo, negativo ou zero.

def tarefa_3():
    fltNumberUser = float(input("Joga um número ai, pode ser quebrado também !!"))
    if fltNumberUser == 0:
        print("Sério, um Zero ?")
    elif fltNumberUser < 0:
        print("Número Negativo, espero que não seja o XP")
    else:
        print("Número Positivo, OK")


# Exercício 4:
# Simule um sistema de login simples:

# 1 - Peça uma senha.
# 2 - Se for igual a "python123", exiba "Acesso permitido!"
# 3 - Senão, exiba "Senha incorreta." 

def tarefa_4(var_tarefa1, var_tarefa2):
#Bom mais um de if ? Vou dificultar esse aqui

    print("Vamos Jogar um Jogo ? Se Finalizar Está liberado, por hoje")
    print("Para Começar apenas maiores de Idade podem jogar !!")
    print(f"Seu usuário é {var_tarefa1}")

 
    strPassword = "python123"
    strUserLogin = int(input("Login de Acesso:"))
    strUserPassword = str(input("Senha de Acesso:"))
    
 
    if var_tarefa2 == "Acesso Negado":
        print("Usuario, Senha ou Idade Incorreta")
        return False
    elif strUserPassword != strPassword:
        print("Senha ou Usuario Incorreto")
        return False
    elif strUserLogin != var_tarefa1:
        print("Usuario ou Senha Incorreta")
        return False
    else:
        print("Acesso Permitido !")
        print("Tarefa Fiinalizada")
        return True

# Return = Mantém a varíavel criada para utilização em outras funções, Obs.: Ao utilizar o return encerra automaticamente a função (if, else, elif etc...)

#Execução Completa


tentativas = 0
resultado_1 = tarefa_1()
print("-------------")
resultado_2 = tarefa_2()
print("-------------")

while tentativas < 3:
    sucesso = tarefa_4(resultado_1, resultado_2)
    print("--------------")
    tentativas = tentativas + 1
    print(f"Tentativas Restantes {3 - tentativas}")
    print("--------------")
