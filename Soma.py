class MaquinaSoma:
    def __init__(self,entrada):
        self.estadoatual = "q0" #faz o papel do controle
        self.cabeçote = 0       #indica a posição do cabeçote
        self.fita = self.fitas(entrada)

    def fitas(self,entrada):
        fitas = entrada.split(" ")
        if len(fitas[0]) >= len(fitas[1]):
            return ">_"+fitas[0]+"#"+fitas[1]+"____"
        else:
            return ">_"+fitas[1]+"#"+fitas[0]+"____"

    def configuração(self):
        print(self.estadoatual.ljust(5," "), self.fita[:self.cabeçote]+"["+self.fita[self.cabeçote]+"]"+self.fita[self.cabeçote+1:])

    def direita(self): 
        self.cabeçote += 1
    def esquerda(self):
        self.cabeçote -= 1
    def setestadoatual(self,novoestado):
        self.estadoatual = novoestado
    def setfita(self,pos,simb):
        self.fita = list(self.fita)
        self.fita[pos] = simb
        self.fita = "".join(self.fita)
        
    def soma(self):
        self.configuração()
        while self.estadoatual != "h":
            if self.estadoatual == "q0":
                if self.fita[self.cabeçote] == "_":
                    self.setestadoatual("q1")
                    self.direita()
                if self.fita[self.cabeçote] in ">10#XY":
                    self.direita()
            elif self.estadoatual == "q1":
                if self.fita[self.cabeçote] in "10#XY":
                    self.direita()
                elif self.fita[self.cabeçote] == "_":
                    self.setestadoatual("q2")
                    self.esquerda()
            elif self.estadoatual == "q2":
                if self.fita[self.cabeçote] == "#":
                    self.setestadoatual("q4")
                    self.esquerda()
                elif self.fita[self.cabeçote] == "0":
                    self.setestadoatual("q3")
                    self.setfita(self.cabeçote,"_")
                elif self.fita[self.cabeçote] == "1":
                    self.setestadoatual("q7")
                    self.setfita(self.cabeçote,"_")
                elif self.fita[self.cabeçote] in "_XY":
                    self.direita()
            elif self.estadoatual == "q3":
                if self.fita[self.cabeçote] in "_10XY":
                    self.esquerda()
                elif self.fita[self.cabeçote] == "#":
                    self.esquerda()
                    self.setestadoatual("q4")
            elif self.estadoatual == "q4":
                if self.fita[self.cabeçote] == "0":
                    self.setestadoatual("q1")
                    self.setfita(self.cabeçote,"Y")
                elif self.fita[self.cabeçote] == "1":
                    self.setestadoatual("q1")
                    self.setfita(self.cabeçote, "X")
                elif self.fita[self.cabeçote] in "XY#":
                    self.esquerda()
                elif self.fita[self.cabeçote] == "_":
                    self.setestadoatual("q13")
            elif self.estadoatual == "q5":
                if self.fita[self.cabeçote] in "_10XY":
                    self.esquerda()
                elif self.fita[self.cabeçote] == "#":
                    self.setestadoatual("q6")
                    self.esquerda()
            elif self.estadoatual == "q6":
                if self.fita[self.cabeçote] in "XY_#":
                    self.esquerda()
                elif self.fita[self.cabeçote] == "1":
                    self.setfita(self.cabeçote,"X")
                    self.setestadoatual("q9")
                elif self.fita[self.cabeçote] =="0":
                    self.setfita(self.cabeçote,"Y")
                    self.setestadoatual("q9")
            elif self.estadoatual == "q7":
                if self.fita[self.cabeçote] in "_10XY":
                    self.esquerda()
                elif self.fita[self.cabeçote] == "#":
                    self.setestadoatual("q8")
                    self.esquerda()
            elif self.estadoatual == "q8":
                if self.fita[self.cabeçote] == "0":
                    self.setfita(self.cabeçote, "X")
                    self.setestadoatual("q1")
                elif self.fita[self.cabeçote] == "1":
                    self.setfita(self.cabeçote,"Y")
                    self.setestadoatual("q9")
                elif self.fita[self.cabeçote] in "#YX":
                    self.esquerda()
                elif self.fita[self.cabeçote] == "_":
                    self.setestadoatual("q13")
                    self.setfita(self.cabeçote,"X")
            elif self.estadoatual == "q9":
                if self.fita[self.cabeçote] in "YX10#":
                    self.direita()
                elif self.fita[self.cabeçote] == "_":
                    self.esquerda()
                    self.setestadoatual("q10")
            elif self.estadoatual == "q10":
                if self.fita[self.cabeçote] == "0":
                    self.setestadoatual("q11")
                    self.setfita(self.cabeçote,"_")
                elif self.fita[self.cabeçote] == "1":
                    self.setestadoatual("q5")
                    self.setfita(self.cabeçote,"_")
                elif self.fita[self.cabeçote] == "#":
                    self.direita()
                elif self.fita[self.cabeçote] == "_":
                    self.setfita(self.cabeçote,"1")
                    self.setestadoatual("q1")
            elif self.estadoatual == "q11":
                if self.fita[self.cabeçote] in "_10XY":
                    self.esquerda()
                elif self.fita[self.cabeçote] == "#":
                    self.setestadoatual("q12")
            elif self.estadoatual == "q12":
                if self.fita[self.cabeçote] == "0":
                    self.setfita(self.cabeçote,"X")
                    self.setestadoatual("q1")
                elif self.fita[self.cabeçote] == "1":
                    self.setfita(self.cabeçote,"Y")
                    self.setestadoatual("q9")
                elif self.fita[self.cabeçote] in "XY#_":
                    self.esquerda()
            elif self.estadoatual == "q13":
                if self.fita[self.cabeçote] == "_":
                    self.setestadoatual("q14")
                    self.direita()
                elif self.fita[self.cabeçote] == "X":
                    self.setfita(self.cabeçote, "1")
                elif self.fita[self.cabeçote] == "Y":
                    self.setfita(self.cabeçote, "0")
                elif self.fita[self.cabeçote] == "#":
                    self.setfita(self.cabeçote,"_")
                    self.setestadoatual("h")
                elif self.fita[self.cabeçote] in "10":
                    self.direita()
            elif self.estadoatual == "q14":
                if self.fita[self.cabeçote] == "X":
                    self.setfita(self.cabeçote, "1")
                elif self.fita[self.cabeçote] == "Y":
                    self.setfita(self.cabeçote, "0")
                elif self.fita[self.cabeçote] == "#":
                    self.setfita(self.cabeçote,"_")
                    self.setestadoatual("h")
                elif self.fita[self.cabeçote] in "10":
                    self.direita()
            self.configuração() 
