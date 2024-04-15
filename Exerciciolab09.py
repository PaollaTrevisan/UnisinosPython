#Crie um programa que recebe um inteiro pelo teclado e imprime se ele é
#par ou ímpar.
numero = int(input("Digite um valor: "))
if numero == 0:
    print('Inválido! Número igual a zero.')
elif numero < 0:
    print('Inválido! Número negativo')
elif numero % 2 == 0:
    print(numero,'é par')
else:
    print(numero,('é impar.'))