media = 6
resp = 1
soma = 0
cont = 0
while resp != 0:
    nota = float(input("Informe a nota: "))
    soma = soma + nota
    cont = cont + 1
    resp = int(input("Digite [0] para sair ou [1] para continuar"))
media = soma / cont
print('soma: ',soma)
print('Média: ',media)
if media >= 7:
    print("Aprovado")
elif media >= 5 and media < 7:
    print("recuperação")
else:
    print("Reprovado")
for num in range(0,21):
    print(num)