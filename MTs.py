from Soma import *


class MaquinaTuring:
    def __init__(self,entrada):
        self.estadoatual = "q0" #faz o papel do controle
        self.cabeçote = 0       #indica a posição do cabeçote
        self.fita = ">"+str(entrada)+"____"

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

    def configuração(self):
        print(self.estadoatual.ljust(4," "), self.fita[:self.cabeçote]+"["+self.fita[self.cabeçote]+"]"+self.fita[self.cabeçote+1:])

    def divisão(self):
        self.configuração()
        while self.estadoatual != "h":
            if self.estadoatual == "q0":
                if self.fita[self.cabeçote] == ">":
                    self.direita()
                elif self.fita[self.cabeçote] == "0":
                    self.setestadoatual("q1")
                    self.direita()
                elif self.fita[self.cabeçote] == "1":
                    self.setestadoatual("q1")
                    self.direita()
                elif self.fita[self.cabeçote] == "_":
                    self.setestadoatual("h")
            elif self.estadoatual == "q1":
                if self.fita[self.cabeçote] == "_":
                    self.setestadoatual("q2")
                    self.esquerda()
                elif self.fita[self.cabeçote] == "1":
                    self.setestadoatual("q3")
                    self.direita()
                elif self.fita[self.cabeçote] == "0":
                    self.setestadoatual("q3")
                    self.direita()
            elif self.estadoatual == "q2":
                if self.fita[self.cabeçote] == "0":
                    self.setestadoatual("h")
                elif self.fita[self.cabeçote] == "1":
                    self.setfita(self.cabeçote,"0")
                    self.setestadoatual("h")
                elif self.fita[self.cabeçote] == "_":
                    self.direita()
            elif self.estadoatual == "q3":
                if self.fita[self.cabeçote] == "1":
                    self.direita()
                elif self.fita[self.cabeçote] == "0":
                    self.direita()
                elif self.fita[self.cabeçote] == "_":
                    self.setestadoatual("q4")
                    self.esquerda()
            elif self.estadoatual == "q4":
                if self.fita[self.cabeçote] == "0":
                    self.setestadoatual("h")
                    self.setfita(self.cabeçote,"_")
                elif self.fita[self.cabeçote] == "1":
                    self.setestadoatual("h")
                    self.setfita(self.cabeçote,"_")
                elif self.fita[self.cabeçote] == "_":
                    self.direita()
            self.configuração()
    
    def antecessor(self):
        self.configuração()
        while self.estadoatual != "h":
            if self.estadoatual == "q0":
                if self.fita[self.cabeçote] == ">":
                    self.direita()
                elif self.fita[self.cabeçote] == "0":
                    self.direita()
                elif self.fita[self.cabeçote] == "1":
                    self.direita()
                elif self.fita[self.cabeçote] == "_":
                    self.setestadoatual("q1")
                    self.esquerda()
            elif self.estadoatual == "q1":
                if self.fita[self.cabeçote] == "0":
                    self.setestadoatual("q2")
                    self.setfita(self.cabeçote,"1")
                elif self.fita[self.cabeçote] == "1":
                    self.setestadoatual("q2")
                    self.setfita(self.cabeçote,"0")
                elif self.fita[self.cabeçote] == ">":
                    self.direita()
                    self.setestadoatual("h")
                elif self.fita[self.cabeçote] == "_":
                    self.setfita(self.cabeçote,"_")
            elif self.estadoatual == "q2":
                if self.fita[self.cabeçote] == "1":
                    self.setestadoatual("q1")
                    self.esquerda()
                elif self.fita[self.cabeçote] == "0":
                    self.setestadoatual("h")
                    self.direita()
                elif self.fita[self.cabeçote] == ">":
                    self.direita()
                elif self.fita[self.cabeçote] == "_":
                    self.setfita(self.cabeçote,"_")
            self.configuração()
                    
    def sucessor(self):
        self.configuração()
        while self.estadoatual != "h":
            if self.estadoatual == "q0":
                if self.fita[self.cabeçote] == ">":
                    self.direita()
                elif self.fita[self.cabeçote] == "0":
                    self.direita()
                elif self.fita[self.cabeçote] == "1":
                    self.direita()
                elif self.fita[self.cabeçote] == "_":
                    self.setestadoatual("q1")
                    self.esquerda()
            elif self.estadoatual == "q1":
                if self.fita[self.cabeçote] == ">":
                    self.direita()
                    self.setestadoatual("q3")
                elif self.fita[self.cabeçote] == "0":
                    self.setestadoatual("h")
                    self.setfita(self.cabeçote,"1")
                elif self.fita[self.cabeçote] == "1":
                    self.setestadoatual("q2")
                    self.setfita(self.cabeçote,"0")
                elif self.fita[self.cabeçote] == "_":
                    self.setfita(self.cabeçote,"1")
                    self.setestadoatual("h")
            elif self.estadoatual == "q2":
                if self.fita[self.cabeçote] == "0":
                    self.setestadoatual("q1")
                    self.esquerda()
                elif self.fita[self.cabeçote] == "1":
                    self.setfita(self.cabeçote,"1")
                elif self.fita[self.cabeçote] == ">":
                    self.direita()
                elif self.fita[self.cabeçote] == "_":
                    self.setfita(self.cabeçote,"_")
            elif self.estadoatual == "q3":
                if self.fita[self.cabeçote] == "0":
                    self.setestadoatual("r0")
                    self.shiftright()
                elif self.fita[self.cabeçote] == "1":
                    self.setfita(self.cabeçote,"1")
                elif self.fita[self.cabeçote] == ">":
                    self.direita()
                elif self.fita[self.cabeçote] == "_":
                    self.setfita(self.cabeçote,"_")
            elif self.estadoatual == "r6":
                if self.fita[self.cabeçote] == "_":
                    self.setestadoatual("q1")
                elif self.fita[self.cabeçote] == "1":
                    self.setfita(self.cabeçote,"1")
                elif self.fita[self.cabeçote] == ">":
                    self.direita()
                elif self.fita[self.cabeçote] == "0":
                    self.setfita(self.cabeçote,"0")
            self.configuração()
            
    def shiftright(self):
        self.configuração()
        while self.estadoatual != "r6":
            if self.estadoatual == "r0":
                if self.fita[self.cabeçote] == ">":
                    self.direita()
                elif self.fita[self.cabeçote] == "0":
                    self.direita()
                elif self.fita[self.cabeçote] == "1":
                    self.direita()
                elif self.fita[self.cabeçote] == "_":
                    self.setestadoatual("r1")
                    self.esquerda()
            elif self.estadoatual == "r1":
                if self.fita[self.cabeçote] == ">":
                    self.setestadoatual("r6")
                    self.direita()
                elif self.fita[self.cabeçote] == "0":
                    self.setestadoatual("r4")
                    self.setfita(self.cabeçote,"_")
                elif self.fita[self.cabeçote] == "1":
                    self.setestadoatual("r2")
                    self.setfita(self.cabeçote,"_")
                elif self.fita[self.cabeçote] == "_":
                    self.esquerda()
            elif self.estadoatual == "r2":
                if self.fita[self.cabeçote] == ">":
                    self.direita()
                elif self.fita[self.cabeçote] == "1":
                    self.setfita(self.cabeçote,"1")
                elif self.fita[self.cabeçote] == "0":
                    self.setfita(self.cabeçote,"0")
                elif self.fita[self.cabeçote] == "_":
                    self.setestadoatual("r3")
                    self.direita()
            elif self.estadoatual == "r3":
                if self.fita[self.cabeçote] == "_":
                    self.setfita(self.cabeçote,"1")
                elif self.fita[self.cabeçote] == "1":
                    self.setestadoatual("r1")
                    self.esquerda()
                elif self.fita[self.cabeçote] == "0":
                    self.setfita(self.cabeçote,"0")
                elif self.fita[self.cabeçote] == ">":
                    self.esquerda()
            elif self.estadoatual == "r4":
                if self.fita[self.cabeçote] == "_":
                    self.setestadoatual("r5")
                    self.direita()
                elif self.fita[self.cabeçote] == "1":
                    self.setfita(self.cabeçote,"1")
                elif self.fita[self.cabeçote] == "0":
                    self.setfita(self.cabeçote,"0")
                elif self.fita[self.cabeçote] == ">":
                    self.direita()
            elif self.estadoatual == "r5":
                if self.fita[self.cabeçote] == "_":
                    self.setfita(self.cabeçote,"0")
                elif self.fita[self.cabeçote] == "0":
                    self.setestadoatual("r1")
                    self.esquerda()
                elif self.fita[self.cabeçote] == ">":
                    self.direita()
                elif self.fita[self.cabeçote] == "1":
                    self.setfita(self.cabeçote,"1")
            self.configuração()

    def shiftleft(self):
        self.configuração()
        while self.estadoatual not in ["l7"]:
            if self.estadoatual == "l0":
                if self.fita[self.cabeçote] == ">":
                    self.setestadoatual("l1")
                    self.direita()
                elif self.fita[self.cabeçote] == "0":
                    self.esquerda()
                elif self.fita[self.cabeçote] == "1":
                    self.esquerda()
                elif self.fita[self.cabeçote] == "_":
                    self.esquerda()
            elif self.estadoatual == "l1":
                if self.fita[self.cabeçote] == ">":
                    self.setestadoatual("l2")
                    self.direita()
                elif self.fita[self.cabeçote] == "1":
                    self.setestadoatual("l2")
                    self.direita()
                elif self.fita[self.cabeçote] == "0":
                    self.setestadoatual("l2")
                    self.direita()
                elif self.fita[self.cabeçote] == "_":
                    self.setestadoatual("l2")
                    self.direita()
            elif self.estadoatual == "l2":
                if self.fita[self.cabeçote] == ">":
                    self.direita()
                elif self.fita[self.cabeçote] == "1":
                    self.setfita(self.cabeçote,"_")
                    self.setestadoatual("l3")
                elif self.fita[self.cabeçote] == "0":
                    self.setfita(self.cabeçote,"_")
                    self.setestadoatual("l5")
                elif self.fita[self.cabeçote] == "_":
                    self.setestadoatual("l7")
            elif self.estadoatual == "l3":
                if self.fita[self.cabeçote] == ">":
                    self.direita()
                elif self.fita[self.cabeçote] == "1":
                    self.setfita(self.cabeçote,"1")
                elif self.fita[self.cabeçote] == "0":
                    self.setfita(self.cabeçote,"0")
                elif self.fita[self.cabeçote] == "_":
                    self.setestadoatual("l4")
                    self.esquerda()
            elif self.estadoatual == "l4":
                if self.fita[self.cabeçote] == "0":
                    self.setfita(self.cabeçote,"1")
                elif self.fita[self.cabeçote] == "1":
                    self.setestadoatual("l1")
                    self.direita()
                elif self.fita[self.cabeçote] == "_":
                    self.setfita(self.cabeçote,"1")
            elif self.estadoatual == "l5":
                if self.fita[self.cabeçote] == "_":
                    self.setestadoatual("l6")
                    self.esquerda()
            elif self.estadoatual == "l6":
                if self.fita[self.cabeçote] == "1":
                    self.setfita(self.cabeçote,"0")
                elif self.fita[self.cabeçote] == "0":
                    self.setestadoatual("l1")
                    self.direita()
                elif self.fita[self.cabeçote] == "_":
                    self.setfita(self.cabeçote,"0")
            self.configuração()


while True:
    option = input("QUAL MAQUINA VOCÊ DESEJA USAR?\n1.SOMA\n2.SUCESSOR\n3.ANTECESSOR\n4.DIVISÃO INTEIRA POR 2\n5.SAIR\n")
    if option == "1":
        cadeia = input("\nINSIRA AS CADEIAS QUE VOCÊ DESEJA SOMAR SEPARADAS POR ESPAÇO: ")
        maquina = MaquinaSoma(cadeia)
        maquina.soma()
        print()
    elif option == "2":
        cadeia = input("\nINSIRA A CADEIA: ")
        maquina = MaquinaTuring(cadeia)
        maquina.sucessor()
        print()
    elif option == "3":
        cadeia = input("\nINSIRA A CADEIA: ")
        if cadeia == "0":
            print("\n0 NÃO POSSUI ANTECESSOR NOS NUMEROS NATURAIS!!!")
        else:
            maquina = MaquinaTuring(cadeia)
            maquina.antecessor()
            print()
    elif option == "4":
        cadeia = input("\nINSIRA A CADEIA: ")
        maquina = MaquinaTuring(cadeia)
        maquina.divisão()
        print()
    elif option == "5":
        break
    else:
        print("OPÇÃO INVALIDA!!!\n")
    
