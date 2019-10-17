from grafo_adj import *

g_l1 = Grafo([], [])
for i in ['A', 'B', 'C', 'D']:
    g_l1.adiciona_vertice(i)
for i in ['A-A', 'B-A', 'A-A']:
    g_l1.adiciona_aresta(i)

g_c = Grafo([], [])
for i in ['J', 'C', 'E', 'P']:
    g_c.adiciona_vertice(i)
for i in ['J-C', 'J-E', 'J-P', 'C-J', 'C-E', 'C-P', 'E-J', 'E-C', 'E-P', 'P-J', 'P-C', 'P-E']:
    g_c.adiciona_aresta(i)

g_p = Grafo([], [])
for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
    g_p.adiciona_vertice(i)
for i in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
    g_p.adiciona_aresta(i)

g_p_sem_paralelas = Grafo([], [])
for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
    g_p_sem_paralelas.adiciona_vertice(i)
for i in ['J-C', 'C-E', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
    g_p_sem_paralelas.adiciona_aresta(i)

print(g_l1)
print(g_l1.warshall())

print(g_c)
print(g_c.warshall())

print(g_p)
print(g_p.warshall())

print(g_p_sem_paralelas)
print(g_p_sem_paralelas.warshall())
