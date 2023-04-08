# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
import math

num = int(input('Digite um número inteiro:'))
dobro = num * 2
triplo = num * 3
raiz = math.sqrt(num)

print('O dobro é {} \nO triplo é {} \nA raiz quadrada é {:.2f}'.format(dobro, triplo, raiz))
