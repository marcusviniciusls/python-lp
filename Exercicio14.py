value = input("Digite o valor do IPTU a vista: ")
aVista = int(value)

value = input("Digite o valor da Parcela ")
parcela = int(value)

valorTotalParcelado = parcela * 10
valorDiferenca = valorTotalParcelado - aVista

desconto = (valorDiferenca * 100) / valorTotalParcelado

print("Para quem quiser pagar a vista terá " + str(desconto) + "% de desconto")

