conta_normal = True
conta_universitaria = False

saldo = 2000
saque = float(input("Informe o valor do saque: "))
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque utilizado com o uso do cheque especial!")
    else:
        print("Saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
else:
    print("Conta incorreta!\nEntre em contato com o gerente de sua agência.")