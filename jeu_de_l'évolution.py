import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random as rd

class point:
    
    def __init__(self,name,c):
        self.name = name
        self.c = []
            
    def create(self):
        "crée un point d'une espèce aléatoire"
        a=0
        self.c.append(a)
        "âge"
        g=rd.randint(1,2)
        self.c.append(g)
        "sexe"
        e=rd.randint(1,10)
        self.c.append(e)
        "espèce"
        p=[rd.randint(0, 50),rd.randint(0, 50)]
        self.c.append(p)
        "position"
        
        
    def m_ou_f(self):
        "caractérise le sexe du point"
        if self.c[1] == 1:
            self.c[1] = "Homme"
        elif self.c[1] == 2:
            self.c[1] = "Femme"
        else:
            self.c[1] = "Non-Binaire"
        
    def reprodution(self,a,b):
        "fonction représentant la reproduction entre deux points"
        if a.self.c[3] == b.self.c[3] and a.self.c[1] != b.self.c[1] and a.self.c[2]== b.self.c[2]:
            a1 = point("enfant",[])
            a1.create()
            
    def anniversaire(self):
        "ajoute une année au point créé"
        return(self.c[0]+1)
    
    def mort(self):
        "tue un point"
        m=rd.randint(0, 100)
        if m == 0 or self.c[0]==100:
            del(self)
            
    def différenciation(self):
        "fonction qui différencie les différentes espèces présente"
        if self.c[2]==6:
            self.c[2]="Humain"
            couleur="blue"
        if self.c[2]==1:
            self.c[2]="Aigle"
            couleur="black"
        if self.c[2]==2:
            self.c[2]="Lion"
            couleur="yellow"
        if self.c[2]==3:
            self.c[2]="Taureau"
            couleur="red"
        if self.c[2]==4:
            self.c[2]="chat"
            couleur="grey"
        if self.c[2]==5:
            self.c[2]="Chien"
            couleur="green"
        if self.c[2]==7:
            self.c[2]="Perroquet"
            couleur="orange"
        if self.c[2]==8:
            self.c[2]="Colombe"
            couleur="white"
        if self.c[2]==9:
            self.c[2]="Requin"
            couleur="purple"
        if self.c[2]==10:
            self.c[2]="dauphin"
            couleur="pink"
        return(couleur)
    

def déplacement(self):
    "Fonction qui code le déplacement de chaque point"
    k=rd.randint(1, 9)
    if k ==1:
        self.c[3][0]=self.c[3][0]-1
        self.c[3][1]=self.c[3][1]-1
    if k ==2:
        self.c[3][0]=self.c[3][0]-1
    if k ==3:
        self.c[3][0]=self.c[3][0]-1
        self.c[3][1]=self.c[3][1]+1
    if k ==4:
        self.c[3][1]=self.c[3][1]-1
    if k ==6:
        self.c[3][1]=self.c[3][1]+1
    if k ==7:
        self.c[3][0]=self.c[3][0]+1
        self.c[3][1]=self.c[3][1]-1
    if k ==8:
        self.c[3][0]=self.c[3][0]+1
    if k ==9:
        self.c[3][0]=self.c[3][0]+1
        self.c[3][1]=self.c[3][1]+1        
             
    
Alex = point("Alex",[])
Alex.create()
Alex.m_ou_f()
print(Alex.c)
temps=0
A=plt.figure(figsize=(0,50))
Liste_de_points_a_anime=[]
for i in range(50):
    "initialisation de la grille et de ses points"
    Clara = point("Clara",[])
    Clara.create()
    x=Clara.c[3][0]
    y=Clara.c[3][1]
    plt.plot(x,y,0,color=Clara.différenciation(),marker='x')
plt.show()


for i in (0,50):
    ani = animation.FuncAnimation(A, déplacement(Clara), interval = 500)
    plt.plot(x,y,i,color=Clara.différenciation(),marker='x')
plt.show



