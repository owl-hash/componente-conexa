class Grafo(object):
    def __init__(grafo, path=''):
        grafo._adj = []
        grafo._vertices = 1
        grafo._arestas = 0
        
        for i in range(grafo._vertices):
            grafo._adj.append([])
            with open(path, 'r') as arquivo:
                grafo._vertices = int(arquivo.readline().rstrip('\n'))
                
                for j in range(grafo._vertices):
                    grafo._adj.append([])
                
                grafo._arestas = int(arquivo.readline().rstrip('\n'))

                for k in range(grafo._arestas):
                    linha = arquivo.readline().rstrip('\n')
                    a, b = linha.split()
                    grafo._adj[int(a)].append(int(b))
                    grafo._adj[int(b)].append(int(a))

    def obterVertice(grafo):
        return grafo._vertices
    
    def obterAdj(grafo, v):
        return grafo._adj[v]
    
    def obterAresta(grafo):
        return grafo._aresta
    
class ComponentesConexas(object):
    def __init__(componenteConexa, grafo):
        componenteConexa._contador = 0
        componenteConexa._marcado = []
        componenteConexa._id = []

        for i in range(grafo.obterVertice()):
            componenteConexa._id.append(-1)
            componenteConexa._marcado.append(False)

        for i in range(grafo.obterVertice()):
            if not componenteConexa._marcado[i]:
                componenteConexa.buscaEmProfundidade(grafo, i)
                componenteConexa._contador = 1 + componenteConexa._contador

    def buscaEmProfundidade(componenteConexa, grafo, vertice):
        componenteConexa._marcado[vertice] = True
        componenteConexa._id[vertice] = componenteConexa._contador
        for i in grafo.obterAdj(vertice):
            if not componenteConexa._marcado[i]:
                componenteConexa.buscaEmProfundidade(grafo, i)

    def obterIdentificacao(componenteConexa, v):
        return componenteConexa._id[v]

    def obterComponentes(componenteConexa):
        return componenteConexa._contador

if __name__ == '__main__':
    grafo = Grafo('cenario3.txt')
    componenteConexa = ComponentesConexas(grafo)
    numeroComponentes = componenteConexa.obterComponentes()
    numeroVertice = grafo.obterVertice()
    componentes = []
    tabela = {}
    arquivo = open("tabela.txt", "w")
    
    for i in range(numeroComponentes):
        componentes.append([])

    for i in range(numeroVertice):
        componenteDeV = componenteConexa.obterIdentificacao(i)
        componentes[componenteDeV].append(i)
    
    for i in range(numeroComponentes):
        tamanho = len(componentes[i])
        if tamanho in tabela:
            tabela[tamanho] = 1 + tabela[tamanho]
        else:
            tabela[tamanho] = 1

    arquivo.write("Tabela de componentes\n\n")
    
    for i in sorted(tabela):
        tamanho = i
        quantidadeComponentes = tabela[i]
        if quantidadeComponentes == 1:
            arquivo.write(f'{quantidadeComponentes} componente de tamanho {tamanho}\n')
        else:
           arquivo.write(f'{quantidadeComponentes} componentes de tamanho {tamanho}\n')
    
    arquivo.write("\nTotal de: " + str(numeroComponentes) + " componentes")
    arquivo.close()