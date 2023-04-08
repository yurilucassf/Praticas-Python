# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo
# - Quantas letras tem o primeiro nome.
nome = str(input('Digite um nome:'))
nMinusculas = nome.lower()
nMaiuscula = nome.upper()
qLetras = len(nome.replace(" ", ""))
nSeparado = nome.split()
pNome = nSeparado[0]
qPrimeiroNome = len(pNome)
print(qPrimeiroNome)
print("""Nome maiúsculo: {}  \nNome minúsculo: {} \nQuantidade de letras ao todo: {} \nQuantidade de letras do primeiro nome: {}""" .format(nMaiuscula, nMinusculas, qLetras, qPrimeiroNome))
