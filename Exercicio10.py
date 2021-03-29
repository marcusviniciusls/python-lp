value = input("Digite a Distancia Pecorrida: ")
distancia = float(value)

value = input("Digite o tempo em segundos pecorrido: ")
segundos = float(value)

velocidadeMediaMetrosPorSegundo = distancia/segundos
velocidadeMediaKmHora = velocidadeMediaMetrosPorSegundo * 3.6

print("Velocidade Média m/s: " +str(velocidadeMediaMetrosPorSegundo))
print("Velocidade Média k/h: " +str(velocidadeMediaKmHora))