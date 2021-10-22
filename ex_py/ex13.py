"Desafio 18 – Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo."

import math
a = float(input('>Digite um ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O ângulo {} tem:\nSeno: {:.3f}\nCosseno: {:.3f}\nTangente: {:.3f}'.format(a,s,c,t))
