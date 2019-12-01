quantidadeInstrucoes = 5


memoria = []

for i in range(quantidadeInstrucoes):
   memoria.append(input())

for i in range(quantidadeInstrucoes):
   memoria[i].replace(" ",",")
   memoria[i].replace(",,",",")
   
aux = memoria[0].split(",")
print("Auxiliar:",aux,"\n\nMemória:",memoria)

x = "ola eu sou o dudi"
x.replace(" ",",")

print(x)