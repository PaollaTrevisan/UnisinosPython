#Crie um programa que recebe dois valores inteiros pelo teclado e imprime
#qual dos dois é maior.
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 > num2:
    print('Valor',num1,'é maior que',num2)
else:
    print('Valor',num2,'é maior que',num1)