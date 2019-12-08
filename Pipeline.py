dictionary = {"inst": 25,"mem": 20,"reg": 10,"PC": 0,"IR": "","clock": 1}
memory = []
registers = []
instructions = []
pause = [0]

pipeline = ["NIL","NIL","NIL","NIL"]
IBR = ["NIL","NIL","NIL"]
labels = {}

def initialize():
   global memory
   global registers
   global instructions
   memory = [0 for x in range(dictionary["mem"])]
   registers = [0 for x in range(dictionary["reg"])]
   instructions = [input() for x in range(dictionary["inst"])]

   for i in range(dictionary["inst"]):
      if instructions[i].find(":") != -1:
         aux = instructions[i].split(":")
         labels[aux[0]] = i

def hazardControl():
   cmd = instructions[dictionary["PC"]]
   dep = pipeline[1:4]

   if cmd.find(":") != -1 or cmd.find("j") != -1:
         return False
         
   cmd = cmd.replace(" ",",")
   cmd = cmd.replace(",,",",")
   cmd = cmd.split(",")

   r1 = cmd[2]
   r2 = cmd[-1]

   if r1.find("r") == -1:
      r1 = "NULL"

   if r2.find("r") == -1:
      r2 = "NULL"

   for i in range(len(dep)):
      if dep[i] != "NIL" and dep[i].find(":") == -1:
         dep[i] = dep[i].replace(" ",",")
         dep[i] = dep[i].replace(",,",",")
         dep[i] = dep[i].split(",")
         dep[i] = dep[i][0] + dep[i][1]

      if dep[i].find(r2) != -1 or dep[i].find(r1) != -1:
         return True

   return False

def fetch():
   if not hazardControl():
      pipeline[0] = instructions[dictionary["PC"]]
      dictionary["IR"] = instructions[dictionary["PC"]]
      dictionary["PC"] += 1
   else:
      pipeline[0] = "NIL"

def decode():
   IBR[0] = dictionary["IR"]
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

def execute():
   result = 0

   if len(IBR[1]) == 2:
      result = labels[IBR[1][1]]

   elif len(IBR[1]) > 2:
      r1 = IBR[1][1]
      r2 = IBR[1][2]
      r3 = IBR[1][-1]

      if IBR[1][0] == "lw":
         result = memory[r3]
         pause[0] = 1
      elif IBR[1][0] == "sw":
         result = registers[r1]
         pause[0] = 1
      elif IBR[1][0] == "li":
         result = r3
      elif IBR[1][0] == "move":
         result = registers[r2]
      elif IBR[1][0] == "add":
         result = registers[r2] + registers[r3]
         pause[0] = 1
      elif IBR[1][0] == "addi":
         result = registers[r2] + r3
      elif IBR[1][0] == "sub":
         result = registers[r2] - registers[r3]
         pause[0] = 1
      elif IBR[1][0] == "subi":
         result = registers[r2] - r3
      elif IBR[1][0] == "beq":
         if registers[r1] == registers[r2]:
            result = labels[r3]
         else:
            result = -1
      
   return result

def write(result):
   global IBR
   global pipeline
   if len(IBR[2]) > 1:
      if len(IBR[2]) == 2:
         dictionary["PC"] = result
         pipeline = ["NIL","NIL","NIL","NIL"]
         IBR = ["NIL","NIL","NIL"]
      else:
         r1 = IBR[2][1]
         r2 = IBR[2][2]
         r3 = IBR[2][-1]

         if IBR[2][0] == "sw":
            memory[r2] = result
         elif IBR[2][0] == "beq":
            if result != -1:
               dictionary["PC"] = result
               pipeline = ["NIL","NIL","NIL","NIL"]
               IBR = ["NIL","NIL","NIL","NIL"]
         else:
            registers[r1] = result

def printPipeline():
   print("\n=========Current Clock:",dictionary["clock"],"========")
   print("PC:",dictionary["PC"])
   print("Data Memory:\n",memory)
   print("Registers Memory:\n",registers)
   print("Fetch:\t",pipeline[0])
   print("Decode:\t",pipeline[1])
   print("Execute:",pipeline[2])
   print("Write:\t",pipeline[3])
   print("==========================================")
   dictionary["clock"] += 1

def simulate():
   while dictionary["PC"] < len(instructions):
      IBR[2] = IBR[1]
      pipeline[3] = pipeline[2]
      if pipeline[3] != "NIL":
         write(result)
      
      if pause[0] == 0:
         IBR[1] = IBR[0]
         pipeline[2] = pipeline[1]
         if pipeline[2] != "NIL":
            result = execute()

         pipeline[1] = pipeline[0]
         if pipeline[1] != "NIL":
            decode()
      
         fetch()
      else:
         pipeline[2] = "NIL"
         pause[0] = 0
      
      printPipeline()
   
   while (pipeline[3] != "NIL") or (pipeline[2] != "NIL") or (pipeline[1] != "NIL"):
      IBR[2] = IBR[1]
      pipeline[3] = pipeline[2]
      if pipeline[3] != "NIL":
         write(result)
      
      if pause[0] == 0:
         IBR[1] = IBR[0]
         pipeline[2] = pipeline[1]
         if pipeline[2] != "NIL":
            result = execute()

         pipeline[1] = pipeline[0]
         if pipeline[1] != "NIL":
            decode()
      
         pipeline[0] = "NIL"
      else:
         pipeline[2] = "NIL"
         pause[0] = 0

      printPipeline()

initialize()

simulate()