import pyglet
from snake import Snake, taille_de_cellule
from nourriture import Nourriture, rayon
import random
from bonus import BonusTaille,BonusScore, rayon_bonus
from malus import Malus, rayon_malus

dt=1/10
longuer_fenetre=960
hauteur_fenetre=560
vies=3
t1=17 #temps d'apparition des bonus_taille
t2=12 #temps d'apparition des bonus_score
t3=8 #temps d'apparition des malus

class Fenetre(pyglet.window.Window):
    def __init__(self):
        super().__init__(longuer_fenetre, hauteur_fenetre, "Snake Game")
        self.score=0
        self.score_label = pyglet.text.Label("Score : " + str(self.score),x=longuer_fenetre-20,y=hauteur_fenetre-10,anchor_x="right",anchor_y="top")
        self.vie = vies
        self.vie_label = pyglet.text.Label("Vie : " + str(self.vie),x=20,y=10,anchor_x="left",anchor_y="bottom")
        self.snake=Snake(longuer_fenetre, hauteur_fenetre)
        self.direction=(0,1)
        self.direction_choisi=True
        self.nourriture=Nourriture(rayon,longuer_fenetre, hauteur_fenetre)
        self.nourriture_encore=True
        self.compteur_des_queues_a_ajoute=0
        self.jeu_stop=True
        self.label_pause = pyglet.text.Label("(Cliquer sur ESPACE pour commencer)",font_size=20 ,x=self.width // 2,y=self.height - taille_de_cellule ,anchor_x="center",anchor_y="center",color=(0,255,255,225))
        self.label_termine = pyglet.text.Label("Jeu terminé, votre score est : " ,font_size=20 ,x=self.width // 2,y=self.height - taille_de_cellule ,anchor_x="center",anchor_y="center",color=(0,255,255,225))
        self.gameover=pyglet.text.Label("GAME OVER" ,font_size=60 ,font_name ='Times New Roman' ,x=self.width // 2,y=self.height //2 ,anchor_x="center",anchor_y="center",color=(255,255,255,255))
        self.jeu_commence=False
        self.jeu_termine=False
        self.score_total=0 #score des 3 vies
        self.bonus_taille=BonusTaille(longuer_fenetre, hauteur_fenetre)
        self.bonus_taille_encore=False
        self.bonus_score=BonusScore(longuer_fenetre, hauteur_fenetre)
        self.bonus_score_encore=False
        self.malus=Malus(longuer_fenetre, hauteur_fenetre)
        self.malus_encore=False
        self.collision_avec_malus=False
        self.coordonnees_des_objets=[[0,0,rayon],[0,0,rayon_bonus],[0,0,rayon_bonus],[0,0,rayon_malus]]
        pyglet.clock.schedule_interval(self.update1,dt) #temps de chaque deplacement
        pyglet.clock.schedule_interval(self.update2,1) #temps d'ajout du score tant que vivant
        pyglet.clock.schedule_interval(self.update3,5) #temps d'apparition de la nourriture
        pyglet.clock.schedule_interval(self.update4,t1) #temps d'apparition des bonus_taille
        pyglet.clock.schedule_interval(self.update5,t2) #temps d'apparition des bonus_score
        pyglet.clock.schedule_interval(self.update6,t3) #temps d'apparition des malus


    def on_draw(self):
        self.clear()
        self.score_label.draw()
        self.vie_label.draw()
        self.snake.draw()

        if self.nourriture_encore : #pour s'assurer que le snake n'est pas encore passé par la nourriture
            self.coordonnees_des_objets[0][0]=self.nourriture.disque.x
            self.coordonnees_des_objets[0][1]=self.nourriture.disque.y
            coords=self.coordonnees_des_objets[1:]
            self.nourriture.draw(self.snake,rayon,coords) #les coordonnees sont ceux des deux bonus et du malus

        
        if self.bonus_taille_encore:
            self.coordonnees_des_objets[1][0]=self.bonus_taille.disque.x
            self.coordonnees_des_objets[1][1]=self.bonus_taille.disque.y
            coords=self.coordonnees_des_objets[0:1]+self.coordonnees_des_objets[2:]
            self.bonus_taille.draw(self.snake,rayon_bonus,coords) #les coordonnees sont ceux de la nourriture, du bonus_score et du malus


        if self.bonus_score_encore:
            self.coordonnees_des_objets[2][0]=self.bonus_score.disque.x
            self.coordonnees_des_objets[2][1]=self.bonus_score.disque.y
            coords=self.coordonnees_des_objets[1:2]+self.coordonnees_des_objets[3:]
            self.bonus_score.draw(self.snake,rayon_bonus,coords) #les coordonnees sont ceux de la nourriture, du bonus_taille et du malus

        if self.malus_encore:
            self.coordonnees_des_objets[3][0]=self.malus.disque.x
            self.coordonnees_des_objets[3][1]=self.malus.disque.y
            coords=self.coordonnees_des_objets[:3]
            self.malus.draw(self.snake,rayon_malus,coords) #les coordonnees sont ceux de la nourriture et des bonus

        if self.jeu_stop:
            if self.jeu_termine_condition() or self.collision_avec_malus :
                if self.vie > 1 :
                    self.label_termine.text= "Score de cette partie : " + str(self.score) +" (Cliquer sur ESPACE pour continuer)"
                elif self.vie ==1 :
                    text="Score de cette partie : {}, Le score total des {} vies est : {}"
                    self.label_termine.text= text.format(self.score,str(vies + 1),str(self.score_total+int(self.score)))
                    #on ajoute self.score car le score du dernier jeu ne s'ajoute pas au score total
                self.label_termine.draw()
                self.gameover.draw()
                self.jeu_termine=True
            else :
                if self.jeu_commence:
                #pour distinguer les cas entre l'ecritue de (Cliquer sur ESPACE pour recommencer) et (Cliquer sur ESPACE pour continuer)
                    self.label_pause.text = "(Cliquer sur ESPACE pour continuer)"
                self.label_pause.draw()


    def recommence(self):
        self.score=0
        self.vie=int(self.vie)-1
        self.vie_label.text="Vie : " + str(self.vie)
        self.direction=(0,1)
        self.snake.tete = pyglet.shapes.Rectangle(longuer_fenetre//2,hauteur_fenetre//2, taille_de_cellule, taille_de_cellule, color=(255, 255, 255))
        self.compteur_des_queues_a_ajoute=len(self.snake.queue)
        self.snake.queue =[]
        self.jeu_termine = False
        self.jeu_commence=True
        self.bonus_taille_encore=False
        self.malus_encore=False
        self.bonus_score_encore=False
        self.collision_avec_malus=False
        
    def on_key_press(self, symbol, modifiers):
        if not self.jeu_termine:
            if symbol==pyglet.window.key.UP and self.direction!=(0,-1) and not self.direction_choisi :
                self.direction=(0,1)
                self.direction_choisi=True
            elif symbol==pyglet.window.key.DOWN and self.direction!=(0,1) and not self.direction_choisi :
                self.direction=(0,-1)
                self.direction_choisi=True
            elif symbol==pyglet.window.key.RIGHT and self.direction!=(-1,0) and not self.direction_choisi :
                self.direction=(1,0)
                self.direction_choisi=True
            elif symbol==pyglet.window.key.LEFT and self.direction!=(1,0) and not self.direction_choisi :
                self.direction=(-1,0)
                self.direction_choisi=True
            elif symbol==pyglet.window.key.SPACE:
                self.jeu_stop=not(self.jeu_stop)
                self.jeu_commence=True
        else :
            if symbol==pyglet.window.key.SPACE and self.vie>0:
                self.score_total+=int(self.score)
                self.recommence()
                self.jeu_stop=not(self.jeu_stop)
                
                
    def update1(self,dt):
        if self.jeu_stop:
            return None     
        if self.jeu_termine_condition():
            self.jeu_stop=True
            return None

        self.snake.bouge(self.direction)
        self.direction_choisi = False

        if self.snake.collision(self.nourriture) and self.nourriture_encore==True :
        #pour s'assurer que la taille n'augmente qu'une seule fois au moment de la collision
            self.nourriture_encore=False
            self.score = self.score+5
            self.compteur_des_queues_a_ajoute=5 #pour s'assurer que la taille augmente de 5 carrés
        else :
            if self.compteur_des_queues_a_ajoute < 1 :
                self.snake.queue.pop(0)
            else :
                self.compteur_des_queues_a_ajoute -= 1
        
        if self.snake.collision(self.bonus_taille) and self.bonus_taille_encore==True:
            self.bonus_taille_encore=False
            self.snake.queue=self.snake.queue[3:]

        if self.snake.collision(self.bonus_score) and self.bonus_score_encore:
            self.bonus_score_encore=False
            self.score = self.score +20

        if self.snake.collision(self.malus) and self.malus_encore==True:
            self.malus_encore=False
            self.jeu_stop=True
            self.collision_avec_malus=True

            
    def update2(self,dt):
        if self.jeu_stop:
            return None  
        if self.jeu_termine_condition():
            self.jeu_stop=True
            return None

        self.score+=1
        self.score_label.text = "Score : " + str(self.score)

    def update3(self,dt):
        if self.jeu_stop:
            return None   
        if self.jeu_termine_condition():
            self.jeu_stop=True
            return None

        self.nourriture.disque.x=(random.randint(self.nourriture.min_x+rayon,self.nourriture.max_x-rayon)//taille_de_cellule)*taille_de_cellule
        self.nourriture.disque.y=(random.randint(self.nourriture.min_y+rayon,self.nourriture.max_y-rayon)//taille_de_cellule)*taille_de_cellule  
        self.nourriture_encore=True

    def cinq_secondes_passe_taille(self,dt):
        self.bonus_taille_encore=False

    def update4(self,dt):
        if self.jeu_stop:
            return None     
        if self.jeu_termine_condition():
            self.jeu_stop=True
            return None
        
        pyglet.clock.schedule_once(self.cinq_secondes_passe_taille,5)
        self.bonus_taille.disque.x=(random.randint(self.bonus_taille.min_x+rayon_bonus,self.bonus_taille.max_x-rayon_bonus)//taille_de_cellule)*taille_de_cellule
        self.bonus_taille.disque.y=(random.randint(self.bonus_taille.min_y+rayon_bonus,self.bonus_taille.max_y-rayon_bonus)//taille_de_cellule)*taille_de_cellule
        self.bonus_taille_encore=True
    
    def cinq_secondes_passe_score(self,dt):
        self.bonus_score_encore=False

    def update5(self,dt):
        if self.jeu_stop:
            return None     
        if self.jeu_termine_condition():
            self.jeu_stop=True
            return None

        pyglet.clock.schedule_once(self.cinq_secondes_passe_score,5)
        self.bonus_score.disque.x=(random.randint(self.bonus_score.min_x+rayon_bonus,self.bonus_score.max_x-rayon_bonus)//taille_de_cellule)*taille_de_cellule
        self.bonus_score.disque.y=(random.randint(self.bonus_score.min_y+rayon_bonus,self.bonus_score.max_y-rayon_bonus)//taille_de_cellule)*taille_de_cellule
        self.bonus_score_encore=True

    def update6(self,dt):
        if self.jeu_stop:
            return None     
        if self.jeu_termine_condition():
            self.jeu_stop=True
            return None

        self.malus.disque.x=(random.randint(self.malus.min_x+rayon_malus,self.malus.max_x-rayon_malus)//taille_de_cellule)*taille_de_cellule
        self.malus.disque.y=(random.randint(self.malus.min_y+rayon_malus,self.malus.max_y-rayon_malus)//taille_de_cellule)*taille_de_cellule
        self.malus_encore=True
    

    def jeu_termine_condition(self):
        #snake sort de l'écran
        condition1= self.snake.tete.x + self.direction[0]*taille_de_cellule < 0 or self.snake.tete.y + self.direction[1]*taille_de_cellule < 0 or self.snake.tete.x + self.direction[0]*taille_de_cellule > longuer_fenetre - taille_de_cellule or self.snake.tete.y + self.direction[1]*taille_de_cellule > hauteur_fenetre - taille_de_cellule
        #snake superpose avec son queue
        condition2= (self.snake.tete.x,self.snake.tete.y) in self.snake.queue
        return condition1 or condition2

