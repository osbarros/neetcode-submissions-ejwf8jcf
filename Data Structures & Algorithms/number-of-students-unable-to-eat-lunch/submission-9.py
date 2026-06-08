class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        deqStudents = deque(students)
        deqSand = deque(sandwiches)

        while count < len(deqStudents):
            if deqStudents[0] == deqSand[0]:
                deqStudents.popleft()
                deqSand.popleft()
                count = 0
            else:
                s = deqStudents.popleft()
                deqStudents.append(s)
                count += 1

        return len(deqStudents)


# # Define a estrutura da classe exigida pelo LeetCode para organizar a solução
# class Solution:
#     # Define a função principal que recebe as listas de estudantes e sanduíches e retorna um número inteiro
#     def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
#         
#         # Conta quantos estudantes na lista preferem o sanduíche do tipo 0 e guarda o total na variável 'count0'
#         count0 = students.count(0)
# 
#         # Conta quantos estudantes na lista preferem o sanduíche do tipo 1 e guarda o total na variável 'count1'
#         count1 = students.count(1)
# 
#         # Inicia um laço de repetição para avaliar cada sanduíche da pilha, um por um, do topo até a base
#         for sand in sandwiches:
# 
#             # Verifica se o sanduíche atual que está no topo da pilha é do tipo 0
#             if sand == 0:
# 
#                 # Se o sanduíche é do tipo 0, checa se a quantidade de alunos que querem o tipo 0 acabou (chegou a zero)
#                 if count0 == 0:
#                     # Como o sanduíche 0 está no topo e ninguém o quer, a fila trava. Retorna os alunos restantes (que querem o tipo 1)
#                     return count1
# 
#                 # Se ainda existem alunos que querem o tipo 0, um deles vai comer. Decrementa 1 da contagem desse grupo
#                 count0 -= 1
# 
#             # Entra neste bloco caso o sanduíche atual seja do tipo 1 (já que as únicas opções possíveis são 0 e 1)
#             else:
# 
#                 # Se o sanduíche é do tipo 1, checa se a quantidade de alunos que querem o tipo 1 acabou (chegou a zero)
#                 if count1 == 0:
#                     # Como o sanduíche 1 está no topo e ninguém o quer, a fila trava. Retorna os alunos restantes (que querem o tipo 0)
#                     return count0
# 
#                 # Se ainda existem alunos que querem o tipo 1, um deles vai comer. Decrementa 1 da contagem desse grupo
#                 count1 -= 1
# 
#         # Caso o laço termine sem interrupções, significa que todos os sanduíches foram consumidos com sucesso
#         # Retorna 0, indicando que nenhum estudante ficou sem almoçar
#         return 0