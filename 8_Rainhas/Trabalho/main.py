#/**
#* @author Ruan Moral 
#* @version 1.0
#*/


import numpy as np
import Queue
import random 
import os
import time
import game
import ia

#/**
#* Metodo Main do programa. Onde e gerado um tabuleiro
#* aleatorio com a IA e entao utilizada-se da IA com o
#* metodo de busca em profundidade ate que seja 
#* posicionadas as 8 rainhas. 
#*/
if __name__ =="__main__":
    start_time = time.time()
    ia = ia.IA()
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


