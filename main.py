from random import sample
from array import array
import sys

sorteio = sample(range(0, 100), 10)

indexAcerto = 0
numero = []
numeroCorreto = []
numeroPalpite = 15

for i in range (0, numeroPalpite):
  numero.append( int(input('Digite um número: ')))
  for x in range(0, 9): 
    if (numero[i] == sorteio[x]):
      numeroCorreto.append(numero[i])
      indexAcerto = indexAcerto + 1


print("Números sorteados: ",sorteio)

print("Os palpites são: ", numero)

if indexAcerto > 0:

  print("Você acertou " + str(indexAcerto) + " e errou " + str(numeroPalpite - indexAcerto))
else:
  print("Você não acertou nenhum número")