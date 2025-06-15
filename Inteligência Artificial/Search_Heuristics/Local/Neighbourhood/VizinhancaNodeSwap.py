import math
from Solucao import Solucao
from Local.Neighbourhood.Vizinhanca import Vizinhanca

class VizinhancaNodeSwap(Vizinhanca):
    def __init__(self, distancias: tuple[tuple[int]]):
        super().__init__("nodeswap", distancias, 2)  # qtd_trocas = 2 para refletir a troca de 2 cidades

    # Método que computa a qualidade da solução vizinha após um Node Swap
    def computar_qualidade(self, solucao: Solucao, i: int, j: int) -> int:
        qualidade = solucao.qualidade
        elemento_pre_i, elemento_i, elemento_pos_i, elemento_pre_j, elemento_j, elemento_pos_j = solucao.retornar_elementos(i, j)

        # Cálculo da mudança de qualidade ao trocar dois nós
        if abs(i - j) == 1:  # Se os nós forem vizinhos
            qualidade += - self.distancias[elemento_pre_i][elemento_i] - self.distancias[elemento_j][elemento_pos_j] \
                         + self.distancias[elemento_pre_i][elemento_j] + self.distancias[elemento_i][elemento_pos_j]
        else:  # Se os nós não forem vizinhos
            qualidade += - (self.distancias[elemento_pre_i][elemento_i] + self.distancias[elemento_i][elemento_pos_i] +
                            self.distancias[elemento_pre_j][elemento_j] + self.distancias[elemento_j][elemento_pos_j]) \
                         + (self.distancias[elemento_pre_i][elemento_j] + self.distancias[elemento_j][elemento_pos_i] +
                            self.distancias[elemento_pre_j][elemento_i] + self.distancias[elemento_i][elemento_pos_j])
        
        return qualidade

    # Aplica a troca de dois nós (i e j) no ciclo
    @staticmethod
    def gerar_novo_ciclo(solucao: Solucao, i: int, j: int) -> list:
        novo_ciclo = solucao.ciclo[:]
        novo_ciclo[i], novo_ciclo[j] = novo_ciclo[j], novo_ciclo[i]  # Faz a troca dos nós
        return novo_ciclo

    # Retorna a melhor solução da vizinhança
    def melhor_vizinho(self, solucao: Solucao, tabu: set) -> Solucao:
        melhor_qualidade = math.inf
        imelhor = -1
        jmelhor = -1
        for i in range(self.tamanho-1):
            if solucao.ciclo[i] not in tabu:
                for j in range(i+1, self.tamanho-1):
                    if solucao.ciclo[j] not in tabu:
                        qualidade = self.computar_qualidade(solucao, i, j)
                        if qualidade < melhor_qualidade:
                            melhor_qualidade = qualidade
                            imelhor = i
                            jmelhor = j
        return Solucao(melhor_qualidade, self.gerar_novo_ciclo(solucao, imelhor, jmelhor), solucao.ciclo[imelhor], solucao.ciclo[jmelhor])

    # Retorna o primeiro vizinho que seja melhor que a solução atual
    # Retorna a solução atual se nenhum vizinho for melhor
    def primeiro_vizinho_melhor(self, solucao: Solucao, tabu: set) -> Solucao:
        melhor_qualidade = solucao.qualidade
        for i in range(self.tamanho-1):
            if solucao.ciclo[i] not in tabu:
                for j in range(i+1, self.tamanho-1):
                    if solucao.ciclo[j] not in tabu:
                        qualidade = self.computar_qualidade(solucao, i, j)
                        if qualidade < melhor_qualidade:
                            return Solucao(qualidade, self.gerar_novo_ciclo(solucao, i, j), i, j)
        return solucao
