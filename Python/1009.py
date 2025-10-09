nome = input("")
salario = float(input(""))
total_de_vendas = float(input(""))

bonificacao = (total_de_vendas * 0.15)
salario_com_bonificacao = salario + bonificacao

salario_final = "{:.2f}".format(salario_com_bonificacao)

print("TOTAL = R$", salario_final)
