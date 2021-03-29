value = input("Digite a Nota da matéria de NAC: ")
notaNac = int(value)

value = input("Digite a Nota da matéria de AM: ")
notaAm = int(value)

value = input("Digite a Nota da matéria de PS: ")
notaPc = int(value)

media = (2*notaNac + 3*notaAm + 5*notaPc) / 10

print("A Média é: " + str(media))