# Automação:
#   Go
#   Python
#   C
#   Ruby


#   Games
#   Java  -> Open Source  (Muitas bibliotecas)  -> JVM(Java Virtual Machinne)
#   C#    -> Microsoft    (Microsoft faz bastante libs)  ->  (Open Source)
#   Node (JavaScript)
#   Python


#   Desenvolvimento Web e Aplicativos
#   Node
#   Python
#   Java
#   C#
#   C


#   Layout -> Frontend -> Node
#   Lógica -> Backend  -> Python
#   TarefaAparte  ->  Micro-serviço  -> Java

#   Curva de aprendizado: Baixa -> Python  -> Node
#   Curva de aprendizado: Alta  -> Java(Orientado a objetos)

#   Python (Alto nivel, Interpretado, dinâmico e multiparadigma)
#   Carro ( nome, cor, velocidade, tamanho, som )

# Variaveis:
# letra minuscula
# Sem caractere especial, menos: underline
# Constantes -> Caixa alta
# Variaveis -> Caixa baixa, iniciando com letra minuscula e separando por underline ou cameCase


def main():
  print('SOMA: ', soma(1, 1))
  print('SUBTRAÇÃO: ', sub(1, 1))
  print('MULTIPLICACAO: ', mult(2, 2))

def soma(parametro1, parametro2):
  return parametro1 + parametro2

def sub(parametro1, parametro2):
  return parametro1 - parametro2

def mult(parametro1, parametro2):
  return parametro1 * parametro2

if __name__ == "__main__":
  main()