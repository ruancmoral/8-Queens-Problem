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


