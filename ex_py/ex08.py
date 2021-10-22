"Desafio 13 – Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de desconto."

salário_inicial = float(input('>>>Digite seu antigo salário: '))
aumento = float(input('>>>Digite a porcentagem de aumento: '))
salário_atual = float((salário_inicial*aumento)/100)
soma_novo_salário = float(salário_atual+salário_inicial)
print('O aumento será de {:.2f}R$, portanto, seu novo salário será de {:.2f}R$.'.format(salário_atual,soma_novo_salário))
