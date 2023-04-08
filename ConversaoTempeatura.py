# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celcius = float(input('Digite a temperatura em °C: '))
fahre = ((9 * celcius) / 5)+32
print('{}°C em Fahrenheit é {}°F'.format(celcius, fahre))
