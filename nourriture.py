import pyglet
import random

taille_de_cellule=20
rayon=40

class Nourriture:
    def __init__(self,rayon,longuer_fenetre, hauteur_fenetre):
        self.rayon=rayon
        self.min_y = 0
        self.max_y = hauteur_fenetre
        self.min_x = 0
        self.max_x = longuer_fenetre
        x=(random.randint(self.min_x+self.rayon,self.max_x-self.rayon)//taille_de_cellule)*taille_de_cellule
        y=(random.randint(self.min_y+self.rayon,self.max_y-self.rayon)//taille_de_cellule)*taille_de_cellule

        #pour s'assurer que la nourriture ne tombe pas en position initiale du snake
        while x - self.rayon <= longuer_fenetre//2 <= x + self.rayon - taille_de_cellule and y - self.rayon <= hauteur_fenetre//2 <= y + self.rayon - taille_de_cellule :
            x=(random.randint(self.min_x+self.rayon,self.max_x-self.rayon)//taille_de_cellule)*taille_de_cellule
            y=(random.randint(self.min_y+self.rayon,self.max_y-self.rayon)//taille_de_cellule)*taille_de_cellule
            
        self.disque=pyglet.shapes.Circle(x,y,radius=self.rayon,color=(255, 255, 255))

    def draw(self,snake,rayon,coordonnees_des_objets):
        #pour s'assurer que la  nourriture ne tombe pas sur la tete du snake
        while ( self.disque.x - rayon <= snake.tete.x <= self.disque.x + rayon-taille_de_cellule ) and ( self.disque.y - rayon <= snake.tete.y <= self.disque.y + rayon - taille_de_cellule ): #pour s'assurer que la nourriture ne tombe pas sur la position du snake
            self.disque.x=(random.randint(self.min_x+rayon,self.max_x-rayon)//taille_de_cellule)*taille_de_cellule
            self.disque.y=(random.randint(self.min_y+rayon,self.max_y-rayon)//taille_de_cellule)*taille_de_cellule 
        #pour s'assurer que la nourriture ne tombe pas sur la queue du snake
        for coords in snake.queue:
            while ( self.disque.x - rayon <= coords[0] <= self.disque.x + rayon - taille_de_cellule ) and ( self.disque.y - rayon <= coords[1] <= self.disque.y + rayon - taille_de_cellule ): #pour s'assurer que la nourriture ne tombe pas sur la position du snake
                self.disque.x=(random.randint(self.min_x+rayon,self.max_x-rayon)//taille_de_cellule)*taille_de_cellule
                self.disque.y=(random.randint(self.min_y+rayon,self.max_y-rayon)//taille_de_cellule)*taille_de_cellule
        #pour s'assurer que  la nourriture ne tombe pas sur un bonus ou un malus et vice-versa
        for coords in coordonnees_des_objets:
            autre_rayon= coords[2]
            while ( coords[0] - (rayon + autre_rayon) <= self.disque.x <= coords[0] + rayon + autre_rayon ) and ( coords[1] - (rayon + autre_rayon) <= self.disque.y <= coords[1] + rayon + autre_rayon ): #pour s'assurer que la nourriture ne tombe pas sur la position du snake
                self.disque.x=(random.randint(self.min_x+rayon,self.max_x-rayon)//taille_de_cellule)*taille_de_cellule
                self.disque.y=(random.randint(self.min_y+rayon,self.max_y-rayon)//taille_de_cellule)*taille_de_cellule
        
        self.disque.draw()