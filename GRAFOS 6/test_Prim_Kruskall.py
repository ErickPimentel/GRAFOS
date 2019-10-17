import unittest
from grafo_adj import *


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = Grafo([], [])
        for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
            self.g_p.adiciona_vertice(i)
        for i in [['J-C', 3], ['C-E', 7], ['C-E', 2], ['C-P', 6], ['C-P', 2], ['C-M', 5], ['C-T', 9], ['M-T', 7], ['T-Z', 4]]:
            self.g_p.adiciona_aresta(i)

        # Grafos completos
        self.g_c = Grafo([], [])
        for i in ['J', 'C', 'E', 'P']:
            self.g_c.adiciona_vertice(i)
        for i in [['J-C', 5], ['J-E', 10], ['J-P', 8], ['C-J', 9], ['C-E', 7], ['C-P', 1], ['E-J', 7], ['E-C', 4],
                  ['E-P', 6], ['P-J', 3], ['P-C', 9], ['P-E', 2]]:
            self.g_c.adiciona_aresta(i)

        self.g_c3 = Grafo([], [])
        self.g_c3.adiciona_vertice('J')

        # Grafos com laco
        self.g_l1 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l1.adiciona_vertice(i)
        for i in [['A-A', 7], ['B-A', 8], ['A-A', 10]]:
            self.g_l1.adiciona_aresta(i)

        self.g_l4 = Grafo([], [])
        self.g_l4.adiciona_vertice('D')
        self.g_l4.adiciona_aresta(['D-D', 1])

        self.g_l5 = Grafo([], [])
        for i in ['C', 'D']:
            self.g_l5.adiciona_vertice(i)
        for i in [['D-C', 5], ['C-C', 1]]:
            self.g_l5.adiciona_aresta(i)


    def test_Prim(self):
        self.assertEqual(self.g_p.Prim(), {'a1': ['J-C', 3],'a3': ['C-E', 2], 'a5': ['C-P', 2],'a6': ['C-M', 5],'a8': ['M-T', 7],'a9': ['T-Z', 4]})
        self.assertEqual(self.g_c.Prim(), {'a10': ['P-J', 3], 'a12': ['P-E', 2], 'a6': ['C-P', 1]})
        self.assertEqual(self.g_c3.Prim(), {})
        self.assertEqual(self.g_l1.Prim(), False)
        self.assertEqual(self.g_l4.Prim(), {})
        self.assertEqual(self.g_l5.Prim(), {"a1": ['D-C', 5]})


    def test_opPrim(self):
        self.assertEqual(self.g_p.opPrim(),  {'a1': ['J-C', 3], 'a3': ['C-E', 2], 'a5': ['C-P', 2], 'a6': ['C-M', 5],
                                            'a8': ['M-T', 7], 'a9': ['T-Z', 4]})
        self.assertEqual(self.g_c.opPrim(), {'a10': ['P-J', 3], 'a12': ['P-E', 2], 'a6': ['C-P', 1]})
        self.assertEqual(self.g_c3.opPrim(), {})
        self.assertEqual(self.g_l1.opPrim(), False)
        self.assertEqual(self.g_l4.opPrim(), {})
        self.assertEqual(self.g_l5.opPrim(), {"a1": ['D-C', 5]})


    def test_Kruskall(self):
        self.assertEqual(self.g_p.Kruskall(), {'a1': ['J-C', 3], 'a3': ['C-E', 2], 'a5': ['C-P', 2], 'a6': ['C-M', 5],
                                         'a8': ['M-T', 7], 'a9': ['T-Z', 4]})
        self.assertEqual(self.g_c3.Kruskall(), {})
        self.assertEqual(self.g_l1.Kruskall(), False)
        self.assertEqual(self.g_l4.Kruskall(), False)
        self.assertEqual(self.g_l5.Kruskall(), {"a1": ['D-C', 5]})


    def test_Kruskall_op(self):
        self.assertEqual(self.g_p.opKruskall(), {'a1': ['J-C', 3], 'a3': ['C-E', 2], 'a5': ['C-P', 2], 'a6': ['C-M', 5],
                                                 'a8': ['M-T', 7], 'a9': ['T-Z', 4]})
        self.assertEqual(self.g_c3.opKruskall(), {})
        self.assertEqual(self.g_l1.opKruskall(), False)
        self.assertEqual(self.g_l4.opKruskall(), False)
        self.assertEqual(self.g_l5.opKruskall(), {"a1": ['D-C', 5]})
