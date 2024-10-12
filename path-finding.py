def pathFinding():
    cidades = ["Belem", "Ananindeua", "Marituba", "Benevides"]
    ponto_inicial = None
    ponto_final = None
    i = 1

    print("Escolha o ponto de partida: ")
    for list in cidades:
            print(f"{i} - {list}")
            i = i + 1
    ponto_inicial = input()
    i = 1   
    print("Escolha o ponto de chegada: ")
    for list in cidades:
            print(f"{i} - {list}")
            i = i + 1
    ponto_final = input()

    print("Melhor rota para chegar ao seu destino")


pathFinding()




