# Bloco de código que executa uma tarefa específica.
  # Serve pra organizar, reutilizar e simplificar o código

# Regras de ouro:
  # Nome de função tem que começar com letra minuscula
    # Os nomes tem que ser descritivos e diretos
    # Cada função tem que fazer uma coisa só
    # Escrever comentários -> Leves!
  # Os parametros sem são com todas as letras minusculas
    # Precisando de mais de uma palavra no parametro, separa usando underline: nome_completo

nome_usuario = ''

def saudacao(nome_completo='Suden'):
  print(f"Olá, {nome_completo}! Bem-vindo ao curso de Python!")

def soma_sub(a, b):
  soma = a + b
  sub = a - b

  return soma, sub

def capturar_nome_usuario():
  global nome_usuario 
  nome_usuario = input("Qual o seu nome?")

def valida_idade(idade):
  if idade < 0:
    return 'Idade inválida'
  elif idade < 18:
    return 'Menor de idade'
  else:
    return 'Maior de idade'
    
# capturar_nome_usuario()

saudacao()
resul_soma, resul_sub = soma_sub(5, 1)

print('Soma: ', resul_soma)
print('Sub: ', resul_sub)
print('Validação idade: ', valida_idade(25))


# Criar uma mini-calculadora
# Soma
# Subtrai
# Multiplica
# Dividi