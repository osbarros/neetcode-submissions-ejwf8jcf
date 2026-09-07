class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}
    
class Trie: 
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if not c in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr




class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        wordsInBoard = set()
        numRows = len(board)
        numColumns = len(board[0])
        visited = set()
        def dfs(prefix, row, column, board):
            visited.add((row, column))
            partialResult = trie.startsWith(prefix)
            if not partialResult:
                visited.remove((row, column))
                return False
            else:
                if partialResult.isWord:
                    if prefix not in wordsInBoard:
                        wordsInBoard.add(prefix)

                if row + 1 < numRows and (row + 1, column) not in visited:
                    dfs(prefix + board[row + 1][column], row + 1, column, board)
                if row - 1 >= 0 and (row - 1, column) not in visited:
                    dfs(prefix + board[row - 1][column], row - 1, column, board)
                if column + 1 < numColumns and (row, column + 1) not in visited:
                    dfs(prefix + board[row][column + 1], row, column + 1, board)
                if column - 1 >= 0 and (row, column - 1) not in visited:
                    dfs(prefix + board[row][column - 1], row, column - 1, board)
            visited.remove((row, column))

                    
        for word in words:
            trie.insert(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board[i][j],i, j, board)
        
        return list(wordsInBoard)
        
        