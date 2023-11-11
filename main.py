import random
import time

class AspiradorDePo:
    def __init__(self):
        self.energia = 100
        self.bolsa_sujeira = 0
        self.grid = [[random.choice([0, 1]) for _ in range(4)] for _ in range(4)]  # Posições aleatórias (0: limpo, 1: sujo)
        self.localizacao = [0, 0]  # Posição inicial no grid 4x4

    def mover(self, direcao):
        movimentos = {
            'Norte': (-1, 0),
            'Sul': (1, 0),
            'Leste': (0, 1),
            'Oeste': (0, -1)
        }

        movimento = movimentos[direcao]
        nova_posicao = [self.localizacao[0] + movimento[0], self.localizacao[1] + movimento[1]]

        # Verifica se a nova posição está dentro do grid 4x4
        if 0 <= nova_posicao[0] < 4 and 0 <= nova_posicao[1] < 4:
            self.energia -= 1
            self.localizacao = nova_posicao
            print(f"O agente se moveu para o {direcao.lower()}.")
        else:
            print("Movimento inválido. Escolha outra direção.")

    def aspirar(self):
        self.energia -= 1
        if self.grid[self.localizacao[0]][self.localizacao[1]] == 1:
            self.grid[self.localizacao[0]][self.localizacao[1]] = 0
            self.bolsa_sujeira += 1
            print("O agente aspirou a sujeira na posição", self.localizacao)
        else:
            print("Nada para aspirar na posição", self.localizacao)

        if self.bolsa_sujeira == 10:
            self.esvaziar_bolsa()

    def esvaziar_bolsa(self):
        self.energia -= 1
        self.bolsa_sujeira = 0
        print("Bolsa cheia! Esvaziando a bolsa na Casa (posição 0, 0)")
        self.localizacao = [0, 0]

    def mostrar_estado(self):
        print("\nEstado Atual do Grid:")
        for i in range(4):
            for j in range(4):
                if [i, j] == self.localizacao:
                    print("A", end=' ')  # Representa a posição do agente
                elif self.grid[i][j] == 1:
                    print("S", end=' ')  # Representa sujeira
                else:
                    print("L", end=' ')  # Representa limpo
            print()

        print(f"\nEnergia: {self.energia} pontos")
        print(f"Bolsa de sujeira: {self.bolsa_sujeira}/10")
        print(f"Posição Atual: ({self.localizacao[0]}, {self.localizacao[1]})")

    def acao_aleatoria(self):
        # Verifica se a posição atual está suja antes de decidir mover ou aspirar
        if self.grid[self.localizacao[0]][self.localizacao[1]] == 1:
            self.aspirar()
        else:
            acoes = ['Norte', 'Sul', 'Leste', 'Oeste']
            acao = random.choice(acoes)

            if acao == 'Norte' or acao == 'Sul' or acao == 'Leste' or acao == 'Oeste':
                self.mover(acao)

    def reiniciar(self):
        self.energia = 100
        self.bolsa_sujeira = 0
        self.grid = [[random.choice([0, 1]) for _ in range(4)] for _ in range(4)]
        self.localizacao = [0, 0]


# Função principal
def main():
    aspirador = AspiradorDePo()

    while aspirador.energia > 0:
        aspirador.mostrar_estado()
        print("-----------------")
        aspirador.acao_aleatoria()

        if aspirador.energia <= 0 or aspirador.bolsa_sujeira == 10:
            print("Energia esgotada ou bolsa cheia. Reiniciando aspirador.")
            aspirador.reiniciar()

        # Introduzindo um atraso de 10 segundos entre as ações
        time.sleep(10)

    print("Energia esgotada. Encerrando programa.")


if __name__ == "__main__":
    main()
