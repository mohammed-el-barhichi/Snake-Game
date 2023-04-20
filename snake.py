import pyglet


taille_de_cellule=20

class Snake:
    def __init__(self,longuer_fenetre, hauteur_fenetre,):
        self.tete = pyglet.shapes.Rectangle(longuer_fenetre//2,hauteur_fenetre//2, taille_de_cellule, taille_de_cellule, color=(117, 212, 129))
        self.queue = [(longuer_fenetre//2,hauteur_fenetre//2-2*taille_de_cellule),(longuer_fenetre//2,hauteur_fenetre//2-taille_de_cellule)]

    def draw(self):
        for coords in self.queue: #pour tracer la queue
            pyglet.shapes.Rectangle(coords[0],coords[1], taille_de_cellule, taille_de_cellule, color=(117, 212, 129,150)).draw()
        self.tete.draw()
    
    def bouge(self,direction):
        self.queue.append((self.tete.x,self.tete.y))
        self.tete.x += direction[0]*taille_de_cellule
        self.tete.y += direction[1]*taille_de_cellule

    def collision(self,nourriture):
        dist_x = min(
            (nourriture.disque.x - self.tete.x) ** 2,
            (nourriture.disque.x - self.tete.x - self.tete.width) ** 2,
        )
        dist_y = min(
            (nourriture.disque.y - self.tete.y) ** 2,
            (nourriture.disque.y - self.tete.y - self.tete.height) ** 2,
        )

        if (self.tete.x <= nourriture.disque.x <= self.tete.x + self.tete.width) and (
            self.tete.y <= nourriture.disque.y <= self.tete.y + self.tete.height
        ):
            return True
        elif self.tete.x <= nourriture.disque.x <= self.tete.x + self.tete.width:
            return dist_y < nourriture.disque.radius**2
        elif self.tete.y <= nourriture.disque.y <= self.tete.y + self.tete.height:
            return dist_x < nourriture.disque.radius**2
        else:
            return dist_x + dist_y < nourriture.disque.radius**2