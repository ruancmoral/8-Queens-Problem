import numpy as np
import time
import random


def printa_cubo(cubo):
    print len(cubo)
    for x in range(len(cubo)):
        for y in range(len(cubo)):
            for z in range(len(cubo)):
                print cubo[x][y][z].get_node()

def ordena_lista(item):
    return item[1] + item[2]
        
def printa_lista(lista,who):
    print "\n\t\t#####\t",who,"\t####"
    
    for l in lista:
        print l.get_node()
    

def printa_node(n):
    node = n.get_node()
        
    print "\n\nNode\tCoord: ",node[0],"  G: ",node[1],"  H: ",node[2],"  Cost: ",node[3],"  Wall: ",node[4]
    if parent ==None:
        print "Parent Start" 
    else:
        parent = n[1].get_node()
        print "Parent\tCoord: ",parent[0],"  G: ",parent[1],"  H: ",parent[2],"  Cost: ",parent[3],"  Wall: ",parent[4]

class Node:
    def __init__(self,Cord,Obj,weigth):
        self.Cord = Cord 
        self.wall = False 
        self.weigth = weigth
        self.H = calcula_heuristica(Cord,Obj)
        self.parent = None
        self.cost = self.weigth + self.H
    def get_parent(self):
        return self.parent
    def set_parent(self,pai):
        self.parent = pai
    def get_heu(self):
        return self.H
    def set_wall(self):
        self.wall = True
    def get_wall(self):
        return self.wall
    def get_cord(self):
        return self.Cord
    def get_node(self):
        return (self.Cord,self.weigth,self.H,self.cost,self.wall,self.parent)
    def get_weigth(self):
        return self.weigth
    def set_weigth(self,weigth):
        self.weigth = weigth
    def update_cost(self):
        self.cost = self.weigth + self.H
    def get_cost(self):
        return self.cost
class Cube:
    def __init__(self,dim,obstacles):
        self.End = (dim-1,dim-1,dim-1)
        self.Start = (0,0,0)
        self.dim = dim
        #self.End = (random.randint(0,dim-1),random.randint(0,dim-1),random.randint(0,dim-1))
        #self.Start = (random.randint(0,dim -1 ),random.randint(0,dim -1),random.randint(0,dim-1))
        self.Cube = []
        for x in range(dim):
            for y in range(dim):
                for z in range(dim):
                    weigth = random.randint(0,9)
                    node = Node((x,y,z),self.End,weigth)
                    if random.random() < obstacles :
                        if (x,y,z) != self.Start and (x,y,z) != self.End:
                            node.set_wall()
                    self.Cube.append(node)
        self.Cube = np.array(self.Cube)
        self.Cube = self.Cube.reshape(dim,dim,dim)
        # demarca o start e end como custo zero
        self.Cube[self.Start[0]][self.Start[1]][self.Start[2]].set_weigth(0)
        self.Cube[self.End[0]][self.End[1]][self.End[2]].set_weigth(0)
    def get_cube(self):
        return self.Cube
    def get_start(self):
        return self.Start
    def get_end(self):
        return self.End
    def get_neighborhood(self,cord):
        cords = cord.get_cord()
        print "Procurando vizinhanca de",cords
        neighbor = []
        neighborhood = [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)] 
        for n in neighborhood:
            x = n[0] + cords[0]
            y = n[1] + cords[1]
            z = n[2] + cords[2]
            print self.Cube.shape
            if x<0 or y<0 or z<0 or x > self.Cube.shape[0]-1 or y> self.Cube.shape[1]-1 or z > self.Cube.shape[2]-1:
                pass
            else:
                weigth = self.Cube[x][y][z].get_weigth()
                novo_node = Node((x,y,z),self.End,weigth)
                novo_node.set_parent(cord)
                #calcula_weigth(novo_node)     
                neighbor.append(novo_node)
                                
        return neighbor

def calcula_heuristica(Cord,End):
    a = Cord[0] - End[0]
    b = Cord[1] - End[1]
    c = Cord[2] - End[2]
    H = int(round(np.sqrt( np.square(a) + np.square(b) + np.square(c) ))) 
    return H    


