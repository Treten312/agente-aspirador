# Ambiente implementado como um array para que a movimentação do agente seja mais fácil de implementar
# 'L' = Limpo e 'S' = Sujo, o ambiente foi feito de acordo com a foto de exemplo da atividade
ambiente = [['L','L','S','L'],
            ['L','S','L','S'],
            ['S','L','S','L'],
            ['S','L','S','L']]

class AgenteAspirador:
    def __init__(self, energia=100):
        self.posicao = (0, 0) # Posição inicial do aspirador como 'A' = [0, 0] no array
        self.energia = energia # Energia inicial do aspirador, 100 pontos de energia
        self.bolsa = [] # Bolsa para armazenar sujeira aspirada em forma de lista

#    def verficar(self, ambiente):
#        x, y = self.posicao
#        estado = ambiente[x][y]
#        return estado
    
    def energia_atual(self): # Verificar a quantidade de energia atual
        return self.energia

    def mover(self, direcao): # Função para atualizar localização atual após se mover
        custo_mover = 1
        x, y = self.posicao
        if self.energia >= custo_mover:
            if direcao == 'Norte' and x > 0:
                x -= 1
            elif direcao == 'Sul' and x < 3:
                x += 1
            elif direcao == 'Leste' and y < 3:
                y += 1
            elif direcao == 'Oeste' and y > 0:
                y -= 1
            
            # Verifica se as coordenadas destino escolhidas estão dentro do limite do ambiente
            if 0 <= x <= 3 and 0 <= y <= 3: 
                self.localizacao = (x, y)
                self.energia -= custo_mover

    def aspirar(self, ambiente): # Função pra fazer a aspiração, como a função já verifica o estado atual da posição, se faz desnecessário a "def verificar"
        custo_aspirar = 1
        x, y = self.posicao
        if self.energia >= custo_aspirar:
            if ambiente[x][y] == 'S':
                ambiente[x][y] == 'L' # "Limpa" o ambiente, só muda o estado pra limpo mesmo 
                self.bolsa.append('Sujeira') # Adciona a "sujeira" no ambiente
                self.energia -= custo_aspirar

        