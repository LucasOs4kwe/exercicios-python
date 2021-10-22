"Desafio 10 – Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comparar."

q_reais = float(input('>>Quanto dinheiro você tem? R$'))
dólar = 3.82
conversão = q_reais / dólar
print('-'*47)
print('Você pode comprar ${:.2f} com essa quantia em R$!'.format(conversão))
print('-'*47)
