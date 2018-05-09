import numpy as np
import Queue
import random 
import os
import time
import game

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
        self.principal = game.Game()
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
                    child =  game.Game()
                    Rx,Ry = np.where(board == 1)
                    for i in range(Rx.shape[0]):
                        x,y= Rx[i],Ry[i]
                        child.set_queen((x,y))
                    child.set_queen((a,b))
                    if child.validation() == "VALID":
                        self.queue.put(child)


