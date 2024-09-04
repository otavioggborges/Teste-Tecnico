# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 
# e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
#  informado um número, ele calcule a sequência de Fibonacci 
# e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE: Esse número pode ser informado 
# através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

### Utilizando as informações propostas, foi chegada a seguinte conclusão: ###

# A sequência de Fibonacci possui a propriedade na Fórmula de Binet: 
# Um número é Fibonacci se e apenas se uma ou ambas as expressões 5*n2 + 4 ou 5*n2 - 4 retornarem um quadrado perfeito.

import math

def éQuadradoPerfeito(x):
	s = int(math.sqrt(x))
	return s*s == x

def éFibonacci(n):
	return éQuadradoPerfeito(5*n*n + 4) or éQuadradoPerfeito(5*n*n - 4)


# Após duas funções para testar se x é um quadrado perfeito e n para testar se é um Fibonacci, uma função para testar]
# se as integrais dentro do range são pertencentes da sequência de Fibonacci

for i in range(1, 35):
	if (éFibonacci(i) == True):
		print(i, "é um número da sequência de Fibonacci")
	else:
		print(i, "não é um número da sequência de Fibonacci")

