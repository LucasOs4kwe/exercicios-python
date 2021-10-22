"Desafio 7 – Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média."

nota_1 = float(input('>>Digite uma nota: '))
nota_2 = float(input('>>Digite outra nota: '))
media = float(((nota_1+nota_2)/2))
print('A média do aluno é igual a {}!'.format(media))

if media > 6.5:
    print('O aluno foi aprovado! :)')
else:
    print('O aluno foi reprovado! :(')
