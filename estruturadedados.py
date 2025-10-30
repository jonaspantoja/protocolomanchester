'''
FATEC - Faculdade de Tecnologia de São Paulo
Disciplina: Estrutura de Dados
PROF. Orlando Saraiva Júnior
Aluno: Jonas Pantoja 
PROVA 2 DO 2º SEMESTRE 2025
PROJETO: PROTOCOLO MANCHESTER

IMPLEMENTAR AS CLASSES REFERENTES AOS NÓS DA ÁRVORE DE DECISÃO, DAS FILAS (VAMOS PRECISAR DE 5 FILAS AO 
TODO COM BASE NA PRIORIDADE) E A ESTRUTURA DO MENU DE OPÇÕES.

'''

# Implementando a classe do nó da árvore de decisão

class NodoArvore:
    def __init__(self, pergunta=None, cor=None):
        self.pergunta = pergunta
        self.cor = cor
        self.sim = None
        self.nao = None

#Implementando a classe FIla (Serão necessárias 5 filas)

class Fila:
    def __init__(self):
        self.itens = []

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        if not self.vazia():
            return self.itens.pop(0)
        return None

    def vazia(self):
        return len(self.itens) == 0

    def tamanho(self):
        return len(self.itens)


# Utilizando um método para implementar a árvore de decisão

def montar_arvore():
    # Montagem da árvore de decisão simplificada
    raiz = NodoArvore("O paciente está respirando?")

    # Caminho "não" → vermelho
    raiz.nao = NodoArvore(cor="Vermelho")

    # Caminho "sim"
    raiz.sim = NodoArvore("O paciente está consciente?")
    raiz.sim.nao = NodoArvore(cor="Laranja")

    raiz.sim.sim = NodoArvore("O paciente está com dor intensa?")
    raiz.sim.sim.sim = NodoArvore(cor="Amarelo")
    raiz.sim.sim.nao = NodoArvore(cor="Verde")

    return raiz

# Método para realizar a triagem

def triagem(arvore):
    nodo_atual = arvore
    while nodo_atual.cor is None:
        resposta = input(f"{nodo_atual.pergunta} (s/n): ").strip().lower()
        if resposta == "s":
            nodo_atual = nodo_atual.sim
        elif resposta == "n":
            nodo_atual = nodo_atual.nao
        else:
            print("Resposta inválida. Digite apenas 's' ou 'n'.")
    return nodo_atual.cor
