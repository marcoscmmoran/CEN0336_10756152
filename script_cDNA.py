#!/usr/bin/env python3
import sys

DNA = sys.argv[1] # coloca a string do dna
n1 = sys.argv[2]  # coloca os valores de n1
n2 = sys.argv[3]  # coloca os valores de n2
n3 = sys.argv[4]  # coloca os valores de n3
n4 = sys.argv[5]  # coloca os valores de n4

n1 = int(n1) # converte os n1 para int
n2 = int(n2) # converte os n2 para int
n3 = int(n3) # converte os n3 para int
n4 = int(n4) # converte os n4 para int

CDS1 = DNA[n1:n2] # determina CDS1 e CDS2
print(CDS1)
CDS2 = DNA[n3:n4]
print(CDS2)

if CDS1[0:3] == 'ATG': # testa se CDS1 começa com ATG
	if CDS2[-3:] == 'TAA' or CDS2[-3:] == 'TAG' or CDS2[-3:] == 'TGA': # verifica se CDS2 termina com algum dos codon escolhidos
                print(CDS1 + CDS2)
	else:
                print('CDS2 não finaliza com um codon de fechamento')
else:
        print('CDS1 não começa com um codon de inicio')
