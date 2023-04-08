# Um professor que sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo e escrevendo o nome do escolhido.
import random
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
lista = [aluno3, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('O escolhido foi {}'.format(escolhido))