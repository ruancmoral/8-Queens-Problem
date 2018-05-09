import numpy as np
import time
import random


def printa_cubo(cubo):
    print len(cubo)
    for x in range(len(cubo)):
        for y in range(len(cubo)):
            for z in range(len(cubo)):
                print cubo[x][y][z].get_node()


def printa_lista(lista,who):
    print "\n\t\t#####\t",who,"\t####"
    
    for l in lista:
        printa_node(l)
    

def printa_node(n):
    node = n[0].get_node()
    parent = n[1]
    print "\n\nNode\tCoord: ",node[0],"  G: ",node[1],"  H: ",node[2],"  Cost: ",node[3],"  Wall: ",node[4]
    if parent ==None:
        print "Parent Start" 
    else:
        parent = n[1].get_node()
        print "Parent\tCoord: ",parent[0],"  G: ",parent[1],"  H: ",parent[2],"  Cost: ",parent[3],"  Wall: ",parent[4]


class Node:
    def __init__(self,Cord,Obj):
        self.Cord = Cord 
        self.wall = False 
        self.weigth = random.randint(0,9)
        a = self.Cord[0] - Obj[0]
        b = self.Cord[1] - Obj[1]
        c = self.Cord[2] - Obj[2]
        self.H = int(round(np.sqrt( np.square(a) + np.square(b) + np.square(c) )))

        self.Cost =  0
        self.Parent = None
    def get_heu(self):
        return self.H 
    def set_wall(self):
        self.wall = True
    def get_wall(self):
        return self.wall
    def get_cord(self):
        return self.Cord
    def get_node(self):
        return (self.Cord,self.weigth,self.H,self.wall, self.Parent)
    def get_weigth(self):
        return self.weigth
    def set_weigth(self,weigth):
        self.weigth = weigth
    def set_Cost(self,cost):
        self.Cost = self.weigth + cost
    def set_parent(self,parent):
        self.Parent = parent
    def get_parent(self):
        return self.Parent
    

class Cube:
    def __init__(self,dim,obstacles):
        self.End = (random.randint(0,dim-1),random.randint(0,dim-1),random.randint(0,dim-1))
        self.Start = (random.randint(0,dim -1 ),random.randint(0,dim -1),random.randint(0,dim-1))
        self.Cube = []
        for x in range(dim):
            for y in range(dim):
                for z in range(dim):
                    node = Node((x,y,z),self.End)
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
        neighbor = []
        for a in (-1,0,1):
            x = a + cord[0]
            for b in (-1,0,1):
                y = b + cord[1]
                for c in (-1,0,1):
                    z = c + cord[2]
                    if (x==y and y==z):
                        pass
                    else:
                        if((x >= 0 and x < len(self.Cube)) and 
                           (y >= 0 and y < len(self.Cube)) and
                           ((z >= 0) and z < len(self.Cube))):
                             neighbor.append(self.Cube[x][y][z])
        return neighbor
    def calcula_custo(self,node,pai):
        custo = node.get_weigth()
        H = node.get_heu()
        custo = custo + H
        print "CAlculando o custo de ", node.get_cord()
        while(pai):
            if pai.get_parent() != None:
                break
            print "parent", pai.get_cord()
            weigth_pai  = pai.get_weigth()
            custo = custo + weigth_pai
            pai = pai.get_parent() 
            time.sleep(1)
       
        print "\t\tCalcula custo =", custo
        return custo
            
class A_Estrela:
    def __init__(self):
        self.open = []
        self.closed = []
    def solve(self,dim,obstacles):
        c = Cube(dim,obstacles)
        cube = c.get_cube()
        start = c.get_start()
        start = cube[start[0]][start[1]][start[2]]
        self.open.append((start,None))

        end = c.get_end()
        end = cube[end[0]][end[1]][end[2]]
        printa_cubo(cube)

        print "Start === ",start.get_node()  
        print "END  === ",end.get_node()    

        
        while(True):
            print "\n\n\n\n\t##########Inicio do WHILE ############"
            if not self.open:
                print "\n\n\n\n NO SOLUTION\n\n\n\n" 
                break
            # pega o primeiro da lista de abertos e salva na lista de fechados
            current = self.open.pop(0)
            self.closed.append(current)
            print "Current", current[0].get_node(),"\t",current
            if current ==end:
                print "Chegou no final, current = end"
            neighbors = c.get_neighborhood(current[0].get_cord()) 
            print "\nVizinhanca \t:",neighbors,"\n"
            for n in neighbors:
                n.set_parent(current[0])
                #print 'n.get_node',n.get_node()
                # so pega se nao tiver for node nao parede e nao for ele mesmo
                if n.get_wall() == False and n.get_cord() != current[0].get_cord():
                    new_node=(n,current[0])
                    custo = c.calcula_custo(n,current[0])
                    # verifica se o new_node ja ta na lista de fechado e compara os custos
                    for f in self.closed:
                        if n.get_cord() == f[0].get_cord(): 
                            print "Cordenada ja conhecida", print n.get_cord()
                            print "comparando custos:", n.get_cost()
                            if 
                    print 'new_nodenew_node '
            time.sleep(1) 
            
        

if  __name__ == "__main__":
    dim = 5
    obstacles = 0.6
    IA = A_Estrela()
    IA.solve(dim,obstacles)

