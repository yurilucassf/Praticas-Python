# Faça um programa que leia algo pelo teclado e mostre o seu tipo primitivo e todas as informações possíveis sobre ele:
n = input('Digite algo: ')
print('O tipo dessa entrada é: ',type(n))
print('Esse valor é um inteiro? ', n.isnumeric())
print('Esse valor é alfabetico? ', n.isalpha())
print('Esse valor é alfanumerico? ', n.isalnum())
print('Esse valor está com caracteres somente em letras maiúsculas? ', n.isupper())
print('Esse valor está com caracteres somente em letras minúsculas? ', n.islower())
