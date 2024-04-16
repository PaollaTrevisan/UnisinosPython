print("- Digite 1 para somar dois valores")
print("- Digite 2 para subtrair dois valores")
print("- Digite 3 para multiplicar dois valores")
print("- Digite 4 para dividir dois valores")
print("- Digite 5 para realizar uma potência entre doisvalores")
print("- Digite 6 para realizar uma radiciação entre doisvalores")
print("- Digite qualquer outro número para sair\n")
opcao = int(input("Digite sua opção:"))
a = int(input("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))
if opcao == 1:
        print("Soma dos valores: ",(a+b))
elif opcao == 2:
        print("Diferença dos valores: ",(a-b))
elif opcao == 3:
        print("Produto dos valores: ",(a*b))
elif opcao == 4:
        if b != 0:
                print("Divisão dos valores: ",(a/b))
        else:
                print("Não posso dividir por zero.")
elif opcao == 5:
        print("a elevado a b: ",(a**b))
elif opcao == 6:
        print("Raiz (fator b) de a: ",(a**(1/b)))
else:
        print("Tchau =)")