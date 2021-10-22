"Desafio 14 – Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF."

temperatura = float(input('Qual a temperatura (em ºC)? '))
C = (temperatura*9/5)+32
print('{}ºC correspondem a {}ºF!'.format(temperatura,C))
