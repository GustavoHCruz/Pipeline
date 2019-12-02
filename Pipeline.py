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
IBR = []

# Vetor com registradores em execução
dep = []
# Vetor com os comandos do pipeline
pipeline = ["NIL","NIL","NIL","NIL"]
# Código da operação atual
opcode = 0

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

def UC(IR):
   a = 0

def ULA(IBR,op):
   if op == 1: # Soma
      return = IBR[0] + IBR[1]
   if op == 2: # Subtração
      return = IBR[0] - IBR[1]
   if op == 3: # Copia
      return = IBR[1]


def imprimir():
   print("Ciclo de Clock atual:",clock)
   print("\nMemória de Dados:\n",memoria)
   print("\nMemória de Registradores:\n",registradores)
   print("\nRegistrador Interno:",PC)
   print("\nPipeline:")
   print("\nBusca de Instrução:",pipeline[0])
   print("\nDecoficiação:",pipeline[1])
   print("\nExecução:",pipeline[2])
   print("\nEscrita:",pipeline[3])

def busca():
   pipeline[0] = instrucoes[PC]
   IR = instrucoes[PC]
   PC = PC+1

def decodificacao():
   pipeline[1] = IR
   opcode = IBR[0]
   IBR = IR.split(",")
   IBR.pop(0)

def execucao():
   pipeline[2] = IR

def escrita():
   pipeline[3] = IR

def clock():
   while i < inst:
      i = i+1
      imprimir()
      clock = clock+1


# Main
memoria = iniciar_memoria()
registradores = iniciar_registradores()
instrucoes = iniciar_instrucoes()

clock()