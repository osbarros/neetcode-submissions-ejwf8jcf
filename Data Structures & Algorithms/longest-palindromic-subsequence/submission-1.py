class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        # dp[L][R] = tamanho da maior subsequência palindrômica
        # dentro do intervalo s[L:R+1]
        dp = [[0 for _ in range(n)] for _ in range(n)]

        # Caso base:
        # qualquer caractere sozinho é um palíndromo de tamanho 1
        for i in range(n):
            dp[i][i] = 1

        # Vamos calcular primeiro intervalos pequenos,
        # depois intervalos maiores
        for length in range(2, n + 1):

            for L in range(n - length + 1):
                R = L + length - 1

                # Se as pontas são iguais,
                # podemos usar ambas no palíndromo
                if s[L] == s[R]:
                    dp[L][R] = 2

                    # Só existe intervalo interno se houver
                    # pelo menos um caractere entre L e R
                    if L + 1 <= R - 1:
                        dp[L][R] += dp[L + 1][R - 1]

                else:
                    # Se as pontas são diferentes,
                    # tentamos ignorar uma delas
                    dp[L][R] = max(
                        dp[L + 1][R],
                        dp[L][R - 1]
                    )

        return dp[0][n - 1]