# Quantidade de instruções
inst = 25
# Tamanho da memória
mem = 25
# Quantidade de Registradores
reg = 10

# Função para inicializar a Memória de Dados
def iniciar_memoria():
   memoria = []
   for i in range(mem):
      memoria.append(0)
   return memoria

# Função para inicializar os valores dos Registradores internos
def iniciar_registradores():
   registradores = []
   for i in range(reg):
      registradores.append(0)
   return registradores

# Função para pegar e inicializar a Memória de Instruções
def iniciar_instrucoes():
   instrucoes = []
   for i in range(inst):
      instrucoes.append(input())
      instrucoes[i] = instrucoes[i].replace(" ",",")
      instrucoes[i] = instrucoes[i].replace(",,",",")
      instrucoes[i] = instrucoes[i].replace("$","")
      instrucoes[i] = instrucoes[i].replace("\\","")
      instrucoes[i] = instrucoes[i].replace("[","")
      instrucoes[i] = instrucoes[i].replace("]","")
   return instrucoes

# Main
memoria = iniciar_memoria()
registradores = iniciar_registradores()
instrucoes = iniciar_instrucoes()