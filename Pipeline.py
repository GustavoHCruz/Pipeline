dictionary = {"inst":0,"mem":20,"reg":11,"PC":0,"IR":"","clock":1,"hazard":0,"pause":0}
memory,registers,instructions = [],[],[]

pipeline,IBR = ["NIL","NIL","NIL","NIL"],["NIL","NIL","NIL"]
labels = {}

def initialize():
   global memory, registers, instructions
   memory = [0 for x in range(dictionary["mem"])]
   registers = [0 for x in range(dictionary["reg"])]

   inst = 0
   while True:
      aux = input()
      if len(aux) == 0:
         break
      if aux.find(":") == -1:
         inst += 1
         instructions.append(aux)
      else:
         aux = aux.replace(" ","")
         aux = aux.split(":")
         labels[aux[0]] = inst
   dictionary["inst"] = inst

def hazardControl():
   cmd,dep = pipeline[1],pipeline[2]

   if cmd.find(":") != -1 or cmd.find("j") != -1:
         return False
   
   cmd = cmd.replace(",","")
   cmd = cmd.split(" ")

   r1,r2 = cmd[2],cmd[-1]

   if r1.find("r") == -1:
      r1 = "NULL"

   if r2.find("r") == -1:
      r2 = "NULL"

   if dep != "NIL" and dep.find(":") == -1:
      dep = dep.replace(",","")
      dep = dep.split(" ")
      dep = dep[0] + dep[1]

   if dep.find(r2) != -1 or dep.find(r1) != -1:
      return True

   return False

def fetch():
   pipeline[0] = instructions[dictionary["PC"]]
   dictionary["IR"] = instructions[dictionary["PC"]]
   dictionary["PC"] += 1

def decode():
   if dictionary["hazard"] == 0:
      IBR[0] = dictionary["IR"]
      if IBR[0].find(":") == -1:
         IBR[0] = IBR[0].replace(",","")
         IBR[0] = IBR[0].replace("\\","")
         IBR[0] = IBR[0].replace("$","")
         IBR[0] = IBR[0].replace("r","")
         IBR[0] = IBR[0].replace("[","")
         IBR[0] = IBR[0].replace("]","")
         IBR[0] = IBR[0].split(" ")
         if len(IBR[0]) != 2:
            IBR[0][1] = int(IBR[0][1])
            IBR[0][2] = int(IBR[0][2])
            if IBR[0][0] != "beq":
               IBR[0][-1] = int(IBR[0][-1])
      else:
         IBR[0] = IBR[0].split(":")
         IBR[0] = IBR[0][1]

   if hazardControl():
      dictionary["hazard"] = 1
   else:
      dictionary["hazard"] = 0

def execute():
   result = 0

   if len(IBR[1]) == 2:
      result = labels[IBR[1][1]]

   elif len(IBR[1]) > 2:
      r1,r2,r3 = IBR[1][1],IBR[1][2],IBR[1][-1]

      if IBR[1][0] == "lw":
         result = memory[r3]
         dictionary["pause"] = 1
      elif IBR[1][0] == "sw":
         result = registers[r1]
         dictionary["pause"] = 1
      elif IBR[1][0] == "li":
         result = r3
      elif IBR[1][0] == "move":
         result = registers[r2]
      elif IBR[1][0] == "add":
         result = registers[r2] + registers[r3]
         dictionary["pause"] = 1
      elif IBR[1][0] == "addi":
         result = registers[r2] + r3
      elif IBR[1][0] == "sub":
         result = registers[r2] - registers[r3]
         dictionary["pause"] = 1
      elif IBR[1][0] == "subi":
         result = registers[r2] - r3
      elif IBR[1][0] == "beq":
         if registers[r1] == registers[r2]:
            result = labels[r3]
         else:
            result = -1
      
   return result

def write(result):
   global IBR,pipeline

   if len(IBR[2]) > 1:
      if len(IBR[2]) == 2:
         dictionary["PC"] = result
         pipeline,IBR = ["NIL","NIL","NIL","NIL"],["NIL","NIL","NIL"]
         dictionary["pause"],dictionary["hazard"] = 0,0
      else:
         r1,r2,r3 = IBR[2][1],IBR[2][2],IBR[2][-1]

         if IBR[2][0] == "sw":
            memory[r2] = result
         elif IBR[2][0] == "beq":
            if result != -1:
               dictionary["PC"] = result
               pipeline,IBR = ["NIL","NIL","NIL","NIL"],["NIL","NIL","NIL"]
               dictionary["pause"],dictionary["hazard"] = 0,0
         else:
            registers[r1] = result

def printPipeline():
   print("\n============Current Clock:",dictionary["clock"],"============")
   print("PC:",dictionary["PC"])
   print("Data Memory:\n",memory)
   print("Registers Memory:\n",registers[1:])
   print("Fetch:\t",pipeline[0])
   print("Decode:\t",pipeline[1])
   print("Execute:",pipeline[2])
   print("Write:\t",pipeline[3])
   print("==========================================")
   dictionary["clock"] += 1

def simulate():
   while True:
      printPipeline()

      if dictionary["pause"] == 0:
         IBR[2] = IBR[1]
         pipeline[3] = pipeline[2]
         if pipeline[3] != "NIL":
            write(result)
      
         if dictionary["hazard"] == 0:
            IBR[1] = IBR[0]
            pipeline[2] = pipeline[1]
            if pipeline[2] != "NIL":
               result = execute()

            if dictionary["hazard"] == 0:
               pipeline[1] = pipeline[0]
               if pipeline[1] != "NIL":
                  decode()
            
               if dictionary["PC"] < len(instructions):
                  fetch()
               else:
                  pipeline[0] = "NIL"
            else:
               pipeline[1] = "NIL"
               decode()
         else:
            pipeline[2] = "NIL"
            if pipeline[1] != "NIL":
               decode()
      else:
         pipeline[3] = "NIL"
         dictionary["pause"] = 0

      if (pipeline[3] == "NIL") and (pipeline[2] == "NIL") and (pipeline[1] == "NIL") and (pipeline[0] == "NIL") and (dictionary["PC"] >= len(instructions)):
         break
   
   printPipeline()

initialize()
simulate()