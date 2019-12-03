inst = 0 # Tamanho da memória de instruções
mem = 1 # Tamanho da memória de dados
reg = 2 # Quantidade de registradores de uso geral
PC = 3 # Program Counter
IR = 4 # Instruction Register
clock = 6
pause = [0]

dicionario = {inst: 14,mem: 20,reg: 10,PC: 0,IR: "",clock: 1}
memoria = [] # Memória de dados 
registradores = [] # Lista dos registradores
instrucoes = [] # Memória de instruções

pipeline = ["NIL","NIL","NIL","NIL"] # Instruções dentro de cada etapa do pipeline
IBR = ["NIL","NIL","NIL"]
dep = [""] # Lista de registradores dentro do pipelile

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
   IBR[0] = dicionario[IR]
   IBR[0] = IBR[0].replace(" ",",")
   IBR[0] = IBR[0].replace(",,",",")
   IBR[0] = IBR[0].replace("\\","")
   IBR[0] = IBR[0].replace("$","")
   IBR[0] = IBR[0].replace("r","")
   IBR[0] = IBR[0].replace("[","")
   IBR[0] = IBR[0].replace("]","")
   IBR[0] = IBR[0].split(",")
  
   IBR[0][1] = int(IBR[0][1])
   IBR[0][2] = int(IBR[0][2])
   IBR[0][-1] = int(IBR[0][-1])

def execucao():
   r1 = IBR[1][1]
   r2 = IBR[1][2]
   r3 = IBR[1][-1]

   resultado = 0

   if IBR[1][0] == "lw":
      resultado = memoria[r3]
      pause[0] = 1
   elif IBR[1][0] == "sw":
      resultado = registradores[r1]
      pause[0] = 1
   elif IBR[1][0] == "li":
      resultado = r3
   elif IBR[1][0] == "move":
      resultado = registradores[r2]
   elif IBR[1][0] == "add":
      resultado = registradores[r2] + registradores[r3]
      pause[0] = 1
   elif IBR[1][0] == "addi":
      resultado = registradores[r2] + r3
      print(resultado)
   elif IBR[1][0] == "sub":
      resultado = registradores[r2] - registradores[r3]
      pause[0] = 1
   elif IBR[1][0] == "subi":
      resultado = registradores[r2] - r3
   
   return resultado

def escrita(resultado):
   r1 = IBR[2][1]
   r2 = IBR[2][2]
   r3 = IBR[2][-1]

   if IBR[2][0] == "lw":
      registradores[r1] = resultado
   elif IBR[2][0] == "sw":
      memoria[r2] = resultado
   elif IBR[2][0]  == "li":
      registradores[r1] = resultado
   elif IBR[2][0] == "move":
      registradores[r1] = resultado
   elif IBR[2][0] == "add":
      registradores[r1] = resultado
   elif IBR[2][0] == "addi":
      registradores[r1] = resultado
   elif IBR[2][0] == "sub":
      registradores[r1] = resultado
   elif IBR[2][0] == "subi":
      registradores[r1] = resultado

def imprimir():
   print("\n=========Ciclo de Clock atual:",dicionario[clock],"========")
   print("PC:",dicionario[PC] - 1)
   print("Memória de Dados:\n",memoria)
   print("Memória de Registradores:\n",registradores)
   print("Busca de Instrução:",pipeline[0])
   print("Decoficiação:",pipeline[1])
   print("Execução:",pipeline[2])
   print("Escrita:",pipeline[3])
   print("==========================================")
   dicionario[clock] += 1

def simular():
   saida = 0
   for i in range(len(instrucoes)):
      IBR[2] = IBR[1]
      pipeline[3] = pipeline[2]
      if pipeline[3] != "NIL":
         escrita(saida)
      
      if pause[0] == 0:
         IBR[1] = IBR[0]
         pipeline[2] = pipeline[1]
         if pipeline[2] != "NIL":
            saida = execucao()

         pipeline[1] = pipeline[0]
         if pipeline[1] != "NIL":
            decodificacao()
      
         busca()
      else:
         pipeline[2] = "NIL"
         pause[0] = 0
      
      imprimir()
   
   while (pipeline[3] != "NIL") or (pipeline[2] != "NIL") or (pipeline[1] != "NIL"):
      IBR[2] = IBR[1]
      pipeline[3] = pipeline[2]
      if pipeline[3] != "NIL":
         escrita(saida)
      
      if pause[0] == 0:
         IBR[1] = IBR[0]
         pipeline[2] = pipeline[1]
         if pipeline[2] != "NIL":
            saida = execucao()

         pipeline[1] = pipeline[0]
         if pipeline[1] != "NIL":
            decodificacao()
      
         pipeline[0] = "NIL"
      else:
         pipeline[2] = "NIL"
         pause[0] = 0

      imprimir()

def main():

   inicializarMemoria()
   inicializarRegistradores()
   inicializarInstrucoes()

   simular()

main()