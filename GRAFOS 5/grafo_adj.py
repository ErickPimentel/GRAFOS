# -*- coding: utf-8 -*-

import copy
from math import *

class VerticeInvalidoException(Exception):
    pass


class ArestaInvalidaException(Exception):
    pass


class MatrizInvalidaException(Exception):
    pass


class Grafo:
    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'
    __maior_vertice = 0

    def __init__(self, N=[], M=[]):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
        '''
        for v in N:
            if not (Grafo.vertice_valido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = N

        if len(M) != len(N):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(N):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(N)):
            for j in range(len(N)):
                aresta = N[i] + Grafo.SEPARADOR_ARESTA + N[j]
                if not (self.aresta_valida(aresta)):
                    raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

        self.M = M

    def aresta_valida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        if not (self.existe_vertice(aresta[:i_traco])) or not (self.existe_vertice(aresta[i_traco + 1:])):
            return False

        return True

    @classmethod
    def vertice_valido(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existe_vertice(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.vertice_valido(vertice) and self.N.count(vertice) > 0

    def primeiro_vertice_aresta(self, a: str):
        return a[0:a.index(Grafo.SEPARADOR_ARESTA)]

    def segundo_vertice_aresta(self, a: str):
        return a[a.index(Grafo.SEPARADOR_ARESTA) + 1:]

    def indice_primeiro_vertice_aresta(self, a: str):
        return self.N.index(self.primeiro_vertice_aresta(a))

    def indice_segundo_vertice_aresta(self, a: str):
        return self.N.index(self.segundo_vertice_aresta(a))

    def existe_aresta(self, a: str):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.aresta_valida(self, a):
            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    if self.M[self.indice_primeiro_vertice_aresta(a)][self.indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adiciona_vertice(self, v):
        if self.vertice_valido(v):
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

            self.N.append(v)
            self.M.append([])
            for k in range(len(self.N)):
                if k != len(self.N) - 1:
                    self.M[k].append(0)
                self.M[self.N.index(v)].append(0)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adiciona_aresta(self, a):
        if self.aresta_valida(a):
            self.M[self.indice_primeiro_vertice_aresta(a)][self.indice_segundo_vertice_aresta(a)] += 1
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')

    def vertices_nao_adjacentes(self):
        lista = []
        for x in range(len(self.N)):
            for y in range(len(self.N)):
                aresta = '{}-{}'.format(self.N[x], self.N[y])
                if self.M[x][y] != '-' and self.M[x][y] == 0:
                    lista.append(aresta)
        return lista

    def ha_laco(self):
        contador = 0
        for x in self.M:
            if x[contador] >= 1:
                return True
            contador += 1
        return False

    def ha_paralelas(self):
        for x in range(len(self.N)):
            for y in range(len(self.N)):
                if self.M[x][y] != '-' and self.M[x][y] >= 2:
                    return True
        return False

    def grau(self, vertice):
        somador = 0
        for x in range(len(self.N)):
            if self.N[x] == vertice:
                for y in range(len(self.N)):
                    if self.M[x][y] != '-':
                        somador += self.M[x][y]
                    elif self.M[y][x] != '-':
                        somador += self.M[y][x]
        return somador

    def arestas_sobre_vertice(self, vertice):
        lista = []
        for x in range(len(self.N)):
            if self.N[x] == vertice:
                for y in range(len(self.N)):
                    aresta = '{}-{}'.format(self.N[x], self.N[y])
                    aresta1 = '{}-{}'.format(self.N[y], self.N[x])
                    if self.M[x][y] != '-' and self.M[x][y] > 0:
                        if self.M[x][y] != '-' and self.M[x][y] > 1:
                            for z in range(self.M[x][y]):
                                lista.append(aresta)
                        else:
                            lista.append(aresta)
                    elif self.M[y][x] != '-' and self.M[y][x] > 0:
                        if self.M[y][x] != '-' and self.M[y][x] > 1:
                            for z in range(self.M[y][x]):
                                lista.append(aresta1)
                        else:
                            lista.append(aresta1)
        return lista

    def eh_completo(self):
        for x in range(len(self.N)):
            for y in range(len(self.N)):
                if self.M[x][y] != '-' and x != y and self.M[x][y] == 0:
                    return False
        return True

    def ha_ciclo(self):
        eh_ciclo = self.__procurar_ciclo()
        identificador_bordas = 1
        if eh_ciclo is not False:
            caminho = []
            começo = eh_ciclo[-1].split(self.SEPARADOR_ARESTA)[1]
            for i in range(len(eh_ciclo) - 1, -1, -1):
                vertice = eh_ciclo[i].split(self.SEPARADOR_ARESTA)
                if vertice[0] == começo:
                    caminho.append(vertice[1] + self.SEPARADOR_ARESTA + vertice[0])
                    return caminho
                caminho.append(vertice[1] + self.SEPARADOR_ARESTA + vertice[0])
                identificador_bordas += 1
        return False

    def __procurar_ciclo(self, vertice: object = None, visitado: object = None, caminho: object = None,
                         bordas: object = None) -> object:
        if visitado is None:
            visitado = list()
        if caminho is None:
            caminho = list()
        if vertice is None:
            vertice = self.N[0]
        if bordas is None:
            bordas = []
            for i in range(len(self.N)):
                for j in range(len(self.N)):
                    if self.M[i][j] > 0:
                        for k in range(self.M[i][j]):
                            bordas.append(self.N[i] + self.SEPARADOR_ARESTA + self.N[j])
        if vertice in visitado:
            return caminho
        else:
            visitado.append(vertice)
            bordas_adjacentes = self.arestas_sobre_vertice(vertice)
            for i in bordas_adjacentes:
                if i in bordas:
                    bordas.remove(i)
                proximo = i.split(self.SEPARADOR_ARESTA)
                if proximo[0] == vertice:
                    caminho.append(vertice + self.SEPARADOR_ARESTA + proximo[1])
                    result = self.__procurar_ciclo(proximo[1], visitado, caminho, bordas)
                    if result != False:
                        return result
                    else:
                        caminho.pop()
                else:
                    if len(bordas_adjacentes) != 1:
                        caminho.append(vertice + self.SEPARADOR_ARESTA + proximo[0])
                        result = self.__procurar_ciclo(proximo[0], visitado, caminho, bordas)
                        if result != False:
                            return result
                        else:
                            caminho.pop()
        return False

    def caminho_de_comprimento_n(self, n, vertice=None, visitado=None, caminho=None, bordas=None, contador=None):
        if contador is None:
            contador = 0
        if vertice is None:
            vertice = self.N[0]
        if visitado is None:
            visitado = list()
        if bordas is None:
            bordas = []
            for i in range(len(self.N)):
                for j in range(len(self.N)):
                    if self.M[i][j] > 0:
                        for k in range(self.M[i][j]):
                            bordas.append(self.N[i] + self.SEPARADOR_ARESTA + self.N[j])
        if caminho is None:
            caminho = list()
        if vertice in visitado:
            return False
        else:
            contador += 1
            if contador == n:
                return True
            visitado.append(vertice)
            bordas_adjacentes = self.arestas_sobre_vertice(vertice)
            for i in bordas_adjacentes:
                if i in bordas:
                    bordas.remove(i)
                proximo = i.split(self.SEPARADOR_ARESTA)
                if proximo[0] == vertice:
                    caminho.append(vertice + self.SEPARADOR_ARESTA + proximo[1])
                    resultado = self.caminho_de_comprimento_n(n, proximo[1], visitado, caminho, bordas, contador)
                    if resultado:
                        return True
                    else:
                        caminho.pop()
                        contador -= 1
                else:
                    if len(bordas_adjacentes) != 1:
                        caminho.append(vertice + self.SEPARADOR_ARESTA + proximo[0])
                        resultado = self.caminho_de_comprimento_n(n, proximo[0], visitado, caminho, bordas, contador)
                        if resultado:
                            return True
                        else:
                            caminho.pop()
                            contador -= 1
        return False

    def eh_conexo(self, vertice=None, visitado=None, caminho=None, bordas=None):
        if visitado is None:
            visitado = []
        if caminho is None:
            caminho = []
        if vertice is None:
            vertice = self.N[0]
        if bordas is None:
            bordas = []
            for i in range(len(self.N)):
                for j in range(len(self.N)):
                    if self.M[i][j] != '-' and self.M[i][j] > 0:
                        for k in range(self.M[i][j]):
                            bordas.append(self.N[i] + "-" + self.N[j])
        if vertice in visitado:
            if len(visitado) == len(self.N):
                return True
            else:
                return False
        else:
            visitado.append(vertice)
            bordas_adjacentes = self.arestas_sobre_vertice(vertice)
            for i in bordas_adjacentes:
                proximo = i.split("-")
                if proximo[0] == vertice:
                    caminho.append(vertice + "-" + proximo[1])
                    if self.eh_conexo(proximo[1], visitado, caminho, bordas):
                        return True
                    else:
                        caminho.pop()
                else:
                    if len(bordas_adjacentes) != 1:
                        caminho.append(vertice + "-" + proximo[0])
                        if self.eh_conexo(proximo[0], visitado, caminho, bordas):
                            return True
                        else:
                            caminho.pop()
        return False

    def caminho_euleriano(self):
        contadorImpar = 0
        if self.eh_conexo() is False:
            return False
        for i in self.N:
            verGrau = self.grau(i)
            if verGrau % 2 != 0:
                contadorImpar += 1
                if contadorImpar > 2:
                    return False
        if contadorImpar == 1:
            return False
        return True

    def retorna_caminho_euleriano(self):
        if self.caminho_euleriano() is True:
            lista = []
            copia = copy.deepcopy(self.M)
            ultimo_valor = 0
            armazena_x = 0
            armazena_y = 0
            aresta = 0
            for x in range(len(self.N)):
                for y in range(len(self.N)):
                    aresta_valor = copia[x][y]
                    if aresta_valor != '-' and aresta_valor >= 1:
                        armazena_x = x
                        armazena_y = y
                        ultimo_valor = aresta_valor
                        aresta = '{}-{}'.format(self.N[x], self.N[y])
            while ultimo_valor > 0:
                if copia[armazena_x + 1][armazena_y] != '-' and copia[armazena_x + 1][armazena_y] > 0:
                    lista.append(aresta)
                    copia[armazena_x][armazena_y] -= 1
                    armazena_x += 1
                    ultimo_valor = copia[armazena_x][armazena_y]
                    aresta = '{}-{}'.format(self.N[armazena_x], self.N[armazena_y])
                elif copia[armazena_x][armazena_y - 1] != '-' and copia[armazena_x][armazena_y - 1] > 0:
                    lista.append(aresta)
                    copia[armazena_x][armazena_y] -= 1
                    armazena_y -= 1
                    ultimo_valor = copia[armazena_x][armazena_y]
                    aresta = '{}-{}'.format(self.N[armazena_x], self.N[armazena_y])
                elif copia[armazena_x - 1][armazena_y] != '-' and copia[armazena_x - 1][armazena_y] > 0:
                    lista.append(aresta)
                    copia[armazena_x][armazena_y] -= 1
                    armazena_x -= 1
                    ultimo_valor = copia[armazena_x][armazena_y]
                    aresta = '{}-{}'.format(self.N[armazena_x], self.N[armazena_y])
                elif copia[armazena_x - 1][armazena_y - 1] != '-' and copia[armazena_x - 1][armazena_y - 1] > 0:
                    lista.append(aresta)
                    copia[armazena_x][armazena_y] -= 1
                    armazena_x -= 1
                    armazena_y -= 1
                    ultimo_valor = copia[armazena_x][armazena_y]
                    aresta = '{}-{}'.format(self.N[armazena_x], self.N[armazena_y])
                elif copia[armazena_x][armazena_y + 1] != '-' and copia[armazena_x][armazena_y + 1] > 0:
                    lista.append(aresta)
                    copia[armazena_x][armazena_y] -= 1
                    armazena_y += 1
                    ultimo_valor = copia[armazena_x][armazena_y]
                    aresta = '{}-{}'.format(self.N[armazena_x], self.N[armazena_y])
                else:
                    lista.append(aresta)
                    copia[armazena_x][armazena_y] -= 1
                    ultimo_valor = copia[armazena_x][armazena_y]
            return lista
        return False

    def warshall(self):
        e = copy.deepcopy(self.M)
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if e[j][i] != 0:
                    for k in range(len(self.N)):
                        e[j][k] = max(e[j][k], e[i][k])
                        if e[j][k] > 1:
                            e[j][k] = 1
        return e

    def aresta_com_peso(self):
        edges = []
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if self.M[i][j] > 0:
                    for k in range(self.M[i][j]):
                        edges.append(self.N[i] + self.SEPARADOR_ARESTA + self.N[j])
        arestas = {}
        for i in edges:
            arestas[i] = 1
        return arestas

    def dijkstra(self, inicial, final):
        vertices = self.N
        aresta = self.M
        prede = {}
        peso = {}
        fechado = {}
        caminho = [final]
        vez = inicial
        possivel = self.warshall()
        terminou = False
        for i in range(len(vertices)):
            prede['{}'.format(vertices[i])] = 'null'
            peso['{}'.format(vertices[i])] = inf
            fechado['{}'.format(vertices[i])] = 0
        peso['{}'.format(inicial)] = 0
        if possivel[vertices.index(inicial)][vertices.index(final)] == 1:
            while terminou is False:
                for i in range(len(vertices)):
                    if vertices[i] == vez:
                        fechado['{}'.format(vertices[i])] = 1
                        menor = inf
                        chave = 'null'
                        for a in range(len(vertices)):
                            if aresta[i][a] > 1:
                                aresta[i][a] = 1
                            if aresta[i][a] == 1 and peso['{}'.format(vertices[a])] > peso[
                                '{}'.format(vertices[i])] + 1:
                                prede['{}'.format(vertices[a])] = vertices[i]
                                peso['{}'.format(vertices[a])] = peso['{}'.format(vertices[i])] + 1
                            if aresta[i][a] == 1 and peso['{}'.format(vertices[a])] < menor and fechado[
                                '{}'.format(vertices[a])] == 0:
                                menor = peso['{}'.format(vertices[a])]
                                chave = vertices[a]
                        if chave == 'null':
                            for j in range(len(vertices)):
                                if peso['{}'.format(vertices[j])] < menor and fechado['{}'.format(vertices[j])] == 0:
                                    menor = peso['{}'.format(vertices[j])]
                                    chave = vertices[j]
                        vez = chave
                for b in range(len(aresta)):
                    if peso['{}'.format(vertices[b])] != inf and fechado['{}'.format(vertices[b])] == 0:
                        terminou = False
                        break
                    terminou = True
            prox = prede['{}'.format(final)]
            while True:
                caminho += [prox]
                if prox == inicial:
                    break
                prox = prede['{}'.format(prox)]
            caminho = caminho[::-1]
            return caminho, len(caminho) - 1
        else:
            return "Fuel Low"

    def drone(self, ponto, recargas, carga_maxima, final):
        caminho = self.dijkstra(ponto, final)
        tamanho = []
        vetices = []
        distancias_final = []
        distancias_inicial = []
        if caminho == "Fuel Low":
            return 0, [ponto]
        elif caminho[1] <= carga_maxima:
            return caminho[1], [ponto, final]
        else:
            for a in range(len(recargas)):
                if recargas[a] != ponto:
                    if (self.dijkstra(recargas[a], final) != "Fuel Low" and self.dijkstra(ponto,
                        recargas[a]) != "Fuel Low"):
                        distancias_final += [self.dijkstra(recargas[a], final)[1]]
                        distancias_inicial += [self.dijkstra(ponto, recargas[a])[1]]

            if len(distancias_inicial) > 0 and len(distancias_final) > 0:
                if min(distancias_final) <= carga_maxima and min(distancias_inicial) <= carga_maxima:
                    for i in range(len(recargas)):
                        if recargas[i] != ponto and i > recargas.index(ponto):
                            s = self.drone(recargas[i], recargas, carga_maxima, final)
                            tamanho += [s[0] + self.dijkstra(ponto, recargas[i])[1]]
                            vetices += [s[1]]

                    for a in range(len(tamanho)):
                        if vetices[a][-1] == final:
                            while True:
                                if vetices[tamanho.index(min(tamanho))][-1] == final:  # se for o caminho mais curto
                                    return min(tamanho), vetices[tamanho.index(min(tamanho))]
                                else:
                                    del vetices[tamanho.index(min(tamanho))]
                                    del tamanho[tamanho.index(min(tamanho))]
                    return min(tamanho), vetices[tamanho.index(min(tamanho))]
            return 0, [ponto]

    def dijkstra_drone(self, inicial, final, cargaI, cargaM, recarga):
        caminho = []
        trajeto = []
        peso = []
        prime = []
        if self.dijkstra(inicial, final) == "Fuel Low":
            return "Fuel Low"
        elif self.dijkstra(inicial, final)[1] <= cargaI:
            return self.dijkstra(inicial, final)[0]

        for i in range(len(recarga)):
            peso1 = self.dijkstra(inicial, recarga[i])[1]
            if peso1 <= cargaI:
                peso += [self.drone(recarga[i], recarga, cargaM, final)[0] + peso1]
                trajeto += [self.drone(recarga[i], recarga, cargaM, final)[1]]
                prime += [recarga[i]]
        if len(trajeto) == 0:
            return "Fuel Low"
        for i in range(len(trajeto)):
            if trajeto[i][-1] == final:
                break
            elif len(trajeto) - 1 == i:
                return "Fuel Low"
        for i in range(len(trajeto)):
            if trajeto[i][0] == prime[i]:
                continue
            trajeto[i].insert(0, prime[i])
        ini = inicial
        for i in trajeto[peso.index(min(peso))]:
            caminho += self.dijkstra(ini, i)[0]
            ini = i
        for a in range(len(caminho)):
            if a == len(caminho) - 1:
                break
            if caminho[a] == caminho[a + 1]:
                del caminho[a]
        return caminho

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
        espaco = ' ' * (self.__maior_vertice)

        grafo_str = espaco + ' '

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(len(self.M)):
            grafo_str += self.N[l] + ' '
            for c in range(len(self.M)):
                grafo_str += str(self.M[l][c]) + ' '
            grafo_str += '\n'

        return grafo_str
