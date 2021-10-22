"Desafio 12 – Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto."

vsd = float(input('Valor sem desconto: '))
desconto = float(input('Desconto (em %): '))
liquidação = float((desconto*vsd)/100)
preço_final = float(vsd - liquidação)
print('O desconto será de {:.2f}R$, portanto seu preço será de {:.2f}R$'.format(liquidação,preço_final))
