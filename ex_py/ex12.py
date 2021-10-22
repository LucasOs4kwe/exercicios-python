"Desafio 17 – Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa."

from math import pow,sqrt
c_o = float((input('Qual é o comprimento do cateto oposto? ')))
c_a = float(input('Qual é o comprimento do cateto adjacente? '))
h = pow(c_o,2)+pow(c_a,2)
h_2 = (sqrt(h))
print('A hipotenusa vale {:.2f}'.format(h_2))
