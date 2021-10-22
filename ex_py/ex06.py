""""
Desafio 11 – Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
"""

largura = float(input('>>Qual é a largura dessa parede?: '))
altura = float(input('>>Qual é a altura dessa parede?: '))
área = float(largura*altura)
qntd_tinta = float(área/2)
print('A área dessa parede é de {}m², portanto serão necessários {} litros de tinta para pintar essa parede.'.format(área,qntd_tinta))
