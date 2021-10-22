"Desafio 8 – Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros."

valor_m = float(input('>>Digite o valor em metros: '))
valor_cm = float(valor_m*100)
valor_mm = float(valor_m*1000)
print('{} metros são equivalentes a {} centímetros e {} milímetros.'.format(valor_m,valor_cm,valor_mm))
