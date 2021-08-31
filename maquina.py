class Maquina:

    # Init da class
    def __init__(self, alfabeto, estados):
        self.alfabeto = [letra for letra in alfabeto] + ['-'] # Loop para montar o alfabeto em uma list com o elemento vazio
        self.estados = estados
        self.posCabecote = 0
        self.fita = []
        self.saidas = []

    # Func para rodar a MT
    def start(self, entradas):
        saidas = []

        # Percorre todas as linhas de teste
        for teste in entradas:
            self.posCabecote = 0
            self.fita = [letra for letra in teste] #Loop para separar o teste em uma list, assim ficando mais facil de se trabalhar com os elementos
            saidas.append(f'{teste}: {self.leitura(0)}')

        return saidas

    # Func executa a leitura
    def leitura(self, estado):
        # Verificação para fazer uma fita com tamanho dinamico, sempre colocando um espaço vazio no final
        if len(self.fita) - 1 < self.posCabecote:
            self.fita.append('-')

        # Faz a leitura do elemento atual da fita
        item = self.fita[self.posCabecote] 
        
        # Procura qual será o proximo estado
        proxEstado = self.procurarItem(item, estado) 

        # Verificação para saber se a maquina precisa Aceitar, Rejeitar ou continuar rodando
        if proxEstado == -1:
            return "not OK"
        elif proxEstado == 4:
            return "OK"
        else:
            return self.leitura(proxEstado)


    # Func escreve na fita
    def escrever(self, itemEscrever):
        self.fita[self.posCabecote] = itemEscrever

    # Func para mover o cabeçote
    def moverCabecote(self, movimento):
        if movimento == "D":
            self.posCabecote += 1
        else:
            self.posCabecote -= 1 

    # Func para procurar uma transição entre as disponiveis
    def procurarItem(self, item, estado):
        # Verificação de se o elemento é um dos elementos do alfabeto
        if self.alfabeto.count(item) > 0:
            # Loop para achar qual será o proximo estado de acordo com o elemento
            for transicao in self.estados[estado]:
                if transicao[1] == item:
                    self.escrever(transicao[2])
                    self.moverCabecote(transicao[3])
                    return int(transicao[4]) - 1 # Retorna o proximo estado
                    
        return -1 # Retorna -1 se não encontar um elemento valido ou um proximo estado






