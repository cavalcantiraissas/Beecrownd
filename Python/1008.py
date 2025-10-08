numero_funcionario = int(input(""))
horas_trabalhadas = int(input(""))
valor_hora = float(input(""))
salario = horas_trabalhadas * valor_hora
salario1 = "{:.2f}".format(salario)
print("NUMBER =", numero_funcionario)
print("SALARY = U$", salario1)
