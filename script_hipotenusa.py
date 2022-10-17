#!/usr/bin/env python3
import sys

X = sys.argv[1] # seleciona o valor de X

Y = sys.argv[2] # seleciona o valor de Y


if str.isdigit(X) == True: # etapa de confirmção se os caracteres digitados são algarismos 
	if str.isdigit(Y) == True:
		X = int(X) # transforma o valor de X em um valor do tipo int
		Y = int(Y) # transforma o valor de Y em um valor do tipo int
	else:
		print('digite 2 numeros')
else:
	print('digite 2 numeros')


Z = X^2 + Y^2  # Z com o valor da hipotenusa ao quadrado



print('O valor do quadrado da hipotenusa para o triangulo com lados a=',X,'e b=',Y,' é',Z)
