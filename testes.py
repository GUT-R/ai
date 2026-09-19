from ia import RedeNeural
def exibir_modelo():
    camadas = (3, 5, 2)
    rede_neural = RedeNeural(camadas)
    for i in range(len(rede_neural)):
        camada = rede_neural[i]
        print(f'[{i}] {camada}')

for i in range(10):
    print(f'----- GERAÇÂO ALEATÓRIA {i} -----')
    exibir_modelo()
    print(f'---------------------------------')