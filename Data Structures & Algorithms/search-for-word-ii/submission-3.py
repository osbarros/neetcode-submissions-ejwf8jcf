from typing import List


class TrieNode:
    def __init__(self):
        # Próximos caracteres possíveis
        self.children = {}

        # Só terá valor quando este nó representar
        # o final de uma palavra completa
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

        # Em vez de apenas marcar isWord = True,
        # guardamos a palavra completa no nó terminal
        curr.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = Trie()

        # Constrói a Trie com todas as palavras
        for word in words:
            trie.insert(word)

        numRows = len(board)
        numColumns = len(board[0])

        # Guarda as palavras encontradas.
        # Como usamos set, não teremos duplicatas.
        wordsInBoard = set()

        # Células usadas no caminho atual da DFS
        visited = set()

        def dfs(row, column, trieNode):

            # Letra da célula atual
            char = board[row][column]

            # Se essa letra não é um filho do nó atual da Trie,
            # então nenhum prefixo válido continua por esse caminho.
            if char not in trieNode.children:
                return

            # Avança uma posição na Trie
            nextNode = trieNode.children[char]

            # Marca a célula como usada no caminho atual
            visited.add((row, column))

            # Se esse nó terminal guarda uma palavra,
            # encontramos uma palavra completa
            if nextNode.word is not None:
                wordsInBoard.add(nextNode.word)

            # Baixo
            if (
                row + 1 < numRows
                and (row + 1, column) not in visited
            ):
                dfs(row + 1, column, nextNode)

            # Cima
            if (
                row - 1 >= 0
                and (row - 1, column) not in visited
            ):
                dfs(row - 1, column, nextNode)

            # Direita
            if (
                column + 1 < numColumns
                and (row, column + 1) not in visited
            ):
                dfs(row, column + 1, nextNode)

            # Esquerda
            if (
                column - 1 >= 0
                and (row, column - 1) not in visited
            ):
                dfs(row, column - 1, nextNode)

            # Backtracking:
            # libera essa célula para outros caminhos
            visited.remove((row, column))


        # Cada célula pode ser o início de uma palavra
        for row in range(numRows):
            for column in range(numColumns):
                dfs(row, column, trie.root)

        return list(wordsInBoard)