def iniciar_memoria(memoria,mem):
   for i in range(mem):
      memoria.append(0)

def iniciar_registradores(registradores,reg):
   for i in range(reg):
      registradores.append(0)

def iniciar_instrucoes(instrucoes,inst):
   for i in range(inst):
      instrucoes.append(input())

def UC(IBR):
   opcode = IBR[0]

   if opcode == "lw":
      IBR[1] = IBR[1].replace("r","")
      r1 = int(IBR[1])
      registradores[r1] = memoria[int(IBR[2])]
   elif opcode == "sw":
      IBR[1] = IBR[1].replace("r","")
      r1 = int(IBR[1])
      memoria[int(IBR[2])] = registradores[r1]
   elif opcode  == "li":
      IBR[1] = IBR[1].replace("r","")
      r1 = int(IBR[1])
      registradores[r1] = IBR[2]
   elif opcode == "move":
      IBR[1] = IBR[1].replace("r","")
      r1 = int(IBR[1])
      IBR[2] = IBR[2].replace("r","")
      r2 = int(IBR[2])
      registradores[r1] = registradores[r2]
   elif opcode == "add":
      IBR[1] = IBR[1].replace("r","")
      r1 = int(IBR[1])
      IBR[2] = IBR[2].replace("r","")
      r2 = int(IBR[2])
      IBR[3] = IBR[3].replace("r","")
      r3 = int(IBR[3])
      registradores[r1] = registradores[r2] + registradores[r3]
   elif opcode == "addi":
      IBR[1] = IBR[1].replace("r","")
      r1 = int(IBR[1])
      IBR[2] = IBR[2].replace("r","")
      r2 = int(IBR[2])
      registradores[r1] = registradores[r2] + IBR[3]
   elif opcode == "sub":
      IBR[1] = IBR[1].replace("r","")
      r1 = int(IBR[1])
      IBR[2] = IBR[2].replace("r","")
      r2 = int(IBR[2])
      IBR[3] = IBR[3].replace("r","")
      r3 = int(IBR[3])
      registradores[r1] = registradores[r2] - registradores[r3]
   elif opcode == "subi":
      IBR[1] = IBR[1].replace("r","")
      r1 = int(IBR[1])
      IBR[2] = IBR[2].replace("r","")
      r2 = int(IBR[2])
      registradores[r1] = registradores[r2] - IBR[3]

def imprimir():
   print("\nCiclo de Clock atual:",clock)
   print("Memória de Dados:\n",memoria)
   print("Memória de Registradores:\n",registradores)
   print("Registrador Interno:\nPC:",PC)
   print("Pipeline:")
   print("Busca de Instrução:",pipeline[0])
   print("Decoficiação:",pipeline[1])
   print("Execução:",pipeline[2])
   print("Escrita:",pipeline[3])

def busca(pipeline,PC,IR):
   pipeline[0] = instrucoes[PC]
   IR[0] = instrucoes[PC]
   PC = PC+1

def decodificacao(pipeline):
   pipeline[1] = IR
   aux = str(IR)
   IBR = aux.split(",")

def execucao(pipeline):
   pipeline[2] = IR
   UC(IBR)

def escrita(pipeline):
   pipeline[3] = IR

def executar(memoria,registradores,instrucoes,mem,reg,inst):
   PC = 0 # Program Counter
   IR = ["","","",""] # Instruction Register
   IBR = ["","","",""] # Instruction Buffer Register
   pipeline = ["","","",""] # Instruções dentro de cada etapa do pipeline

   clock = 1
   for i in range(inst):

      busca(pipeline,PC,IR)
      decodificacao(pipeline)
      execucao(pipeline)
      escrita(pipeline)

      imprimir()
      clock = clock+1

def main():
   inst = 1 # Tamanho da memória de instruções
   mem = 20 # Tamanho da memória de dados
   reg = 10 # Quantidade de registradores

   memoria = [] # Memória de dados
   registradores = [] # Lista dos registradores
   instrucoes = [] # Memória de instruções
   iniciar_memoria(memoria,mem) # Inicializa a memória de dados
   iniciar_registradores(registradores,reg) # Inicializa a lista dos registradores
   iniciar_instrucoes(instrucoes,inst) # Inicializa a memória de instruções

   executar(memoria,registradores,instrucoes,mem,reg,inst)

main()