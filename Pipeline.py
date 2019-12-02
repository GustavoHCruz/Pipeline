# Tamanho da memória de instruções
inst = 25
# Tamanho da memória de dados
mem = 20
# Quantidade de Registradores
reg = 10

# Clock atual
clock = 1

# Registradores internos
PC = 0
IR = []

# Vetor com registradores em execução
dep = []
# Vetor com os comandos do pipeline
pipeline = []

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

def imprimir():
   print("Ciclo de Clock atual:",clock)
   print("\nMemória de Dados:\n",memoria)
   print("\nMemória de Registradores:\n",registradores)
   print("\nRegistrador Interno:",PC)
   print("\nPipeline:\nBusca de Instrução:")

def busca():
   IR = instrucoes[PC].split(",")
   PC = PC+1

def decodificacao():
   a = 0

def execucao():
   a = 0

def escrita():
   a = 0

def clock():
   imprimir()
   clock = clock+1

# Main
memoria = iniciar_memoria()
registradores = iniciar_registradores()
instrucoes = iniciar_instrucoes()

