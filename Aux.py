inst = 3 # Tamanho da memória de instruções
mem = 20 # Tamanho da memória de dados
reg = 10 # Quantidade de registradores

memoria = [] # Memória de dados
registradores = [] # Lista dos registradores
instrucoes = [] # Memória de instruções

# Inicializa a memória de dados
for i in range(mem):
      memoria.append(0)

# Inicializa a lista dos registradores
for i in range(reg):
      registradores.append(0)

# Inicializa a memória de instruções
for i in range(inst):
      instrucoes.append(input())

PC = 0 # Program Counter
IR = "" # Instruction Register
IBR = "" # Instruction Buffer Register
pipeline = ["","","",""] # Instruções dentro de cada etapa do pipeline
clock = 1

# Execução
for i in range(inst):

   # Busca
   pipeline[0] = instrucoes[PC]
   IR = instrucoes[PC]
   PC = PC+1

   # Decodificação
   pipeline[1] = IR
   IBR = IR
   IBR = IBR.replace(" ",",")
   IBR = IBR.replace(",,",",")
   IBR = IBR.replace("$","")
   IBR = IBR.replace("\\","")
   IBR = IBR.replace("[","")
   IBR = IBR.replace("]","")
   IBR = IBR.split(",")

   # Execucao
   pipeline[2] = IR
   # Unidade de Controle
   r1 = IBR[1]
   r1 = int(r1[-1])
   r2 = IBR[2]
   r2 = int(r2[-1])
   r3 = IBR[-1]
   r3 = r3.replace("r","")
   r3 = int(r3)

   if IBR[0] == "lw":
      registradores[r1] = memoria[int(IBR[2])]
   elif IBR[0] == "sw":
      memoria[int(IBR[2])] = registradores[r1]
   elif IBR[0]  == "li":
      registradores[r1] = r3
   elif IBR[0] == "move":
      registradores[r1] = registradores[r2]
   elif IBR[0] == "add":
      registradores[r1] = registradores[r2] + registradores[r3]
   elif IBR[0] == "addi":
      registradores[r1] = registradores[r2] + r3
   elif IBR[0] == "sub":
      registradores[r1] = registradores[r2] - registradores[r3]
   elif IBR[0] == "subi":
      registradores[r1] = registradores[r2] - r3

   # Escrita
   pipeline[3] = IR

   # Impressão
   print("\nCiclo de Clock atual:",clock)
   print("Memória de Dados:\n",memoria)
   print("Memória de Registradores:\n",registradores)
   print("Registrador Interno:\nPC:",PC)
   print("Pipeline:")
   print("Busca de Instrução:",pipeline[0])
   print("Decoficiação:",pipeline[1])
   print("Execução:",pipeline[2])
   print("Escrita:",pipeline[3])
   clock = clock+1