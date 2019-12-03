inst = 0 # Tamanho da memória de instruções
mem = 1 # Tamanho da memória de dados
reg = 2 # Quantidade de registradores de uso geral
PC = 3 # Program Counter
IR = 4 # Instruction Register
IBR = 5 # Instruction Buffer Register
clock = 6

dicionario = {inst: 3,mem: 20,reg: 10,PC: 0,IR: "",IBR: "",clock: 1}
memoria = [] # Memória de dados 
registradores = [] # Lista dos registradores
instrucoes = [] # Memória de instruções

pipeline = ["","","",""] # Instruções dentro de cada etapa do pipeline

def inicializarMemoria():
   for i in range(dicionario[mem]):
      memoria.append(0)   

def inicializarRegistradores():
   for i in range(dicionario[reg]):
      registradores.append(0)

def inicializarInstrucoes():
   for i in range(dicionario[inst]):
      instrucoes.append(input())

def busca():
   pipeline[0] = instrucoes[dicionario[PC]]
   dicionario[IR] = instrucoes[dicionario[PC]]
   dicionario[PC] += 1

def decodificacao():
   pipeline[1] = dicionario[IR]
   dicionario[IBR] = dicionario[IR]
   dicionario[IBR] = dicionario[IBR].replace(" ",",")
   dicionario[IBR] = dicionario[IBR].replace(",,",",")
   dicionario[IBR] = dicionario[IBR].replace("$","")
   dicionario[IBR] = dicionario[IBR].replace("r","")
   dicionario[IBR] = dicionario[IBR].replace("\\","")
   dicionario[IBR] = dicionario[IBR].replace("[","")
   dicionario[IBR] = dicionario[IBR].replace("]","")
   dicionario[IBR] = dicionario[IBR].split(",")
   dicionario[IBR][1] = int(dicionario[IBR][1])
   dicionario[IBR][2] = int(dicionario[IBR][2])
   dicionario[IBR][-1] = int(dicionario[IBR][-1])

def execucao():
   pipeline[2] = dicionario[IR]

   r1 = dicionario[IBR][1]
   r2 = dicionario[IBR][2]
   r3 = dicionario[IBR][-1]

   if dicionario[IBR][0] == "lw":
      resultado = memoria[r3]
   elif dicionario[IBR][0] == "sw":
      resultado = registradores[r1]
   elif dicionario[IBR][0]  == "li":
      resultado = r3
   elif dicionario[IBR][0] == "move":
      resultado = registradores[r2]
   elif dicionario[IBR][0] == "add":
      resultado = registradores[r2] + registradores[r3]
   elif dicionario[IBR][0] == "addi":
      restulado = registradores[r2] + r3
   elif dicionario[IBR][0] == "sub":
      resultado = registradores[r2] - registradores[r3]
   elif dicionario[IBR][0] == "subi":
      resultado = registradores[r2] - r3
   
   return resultado

def escrita(resultado):
   pipeline[3] = dicionario[IR]

   r1 = dicionario[IBR][1]
   r2 = dicionario[IBR][2]
   r3 = dicionario[IBR][-1]

   if dicionario[IBR][0] == "lw":
      registradores[r1] = resultado
   elif dicionario[IBR][0] == "sw":
      memoria[r2] = resultado
   elif dicionario[IBR][0]  == "li":
      registradores[r1] = resultado
   elif dicionario[IBR][0] == "move":
      registradores[r1] = resultado
   elif dicionario[IBR][0] == "add":
      registradores[r1] = resultado
   elif dicionario[IBR][0] == "addi":
      registradores[r1] = restulado
   elif dicionario[IBR][0] == "sub":
      registradores[r1] = resultado
   elif dicionario[IBR][0] == "subi":
      registradores[r1] = resultado

def imprimir():
   print("\nCiclo de Clock atual:",dicionario[clock])
   print("Memória de Dados:\n",memoria)
   print("Memória de Registradores:\n",registradores)
   print("Registrador Interno:\nPC:",dicionario[PC])
   print("Pipeline:")
   print("Busca de Instrução:",pipeline[0])
   print("Decoficiação:",pipeline[1])
   print("Execução:",pipeline[2])
   print("Escrita:",pipeline[3])
   dicionario[clock] += 1

def simular():
   for i in range(dicionario[inst]):

      busca()

      decodificacao()

      saida = execucao()

      escrita(saida)

      imprimir()

def main():

   inicializarMemoria()
   inicializarRegistradores()
   inicializarInstrucoes()

   simular()

main()