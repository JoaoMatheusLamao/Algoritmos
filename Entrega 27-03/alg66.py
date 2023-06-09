print('')
tempo = float(input("Entre com o tempo gasto, em horas: "))
vel_media = float(input("Entre com a velocidade média: "))
distancia = tempo * vel_media
combustivel_gasto = distancia/12
print('')
print(f"Velocidade média: {vel_media}Km/h")
print(f"Tempo gasto: {tempo}h")
print(f"Distância percorrida:  {distancia}km")
print(f"Combustível gasto: {combustivel_gasto:.2f}L")