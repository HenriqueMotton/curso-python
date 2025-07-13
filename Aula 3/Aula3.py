# for ou while
# for item in range(3):
#   print('Oi')


# SENHA -> Tentar 3 vezes, após isso, bloqueia!

senha = ''
tentativas = 0
senha_correta = 'banana'
numero_tentativar = 3

for tentativas in range(tentativas):
  senha = input('Digita a senha: ')
  if senha == senha_correta:
    print('Acesso liberado!')
    break
  

# while senha != '1234' and tentativas < 3:
#   senha = input('Digita a senha: ')
#   tentativas += 1

# if senha == '1234':
#   print('Acesso liberado!')
# else:
#   print('Acesso bloqueado!')