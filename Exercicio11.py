value = input("Digite seu Salário Antigo: ")
salario01 = float(value)

value = input("Digite o novo Salário: ")
salario02 = float(value)

aumentoValor = salario02 - salario01

porcentagemAumento = (aumentoValor * 100) / salario01

print("O aumento foi: " + str(porcentagemAumento))