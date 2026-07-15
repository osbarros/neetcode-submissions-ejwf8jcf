class Solution:

    def dfs(self, image: List[List[int]], sr: int, sc: int, color: int):

        #testa se está out of bounds e se é diferente da cor original. Return
        if sr < 0 or sc < 0 or sr > self.rowsNumber - 1 or sc > self.columnsNumber - 1 or image[sr][sc] != self.originalColor:
            return

        else:
            image[sr][sc] = color


        #modifica a cor

        self.dfs(image, sr + 1, sc, color)
        self.dfs(image, sr - 1, sc, color)
        self.dfs(image, sr, sc + 1, color)
        self.dfs(image, sr, sc - 1, color)
        #chama os vizinhos 

        
        
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.originalColor = image[sr][sc]
        self.rowsNumber = len(image)
        self.columnsNumber = len(image[0])

        if self.originalColor == color:
            return image
        
        self.dfs(image, sr, sc, color)
        return image

    

        