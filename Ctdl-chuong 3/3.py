import math
import sys

class Graph():
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for column in range(dinh)]
            for row in range(dinh)]

    def inketqua(self, L, a):
        print ("đỉnh nguồn xuất phát từ: ")
        for nut in range(self.x):
            print (a," đến đỉnh ",nut, "độ dài đường đi là: ", L[nut])

    def duongdinhonhat(self, L, P):
        min = sys.maxsize
        for x in range(self.x):
            if L[x] < min and P[x] == False:
                min = L[x]
                min_index = x
        return min_index

    def timduongdi(self, a):
        L = [sys.maxsize] * self.x
        L[a] = 0
        P = [False] * self.x
        for cout in range(self.x):
            u = self.duongdinhonhat(L, P)
            P[u] = True
            for x in range(self.x):
                if self.graph[u][x] > 0 and P[x] == False and L[x] > L[u] + self.graph[u][x]:
                        L[x] = L[u] + self.graph[u][x]
        self.inketqua(L, a)
g = Graph(6)
graph = {
    'a': 0, 'b': 1, 'c': 2, 'f': 3, 'g': 4, 'z': 5
}
g.graph[graph['a']][graph['b']] = 3
g.graph[graph['a']][graph['f']] = 1
g.graph[graph['b']][graph['c']] = 7
g.graph[graph['c']][graph['z']] = 3
g.graph[graph['f']][graph['c']] = 9
g.graph[graph['f']][graph['g']] = 2
g.graph[graph['g']][graph['c']] = 3
g.graph[graph['g']][graph['z']] = 7
g.timduongdi(graph['a'])