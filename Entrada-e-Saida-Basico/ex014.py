# Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Digite o valor do produto: R$'))

novoPreco = preco * 0.95

print('O preço com desconto é R${:.2f}'.format(novoPreco))