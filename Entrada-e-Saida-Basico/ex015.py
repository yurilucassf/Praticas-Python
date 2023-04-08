# Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Digite o valor do produto: '))

novoSalario = salario * 1.15

print('O novo sálario é R${:.2f}'.format(novoSalario))