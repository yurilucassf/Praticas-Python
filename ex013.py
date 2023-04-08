# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2

largura = float(input('Digite o valor da largura: '))
altura = float(input('Digite o valor da altura: '))

area = largura * altura
qtdLitro = area/2

print('Área da parede: {}\nQuantidade de tinta: {}L'.format(area,qtdLitro))
