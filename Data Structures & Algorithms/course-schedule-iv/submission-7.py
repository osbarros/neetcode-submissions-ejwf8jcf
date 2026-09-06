from collections import defaultdict
from typing import List

class Solution:

    def dfs(self, courses, course):

        # Se eu já calculei todos os cursos alcançáveis
        # a partir deste course, não preciso calcular novamente.
        if course in self.calculated:
            return self.reachable[course]

        # Marca que vamos calcular reachable[course] agora.
        self.calculated.add(course)

        # Percorre todos os vizinhos diretos deste curso.
        for neighbor in courses[course]:

            # Se course -> neighbor,
            # então neighbor é diretamente alcançável por course.
            self.reachable[course].add(neighbor)

            # Descobre tudo que o neighbor consegue alcançar.
            reachable_from_neighbor = self.dfs(courses, neighbor)

            # Se:
            #
            # course -> neighbor
            # neighbor -> X
            #
            # então:
            #
            # course -> X
            #
            # Portanto adicionamos todos os alcançáveis
            # do neighbor aos alcançáveis do course.
            self.reachable[course].update(reachable_from_neighbor)

        # Depois de percorrer todos os vizinhos,
        # reachable[course] está completo.
        return self.reachable[course]


    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]]
    ) -> List[bool]:

        # Monta o grafo.
        #
        # [a, b] significa:
        # a é prerequisite de b
        #
        # portanto:
        #
        # a -> b
        courses = defaultdict(list)

        for prereq in prerequisites:
            courses[prereq[0]].append(prereq[1])


        # reachable[A] conterá todos os cursos
        # que podem ser alcançados a partir de A.
        #
        # Exemplo:
        #
        # 1 -> 3 -> 0 -> 2
        #
        # reachable[1] = {3, 0, 2}
        # reachable[3] = {0, 2}
        # reachable[0] = {2}
        self.reachable = defaultdict(set)


        # Guarda quais cursos já tiveram seu reachable
        # completamente calculado.
        self.calculated = set()


        # Calcula reachable para cada curso.
        #
        # A ordem numérica NÃO importa.
        for course in range(numCourses):
            self.dfs(courses, course)


        answer = []

        # Agora responder uma query não exige DFS.
        #
        # [A, B]:
        # basta verificar se B está entre os cursos
        # alcançáveis por A.
        for query in queries:
            courseA = query[0]
            courseB = query[1]

            answer.append(
                courseB in self.reachable[courseA]
            )

        return answer