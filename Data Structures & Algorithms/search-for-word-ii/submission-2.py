from typing import List


class TrieNode:
    def __init__(self):
        # Marca se este nó representa o final de uma palavra válida
        self.isWord = False

        # Mapeia:
        # caractere -> próximo TrieNode
        self.children = {}


class Trie:
    def __init__(self):
        # Nó raiz não representa nenhum caractere
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        # Caminha caractere por caractere
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

        # Ao terminar a palavra, marca o último nó
        curr.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = Trie()

        # Insere todas as palavras na Trie
        for word in words:
            trie.insert(word)

        numRows = len(board)
        numColumns = len(board[0])

        # Usamos set para evitar palavras duplicadas
        wordsInBoard = set()

        # Guarda as células usadas no caminho atual da DFS
        visited = set()

        def dfs(row, column, trieNode, prefix):

            # Letra da célula atual
            char = board[row][column]

            # O trieNode recebido representa o prefixo
            # construído ANTES da célula atual.
            #
            # Se a letra atual não é filha dele,
            # nenhum caminho válido da Trie continua por aqui.
            if char not in trieNode.children:
                return

            # Avançamos na Trie exatamente uma posição.
            #
            # Não precisamos voltar à root nem procurar
            # todo o prefixo novamente.
            nextNode = trieNode.children[char]

            # Adiciona esta célula ao caminho atual
            visited.add((row, column))

            # Atualiza a palavra construída
            newPrefix = prefix + char

            # Se o nó atual marca fim de palavra,
            # encontramos uma palavra do input no board.
            if nextNode.isWord:
                wordsInBoard.add(newPrefix)

            # Explora BAIXO
            if (
                row + 1 < numRows
                and (row + 1, column) not in visited
            ):
                dfs(
                    row + 1,
                    column,
                    nextNode,
                    newPrefix
                )

            # Explora CIMA
            if (
                row - 1 >= 0
                and (row - 1, column) not in visited
            ):
                dfs(
                    row - 1,
                    column,
                    nextNode,
                    newPrefix
                )

            # Explora DIREITA
            if (
                column + 1 < numColumns
                and (row, column + 1) not in visited
            ):
                dfs(
                    row,
                    column + 1,
                    nextNode,
                    newPrefix
                )

            # Explora ESQUERDA
            if (
                column - 1 >= 0
                and (row, column - 1) not in visited
            ):
                dfs(
                    row,
                    column - 1,
                    nextNode,
                    newPrefix
                )

            # Backtracking:
            # depois de terminar este ramo,
            # libera a célula para outros caminhos.
            visited.remove((row, column))


        # Cada célula pode ser o início de uma palavra.
        for row in range(numRows):
            for column in range(numColumns):

                # Começamos sempre na root da Trie,
                # porque ainda não consumimos nenhum caractere.
                dfs(
                    row,
                    column,
                    trie.root,
                    ""
                )

        return list(wordsInBoard)