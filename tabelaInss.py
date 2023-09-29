salario = float(input("informe o salario: "))
if salario <= 1320:
    inss = salario * 0.075
    print("desconto de inss:", inss)
    print("salario liquido: ", salario - inss)
elif salario >= 1320.01 and salario <= 2571.29:
    inss = salario * 0.09
    print("desconto de inss:", inss)
    print("salario liquido: ", salario - inss)
elif salario >= 2571.30 and salario <= 3856.94:
    inss = salario * 0.12
    print("desconto de inss:", inss)
    print("salario liquido: ", salario - inss)
elif salario >= 3856.95 and salario <=7500.94:
    inss = salario * 0.14
    print("desconto de inss:", inss)
    print("salario liquido: ", salario - inss)
elif salario >= 7507.50:
    inss = salario * 0.14
    print("desconto de inss:", inss)
    print("salario liquido: ", salario - inss)

