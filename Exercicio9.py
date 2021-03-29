value = input("Digite o preço do produto: ")
valorProduto = float(value)

value = input("Digite a % Desconto: ")
desconto = float(value)

value = input("Digite a % Acrescimo: ")
acrescimo = float(value)

PrecoFinalDesconto = valorProduto * (desconto/100)
PrecoFinalProduto = valorProduto - PrecoFinalDesconto
valorAcrescimo = valorProduto * (1 + (acrescimo /100))

print("Preço Final do Produto: " + str(PrecoFinalProduto))
print("Valor do Desconto: " + str(PrecoFinalDesconto))
print("Valor do Acréscimo: " + str(valorAcrescimo))