def calcula_weigth(no):
    print "recalcula custo"
    custo_no = 0
    pai = no 
    while( pai != None):
        #print "pai.get_parent=",pai.get_node(),"custo",custo_no 
        custo_no = custo_no + pai.get_weigth()
        pai = pai.get_parent()
        #print "\tprox, pai",pai
        #time.sleep(0.2)
    #no.set_weigth(custo_no)
    #no.update_cost()
    print "\tnovo custo \t\t\t",no.get_node()
    return custo_no
       
    
class A_Estrela:
    def __init__(self):
        self.open = []
        self.closed = []
    def solve(self,dim,obstacles):
        c = Cube(dim,obstacles)
        cube = c.get_cube()

        end = c.get_end()
        end = cube[end[0]][end[1]][end[2]]
        
        # pega as cordenadas do start
        start = c.get_start()
        print start
        # pega o node de start
        start = cube[start[0]][start[1]][start[2]]
        print "n",start



        self.open.append((start,start.get_weigth(),start.get_heu(),start.get_weigth()+start.get_heu(),None))
        #printa_cubo(cube)


        print "Start === ",start.get_node()
        print "END  === ",end.get_node()
        
        while(True):
            if not self.open:
                Solution = False
                print "\n\n\n\n No solution \n\n\n\n"
                break
            current = self.open.pop(0)
            print "Current = ",current[0].get_node(),"\t", current
            if current[0].get_cord() == end.get_cord():
                Solution = True
                path = current
                print "Chegou no final, current = end"  
                break
            
            self.closed.append(current)
            new_open = []
            neighbors = c.get_neighborhood(current[0])
            print "SELF OPEN"
            for i in self.open:
                print i[0].get_node()
            print "\n\n"

            for n in neighbors:
                ja = False
                if n.get_wall() == False:
                    custo = calcula_weigth(n)
                    print "verificando neigh",n.get_node(),"custo up ==",custo



                    # se esse no ja ta no fechado ja ta otimizado
                    for f in self.closed:
                        if n.get_cord() == f[0].get_cord():
                            print "***********JA TA NO CLOSED*********"
                            ja = True        
                            break
                    if ja == True:
                        print "Break que ja TA NO CLOSED"
                        break
   
                    

                    # verifica se ta no open e compara custos 
                    for op in self.open:

                        #print "op====",op[0].get_node()
                        if n.get_cord() == op[0].get_cord():
                            #print "custo ate o neigh",n.get_node()," == ",custo
                            if custo < op[1]:
                                #pega o indice do que deve ser substiduido e entao muda
                                print "\n\n\tSUBSTITUI NOS OPENS"
                                print "n", n.get_node(), "custo novo", custo
                                print "aberto ja =",op[0].get_node(),"custo antigo = ", op[1]
            
                                index = self.open.index(op)
                                #print "index sub",index
                                self.open[index] = ((n,custo,n.get_heu(), n.get_parent()))
                                #print f,"original",op[0].get_node(), "novo",n.get_node(),"==",custo
                                #print "\t######### TEM QUE ATUALZIAR O NOVO PESO, CUSTA MENOS AGORA ##########"
                                #print "ope depois",op
                                #time.sleep(2)
                                
                            ja = True
                            break
                    if ja == True:
                        print "ja na open", n.get_node()
                    else:
                        print "adicionado no open", n.get_cord()
                        self.open.append((n,custo,n.get_heu(),n.get_parent()))
            print "NOVO OPEN"
            for i in self.open:
                print i[0].get_node()
            sorted_open = sorted(self.open, key =ordena_lista)
            print "SORTED OPEN"
            for i in sorted_open:
                print i[0].get_node(), 'custo ==',i[1]
            


        
            print "CLOSED"
            for i in self.closed:
                print i[0].get_node()
            

            #time.sleep(2)
        print "Start === ",start.get_node()
        print "END  === ",end.get_node()
        
        path = []
        current = current[0].get_node()
        print "Cur",current
        if Solution:
            while current[5] != None:
                path.append(current)
                print "path =", path
                print "cu = ",current
                current = current[5].get_node()
                print current
        path.reverse()
        for s in path:
            print s 

if  __name__ == "__main__":
    dim = 5
    obstacles = 0.1
    IA = A_Estrela()
    IA.solve(dim,obstacles)
