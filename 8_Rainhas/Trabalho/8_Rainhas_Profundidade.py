#/**
#* @author Ruan Moral 
#* @version 1.0
#*/


import numpy as np
import Queue
import random 
import os
import time

#/**
#* Esta classe representa um tabuleiro de xadrez
#* (Tamanho 8x8). Onde eh alem de indicar o numero de  
#* rainhas posicionadas e o design do Tabuleiro 
#* valida se as posicoes atuais sao validas
#*
#*
#*/

class Game:
    #/**
    #* Metodo construtor da classe. Onde eh criado um 
    #* tabuleiro 8x8 sem nenhuma rainha
    #*/
    
    def __init__(self):
        self.board = np.zeros((8,8))            
        self.queens = 0

    #/**
    #* Metodo interno do tabuleiro o qual retorna
    #* o desenho com as posicoes das rainhas
    #* @return Retorna o tabuleiro com a posicao das rainhas
    #*/
    def get_board(self):
        return self.board
    #/**
    #* Metodo interno do tabuleiro o qual retorna
    #* o numero atual de rainhas posicionadas
    #* @return Retorna o numero de rainhas no tabuleiro 
    #*/
    def get_queens(self):
        return self.queens

    #/**
    #* Metodo o qual insere uma rainha na posicao passada
    #* @param pos posicao(x,y) onde vai inserir a rainha
    #*/
 
    def set_queen(self,pos):
        self.board[pos[0],pos[1]] = 1.0
        self.queens +=1
    #/**
    #* Metodo o qual valida o tabuleiro verificando para cada rainha se sua linha, coluna e diagonais estao vazias 
    #* @return Retorna "VALID" se o tabulero e valido senao retorna
    #* "INVALID"
    #*/
    
    
    def validation(self):
        Rx,Ry = np.where(self.board ==1)
        flag  = "VALID"
        for i in range(Rx.shape[0]):
            x,y = Rx[i], Ry[i]
            diagonal =  np.sum(np.diag(self.board,y-x))
            antidiagonal = np.sum(np.diag(self.board[:, ::-1],8 - y -1 -x)    )
            line = np.sum(self.board,axis=0)[y]
            column = np.sum(self.board,axis =1)[x]
            s = diagonal + antidiagonal + line + column
            if s != 4.0:
                flag = "INVALID"
                break
        return flag

#/**
#* Esta classe representa a Inteligencia Artifciaial implementada.
#* (busca por Profundidade),
#* <p> Nesta classe foi criado um tabuleiro de xadrez (Classe Game)
#* e posicionado uma rainha em uma posicao gerada aleatoriamente.
#* Tambem foi implementado um metodo que gera os 
#* tabuleiros 'filhos' do tabuleiro atual, posicionado uma nova rainha
#* em uma posicao desocupada e entao verificado se a posicao e valida,
#* se for uma posicao valida entao eh inserido na pilha, senao eh 
#* descartado.
#*
#*/

class IA:
    #/**
    #* Metodo construtor da classe, onde gera um tabuleiro e posiciona
    #* uma rainha em uma posicao aleatoria. Tambem eh criado uma Pilha 
    #* vazia
    #*/
    def __init__(self):
        self.principal = Game()
        x,y = random.randint(0,7),random.randint(0, 7)
        self.principal.set_queen((x,y))    
        self.queue = Queue.LifoQueue()
    #/**
    #* Metodo que insere um novo elemento no topo da Pilha
    #* este elemento(node) representa um elemento do grafo
    #* @param node Novo elemento inserido no topo da pilha
    #*/
    def put_queue(self,node):
        self.queue.put(node)
    #/**
    #* Metodo o qual retira o elemento do topo da pilha 
    #* @return Retorna o elemento do topo da pilha, refere
    #* a uma variavel da classe Game
    #*/
    def get_queue(self):
        return self.queue.get()
    
    #/**
    #* Medoto que retorna o tabuleiro gerado inicialmente
    #* onde existe um tabuleiro vazio com uma rainha 
    #* em uma posicao aleatoria
    #* @return O Tabuleiro inicial
    #*/
    def get_principal(self):
        return self.principal.get_board()

    #/**
    #* Metodo que recebe um board e gera todos os filhos
    #* possiveis, posicionando em todas as coordenadas 
    #* vazias e entao valida se o filho criado e valido
    #* se for valido entao e inserido no topo da pilha
    #* senao e descartado
    #* @param board Tabuleiro o qual sera gerado os filhos
    #*/
    def generate_child(self,board):
        children= []
        for a in range(len(board)):
            for b in range(len(board)):
                if board[a][b] != 1.0:
                    child =  Game()
                    Rx,Ry = np.where(board == 1)
                    for i in range(Rx.shape[0]):
                        x,y= Rx[i],Ry[i]
                        child.set_queen((x,y))
                    child.set_queen((a,b))
                    if child.validation() == "VALID":
                        self.queue.put(child)

#/**
#* Metodo Main do programa. Onde e gerado um tabuleiro
#* aleatorio com a IA e entao utilizada-se da IA com o
#* metodo de busca em profundidade ate que seja 
#* posicionadas as 8 rainhas. 
#*/
if __name__ =="__main__":
    start_time = time.time()
    ia = IA()
    os.system("clear")
    print '\t8 Queens'
    print '\n Busca em Profundidade'
    print '\n\tFirst Board \n',ia.get_principal()
    end = "Unsolved" 
    ia.generate_child(ia.get_principal()) 

    while end != "Solved" :
            node = ia.get_queue()
            a = node.get_queens()
            if a == 8:
                end = "Solved"
                Solution = node.get_board()
                break
            else:
                ia.generate_child(node.get_board())
            if ia.get_queue == True :
                break
                
    if end == "Solved":
        print "\t**SOLVED**"
        print Solution
    else:
        print "UNSOLVED"

    print "\n\tTime taken:\n"
    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- %s minutes ---" % ((time.time() - start_time)/60.0))

