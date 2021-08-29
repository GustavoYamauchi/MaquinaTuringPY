class Maquina:

    def __init__(self, alfabeto, estados):
        self.alfabeto = alfabeto
        self.estados = estados
        self.posCabecote = 0
        self.fita = []
        self.saidas = []

    # Func para rodar a MT
    def start(self, entradas):
        saidas = []
        for teste in entradas:
            self.posCabecote = 0
            self.fita = [letra for letra in teste]
            print(saidas)
            saidas.append(f'{teste}: {self.leitura(0)}')

        return saidas

    # Func executa a leitura
    def leitura(self, estado):
        print(self.fita)
        print(self.posCabecote)

        if len(self.fita) - 1 < self.posCabecote:
            self.fita.append('-')

        item = self.fita[self.posCabecote]
        
        proxEstado = self.procurarItem(item, estado)

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
        for transicao in self.estados[estado]:
            if transicao[1] == item:
                self.escrever(transicao[2])
                self.moverCabecote(transicao[3])
                return int(transicao[4]) - 1
        
        return -1 






