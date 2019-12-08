inst = 0 # Tamanho da memória de instruções
mem = 1 # Tamanho da memória de dados
reg = 2 # Quantidade de registradores de uso geral
PC = 3 # Program Counter
IR = 4 # Instruction Register
clock = 6
pause = [0]

dicionario = {inst: 10,mem: 20,reg: 10,PC: 0,IR: "",clock: 1}
memoria = [] # Memória de dados 
registradores = [] # Lista dos registradores
instrucoes = [] # Memória de instruções

pipeline = ["NIL","NIL","NIL","NIL"] # Instruções dentro de cada etapa do pipeline
IBR = ["NIL","NIL","NIL"]
dep = [""] # Lista de registradores dentro do pipelile
labels = []

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
   if IBR[0].find(":") == -1:
      IBR[0] = IBR[0].replace(" ",",")
      IBR[0] = IBR[0].replace(",,",",")
      IBR[0] = IBR[0].replace("\\","")
      IBR[0] = IBR[0].replace("$","")
      IBR[0] = IBR[0].replace("r","")
      IBR[0] = IBR[0].replace("[","")
      IBR[0] = IBR[0].replace("]","")
      IBR[0] = IBR[0].split(",")
      if len(IBR[0]) != 2:
         IBR[0][1] = int(IBR[0][1])
         IBR[0][2] = int(IBR[0][2])
         if IBR[0][0] != "beq":
            IBR[0][-1] = int(IBR[0][-1])
   else:
      IBR[0] = IBR[0].split(":")
      IBR[0] = IBR[0][1]

def execucao():
   resultado = 0

   if len(IBR[1]) == 2:
      for i in range(len(labels)):
         if labels[i][0] == IBR[1][1]:
            resultado = labels[i][1]

   elif len(IBR[1]) > 2:
      r1 = IBR[1][1]
      r2 = IBR[1][2]
      r3 = IBR[1][-1]

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
      elif IBR[1][0] == "sub":
         resultado = registradores[r2] - registradores[r3]
         pause[0] = 1
      elif IBR[1][0] == "subi":
         resultado = registradores[r2] - r3
      elif IBR[1][0] == "beq":
         if registradores[r1] == registradores[r2]:
            for i in range(len(labels)):
               if labels[i][0] == r3:
                  resultado = labels[i][1]
         else:
            resultado = -1
      
   return resultado


def escrita(resultado):
   if len(IBR[2]) > 1:
      if len(IBR[2]) == 2:
         dicionario[PC] = resultado
         pipeline[0] = "NIL"
         pipeline[1] = "NIL"
         pipeline[2] = "NIL"
         pipeline[3] = "NIL"
         IBR[0] = "NIL"
         IBR[1] = "NIL"
         IBR[2] = "NIL"
      else:
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
         elif IBR[2][0] == "beq":
            if resultado != -1:
               dicionario[PC] = resultado
               pipeline[0] = "NIL"
               pipeline[1] = "NIL"
               pipeline[2] = "NIL"
               pipeline[3] = "NIL"
               IBR[0] = "NIL"
               IBR[1] = "NIL"
               IBR[2] = "NIL"

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
   resultado = 0
   while dicionario[PC] < len(instrucoes):
      IBR[2] = IBR[1]
      pipeline[3] = pipeline[2]
      if pipeline[3] != "NIL":
         escrita(resultado)
      
      if pause[0] == 0:
         IBR[1] = IBR[0]
         pipeline[2] = pipeline[1]
         if pipeline[2] != "NIL":
            resultado = execucao()

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
         escrita(resultado)
      
      if pause[0] == 0:
         IBR[1] = IBR[0]
         pipeline[2] = pipeline[1]
         if pipeline[2] != "NIL":
            resultado = execucao()

         pipeline[1] = pipeline[0]
         if pipeline[1] != "NIL":
            decodificacao()
      
         pipeline[0] = "NIL"
      else:
         pipeline[2] = "NIL"
         pause[0] = 0

      imprimir()

def lidarJump():
   for i in range(dicionario[inst]):
      if instrucoes[i].find(":") != -1:
         aux = instrucoes[i].split(":")
         labels.append([aux[0],i])

def main():
   inicializarMemoria()
   inicializarRegistradores()
   inicializarInstrucoes()

   lidarJump()

   simular()

main()