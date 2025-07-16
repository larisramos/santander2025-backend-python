opcao = -1

while opcao != 0:
    opcao = int(input("[1] SAQUE\n[2] EXTRATO\n[0] SAIR\n\nSelecione a opção: "))
    
    if opcao == 1:
        print ("Sacando...")
        break
    elif opcao == 2:
        print ("Exibindo o extrato")
        break
else:
    print ("Obrigado por utilizar nosso banco!")