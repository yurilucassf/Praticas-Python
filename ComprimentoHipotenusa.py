# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
CatetoOposto = float(input('Digite o valor do comprimento do cateto oposto: '))
CatetoAdjacente = float(input('Digite o valor do comprimento do cateto adjacente: '))
#Hipotenusa = (CatetoOposto ** 2 + CatetoAdjacente ** 2) ** (1/2)
Hipotenusa = math.hypot(CatetoOposto, CatetoAdjacente)
print('A hipotenusa vai medir {:.2f}'.format(Hipotenusa))



