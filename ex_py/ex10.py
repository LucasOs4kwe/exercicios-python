""""
Desafio 15 – Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
 e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado.
"""
d = int(input('>Quantos dias você utilizou o carro? '))
km = float(input('>Quantos km você rodou com o carro? '))
total = (60*d)+(0.15*km)
print('-'*87)
print('>Você utilizou o carro por {} dia(s), rodou {}km e, como total, terá que pagar R${}.'.format(d,km,total))
print('-'*87)
