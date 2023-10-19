# Ambiente implementado como uma lista multidimensional para que a movimentação do agente seja mais fácil de implementar.
# 'L' = Limpo e 'S' = Sujo, o ambiente foi feito de acordo com a foto de exemplo da atividade.
ambiente = [['L','L','S','L'],
            ['L','S','L','S'],
            ['S','L','S','L'],
            ['S','L','S','L']]

class AgenteAspirador:
    def __init__(self, energia=100):
        self.localizacao = 'A' # Posição inicial do aspirador como 'A' = [0, 0] na lista
        self.energia = energia # Energia inicial do aspirador, 100 pontos de energia
        self.bolsa = [] # Bolsa para armazenar sujeira aspirada

    def mover(self, direcao):
        custo_mover = 1
        x, y = self.localizacao
        if self.energia >= custo_mover:
            if direcao == 'Norte' and x > 0:
                x -= 1
            if direcao == 'Sul' and x < 3:
                x += 1
            if direcao == 'Leste' and y < 3:
                y += 1
            if direcao == 'Oeste' and y > 0:
                y -= 1