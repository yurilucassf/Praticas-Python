# Adição, subtração, multiplicação, divisão, exponenciação e quociente

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

soma = n1 + n2
menos = n1 - n2
divisao = n1 / n2
dInteira = n1 // n2
expo = n1 ** n2
multi = n1 * n2

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(soma, multi, divisao))
print('Divisão inteira é {} e a potência é {}'.format(dInteira, expo))
