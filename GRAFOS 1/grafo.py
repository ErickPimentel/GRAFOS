class VerticeInvalidoException(Exception):
    pass

class ArestaInvalidaException(Exception):
    pass

class Grafo:

    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'

    def __init__(self, N=[], A={}):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma dicionário que guarda as arestas do grafo. A chave representa o nome da aresta e o valor é uma string que contém dois vértices separados por um traço.
        '''
        for v in N:
            if not(Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

        self.N = N

        for a in A:
            if not(self.arestaValida(A[a])):
                raise ArestaInvalidaException('A aresta ' + A[a] + ' é inválida')

        self.A = A

    def arestaValida(self, aresta=''):
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

        # Verifica se as arestas antes de depois do elemento separador existem no Grafo
        if not(self.existeVertice(aresta[:i_traco])) or not(self.existeVertice(aresta[i_traco+1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def existeAresta(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, aresta):
            for k in self.A:
                if aresta == self.A[k]:
                    existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        :param v: O vértice a ser adicionado
        :raises: VerticeInvalidoException se o vértice passado como parâmetro não puder ser adicionado
        '''
        if self.verticeValido(v) and not self.existeVertice(v):
            self.N.append(v)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, nome, a):
        '''
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome
        :param v: A aresta a ser adicionada
        :raises: ArestaInvalidaException se a aresta passada como parâmetro não puder ser adicionada
        '''
        if self.arestaValida(a):
            self.A[nome] = a
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')

    #2 questao letra a
    def vertices_nao_adjacentes(self):
        lista = []
        for i in self.N:
            for j in self.N:
               if (not self.existeAresta('{}-{}'.format(i, j))) and (not self.existeAresta('{}-{}'.format(j, i))):
                    lista.append('{}-{}'.format(i, j))
        return lista

    #2 questao letra b
    def ha_laco(self):
        for i in self.A.values():
            vertice = i.split(Grafo.SEPARADOR_ARESTA)
            if vertice[0] == vertice[1]:
                return True
        return False

    #2 questao letra c
    def ha_paralelas(self):
        for x in self.N:
            for y in self.N:
                contador = 0
                aresta = '{}-{}'.format(x,y)
                for aresta1 in self.A.values():
                    if aresta in aresta1:
                        contador += 1
                    if contador > 1:
                        return True
        return False

    #2 questao letra d
    def grau(self, vertice):
        contador = 0
        for aresta in self.A.values():
            if vertice in aresta:
                contador += 1
        return contador

    #2 questao detra e
    def arestas_sobre_vertice(self, vertice):
        lista = []
        for i in self.A.keys():
            aresta = self.A.get(i)
            if vertice in aresta:
                lista.append(i)
        return lista

    #2 questao letra f
    def eh_completo(self):
        for arestaI in self.N:
            for arestaJ in self.N:
                arestaIJ = '{}-{}'.format(arestaI,arestaJ)
                arestaJI = '{}-{}'.format(arestaJ, arestaI)
                if arestaI != arestaJ and arestaIJ not in self.A.values() and arestaJI not in self.A.values():
                    return False
        return True

    def __arestas(self, vertice, arestas=None):
        if arestas is None:
            arestas = self.A.values()
        return filter(lambda v: v.startswith(vertice) or v.endswith(vertice), arestas)

    #2 questao letra g
    def ha_ciclo(self):
        res = self.__procurar_ciclo()
        if res is not False:
            caminho = []
            inicio = res[-1].split(self.SEPARADOR_ARESTA)[1]
            for i in range(len(res) - 1, -1, -1):
                vertices = res[i].split(self.SEPARADOR_ARESTA)
                if vertices[0] == inicio:
                    caminho.append(vertices[1] + self.SEPARADOR_ARESTA + vertices[0])
                    return caminho
                caminho.append(vertices[1] + self.SEPARADOR_ARESTA + vertices[0])
        return False

    def __procurar_ciclo(self, vertice=None, visitados=None, caminho=None, arestas=None):
        if visitados is None:
            visitados = list()
        if caminho is None:
            caminho = list()
        if vertice is None:
            vertice = self.N[0]
        if arestas is None:
            arestas = list(self.A.values())
        if vertice in visitados:
            return caminho
        else:
            visitados.append(vertice)
            a = list(self.__arestas(vertice, arestas))
            for i in a:
                arestas.remove(i)
                proximo = i.split(self.SEPARADOR_ARESTA)
                if proximo[0] == vertice:
                    caminho.append(vertice + self.SEPARADOR_ARESTA + proximo[1])
                    resultado = self.__procurar_ciclo(proximo[1], visitados, caminho, arestas)
                    if resultado is not False:
                        return resultado
                    else:
                        caminho.pop()
                else:
                    caminho.append(vertice + self.SEPARADOR_ARESTA + proximo[0])
                    resultado = self.__procurar_ciclo(proximo[0], visitados, caminho, arestas)
                    if resultado is not False:
                        return resultado
                    else:
                        caminho.pop()
        return False

    #2 questao letra h
    def comprimento_de_tamanho_n(self, n, vertice=None, visitados=[], caminho=[], arestas=None, c=0):
        if vertice is None:
            vertice = self.N[0]
        if arestas is None:
            arestas = list(self.A.values())
        if vertice in visitados:
            return False
        else:
            c += 1
            if c == n:
                return True
            visitados.append(vertice)
            a = list(self.__arestas(vertice, arestas))
            for i in a:
                if i in arestas:
                    arestas.remove(i)
                proximo = i.split("-")
                if proximo[0] == vertice:
                    caminho.append(vertice + "-" + proximo[1])
                    resultado = self.comprimento_de_tamanho_n(n, proximo[1], visitados, caminho, arestas, c)
                    if resultado is not False:
                        return True
                    else:
                        caminho.pop()
                        c -= 1
                else:
                    caminho.append(vertice + "-" + proximo[0])
                    resultado = self.comprimento_de_tamanho_n(n, proximo[0], visitados, caminho, arestas, c)
                    if resultado is not False:
                        return True
                    else:
                        caminho.pop()
                        c -= 1
        return False

    #2 questao letra i
    def eh_conexo(self):
        if len(self.N) == 1:
            return True
        for i in self.N:
            if len(self.arestas_sobre_vertice(i)) == 0:
                return False
        return True

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''
        grafo_str = ''

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca a vírgula se não for o último vértice
                grafo_str += ", "

        grafo_str += '\n'

        for i, a in enumerate(self.A):
            grafo_str += self.A[a]
            if not(i == len(self.A) - 1): # Só coloca a vírgula se não for a última aresta
                grafo_str += ", "

        return grafo_str































