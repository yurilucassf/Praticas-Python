# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

reais = float(input('Digite o valor em reais de quanto tem na carteira?: R$'))

dolar = reais / 3.27

print('Você pode comprar US$ {:.2f}'.format(dolar))
