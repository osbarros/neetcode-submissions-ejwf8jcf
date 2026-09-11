from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # minDist[i] = menor custo conhecido para conectar
        # o ponto i à MST atual.
        #
        # Começamos pelo ponto 0:
        # custo para conectar 0 = 0
        # todos os outros ainda são desconhecidos = infinito
        minDist = [float("inf")] * n
        minDist[0] = 0

        # Guarda quais pontos já entraram na MST
        visited = set()

        # Custo total da MST
        totalCost = 0

        # Precisamos adicionar exatamente n pontos à MST
        for _ in range(n):

            # -------------------------------------------------
            # 1. Encontrar o ponto NÃO visitado com menor minDist
            # -------------------------------------------------

            minValue = float("inf")
            minIndex = -1

            for i in range(n):
                if i not in visited and minDist[i] < minValue:
                    minValue = minDist[i]
                    minIndex = i

            # -------------------------------------------------
            # 2. Adicionar esse ponto à MST
            # -------------------------------------------------

            visited.add(minIndex)

            # O minValue representa o custo da aresta
            # que usamos para conectar esse ponto à MST.
            #
            # Para o primeiro ponto, o custo é 0.
            totalCost += minValue

            # -------------------------------------------------
            # 3. Atualizar os custos dos pontos ainda de fora
            # -------------------------------------------------

            # Coordenadas do ponto que acabou de entrar na MST
            x1, y1 = points[minIndex]

            for j in range(n):

                # Só precisamos olhar pontos que ainda
                # não fazem parte da MST
                if j not in visited:

                    x2, y2 = points[j]

                    # Distância de Manhattan
                    distance = abs(x1 - x2) + abs(y1 - y2)

                    # Talvez o novo ponto da MST ofereça
                    # uma conexão mais barata para j
                    minDist[j] = min(
                        minDist[j],
                        distance
                    )

        return totalCost