import copy


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
                '''
                Verifica se os índices passados como parâmetro representam um elemento da matriz abaixo da diagonal principal.
                Além disso, verifica se o referido elemento é um traço "-". Isso indica que a matriz é não direcionada e foi construída corretamente.
                '''
                if i > j and not (M[i][j] == '-'):
                    raise MatrizInvalidaException('A matriz não representa uma matriz não direcionada')

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

    def __primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice X
        :param a: a aresta a ser analisada
        :return: O primeiro vértice da aresta
        '''
        return a[0:a.index(Grafo.SEPARADOR_ARESTA)]

    def __segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice Y
        :param a: A aresta a ser analisada
        :return: O segundo vértice da aresta
        '''
        return a[a.index(Grafo.SEPARADOR_ARESTA) + 1:]

    def __indice_primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice X na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do primeiro vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__primeiro_vertice_aresta(a))

    def __indice_segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice Y na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do segundo vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__segundo_vertice_aresta(a))

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
                    if self.M[self.__indice_primeiro_vertice_aresta(a)][self.__indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adiciona_vertice(self, v):
        '''
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser incluído no grafo.
        :raises VerticeInvalidoException se o vértice já existe ou se ele não estiver no formato válido.
        '''
        if v in self.N:
            raise VerticeInvalidoException('O vértice {} já existe'.format(v))

        if self.vertice_valido(v):
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

            self.N.append(v)  # Adiciona vértice na lista de vértices
            self.M.append([])  # Adiciona a linha

            for k in range(len(self.N)):
                if k != len(self.N) - 1:
                    self.M[k].append(0)  # adiciona os elementos da coluna do vértice
                    self.M[self.N.index(v)].append('-')  # adiciona os elementos da linha do vértice
                else:
                    self.M[self.N.index(v)].append(0)  # adiciona um zero no último elemento da linha
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adiciona_aresta(self, a):
        '''
        Adiciona uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.aresta_valida(a):
            i_a1 = self.__indice_primeiro_vertice_aresta(a)
            i_a2 = self.__indice_segundo_vertice_aresta(a)
            if i_a1 < i_a2:
                self.M[i_a1][i_a2] += 1
            else:
                self.M[i_a2][i_a1] += 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def remove_aresta(self, a):
        '''
        Remove uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.aresta_valida(a):
            i_a1 = self.__indice_primeiro_vertice_aresta(a)
            i_a2 = self.__indice_segundo_vertice_aresta(a)
            if i_a1 < i_a2:
                self.M[i_a1][i_a2] -= 1
            else:
                self.M[i_a2][i_a1] -= 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

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
        return lista[::-1]

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

    @property
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
                if copia[armazena_x+1][armazena_y] != '-' and copia[armazena_x+1][armazena_y] > 0:
                    lista.append(aresta)
                    copia[armazena_x][armazena_y] -= 1
                    armazena_x += 1
                    ultimo_valor = copia[armazena_x][armazena_y]
                    aresta = '{}-{}'.format(self.N[armazena_x], self.N[armazena_y])
                elif copia[armazena_x][armazena_y-1] != '-' and copia[armazena_x][armazena_y-1] > 0:
                    lista.append(aresta)
                    copia[armazena_x][armazena_y] -= 1
                    armazena_y -= 1
                    ultimo_valor = copia[armazena_x][armazena_y]
                    aresta = '{}-{}'.format(self.N[armazena_x], self.N[armazena_y])
                elif copia[armazena_x-1][armazena_y] != '-' and copia[armazena_x-1][armazena_y] > 0:
                    lista.append(aresta)
                    copia[armazena_x][armazena_y] -= 1
                    armazena_x -= 1
                    ultimo_valor = copia[armazena_x][armazena_y]
                    aresta = '{}-{}'.format(self.N[armazena_x], self.N[armazena_y])
                elif copia[armazena_x-1][armazena_y-1] != '-' and copia[armazena_x-1][armazena_y-1] > 0:
                    lista.append(aresta)
                    copia[armazena_x][armazena_y] -= 1
                    armazena_x -= 1
                    armazena_y -= 1
                    ultimo_valor = copia[armazena_x][armazena_y]
                    aresta = '{}-{}'.format(self.N[armazena_x], self.N[armazena_y])
                elif copia[armazena_x][armazena_y+1] != '-' and copia[armazena_x][armazena_y+1] > 0:
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
