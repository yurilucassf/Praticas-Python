# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor
num = int(input('Digite um número inteiro:'))
antes = num - 1
depois = num + 1
print('O antecessor é {} e o sucessor é {}'.format(antes, depois))
