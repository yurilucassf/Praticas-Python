# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

num = float(input('Digite o valoe em metros: '))

centi = num * 100
mili = num * (100*10)

print('O valor em centímetros é {}cm \nO valor em milímetros é {}mm'.format(centi, mili))
