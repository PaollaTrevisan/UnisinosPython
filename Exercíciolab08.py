print('Grau A')
pratica = float(input('Nota da Atividade prática: '))
teorica = float(input('Nota da Atividade teórica: '))

print('Grau B')
laboratorio = float(input('Nota da Prova em Laboratório: '))
teste = float(input('Nota do Teste Teórico: '))
trabalho = float(input('Nota do Trabalho Extraclasse: '))

nota_pratica = pratica*0.45
nota_teorica = teorica*0.55
nota_laboratorio = laboratorio*0.60
nota_teste = teste*0.20
nota_trabalho = trabalho*0.20
nota_final = (nota_teorica + nota_pratica + nota_laboratorio + nota_teste + nota_trabalho)/2
print('Média final: ',nota_final)