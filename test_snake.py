from snake import Snake, taille_de_cellule
from nourriture import Nourriture, rayon
from bonus import BonusTaille ,BonusScore, rayon_bonus
from malus import Malus, rayon_malus

longuer_fenetre=960
hauteur_fenetre=560

def test_position_initiale():
    snake = Snake(longuer_fenetre, hauteur_fenetre)

    assert snake.tete.x == longuer_fenetre//2
    assert snake.tete.y == hauteur_fenetre//2


def test_bouge_droite():
    snake = Snake(longuer_fenetre, hauteur_fenetre)
    snake.tete.x=0
    snake.tete.y=0
    snake.bouge((1,0))

    assert snake.tete.x==20
    assert snake.tete.y==0


def test_bouge_gauche():
    snake = Snake(longuer_fenetre, hauteur_fenetre)
    snake.tete.x=20
    snake.tete.y=0
    snake.bouge((-1,0))

    assert snake.tete.x==0
    assert snake.tete.y==0


def test_bouge_haut():
    snake = Snake(longuer_fenetre, hauteur_fenetre)
    snake.tete.x=0
    snake.tete.y=0
    snake.bouge((0,1))

    assert snake.tete.x==0
    assert snake.tete.y==20


def test_bouge_bas():
    snake = Snake(longuer_fenetre, hauteur_fenetre)
    snake.tete.x=0
    snake.tete.y=20
    snake.bouge((0,-1))

    assert snake.tete.x==0
    assert snake.tete.y==0


def test_position_de_la_nourriture_dans_la_fenetre():
    nourriture=Nourriture(rayon,longuer_fenetre, hauteur_fenetre)

    assert nourriture.min_x + rayon <= nourriture.disque.x <= nourriture.max_x - rayon
    assert nourriture.min_y + rayon <= nourriture.disque.y <= nourriture.max_y - rayon


def test_position_de_la_nourriture_pas_sur_le_snake_initialement():
    nourriture=Nourriture(rayon,longuer_fenetre, hauteur_fenetre)

    assert not ((nourriture.disque.x - rayon <= longuer_fenetre//2 <= nourriture.disque.x + rayon - taille_de_cellule) and (nourriture.disque.y - rayon <= hauteur_fenetre//2 <= nourriture.disque.y + rayon - taille_de_cellule))


def test_position_du_bonus_taille_pas_sur_le_snake_initialement():
    bonus_taille=BonusTaille(longuer_fenetre, hauteur_fenetre)

    assert not ((bonus_taille.disque.x - rayon_bonus <= longuer_fenetre//2 <= bonus_taille.disque.x + rayon_bonus - taille_de_cellule) and (bonus_taille.disque.y - rayon_bonus <= hauteur_fenetre//2 <= bonus_taille.disque.y + rayon_bonus - taille_de_cellule))

def test_position_du_bonus_score_pas_sur_le_snake_initialement():
    bonus_score=BonusScore(longuer_fenetre, hauteur_fenetre)

    assert not ((bonus_score.disque.x - rayon_bonus <= longuer_fenetre//2 <= bonus_score.disque.x + rayon_bonus - taille_de_cellule) and (bonus_score.disque.y - rayon_bonus <= hauteur_fenetre//2 <= bonus_score.disque.y + rayon_bonus - taille_de_cellule))


def test_position_du_malus_pas_sur_le_snake_initialement():
    malus=Malus(longuer_fenetre, hauteur_fenetre)

    assert not ((malus.disque.x - rayon_malus <= longuer_fenetre//2 <= malus.disque.x + rayon_malus - taille_de_cellule) and (malus.disque.y - rayon_malus <= hauteur_fenetre//2 <= malus.disque.y + rayon_malus - taille_de_cellule))


def test_collision_snake_avec_la_nourriture():
    snake = Snake(longuer_fenetre, hauteur_fenetre)
    snake.tete.x=40
    snake.tete.y=40
    nourriture=Nourriture(rayon,longuer_fenetre, hauteur_fenetre)
    nourriture.disque.x=60
    nourriture.disque.y=20

    assert snake.collision(nourriture)

def test_collision_snake_avec_bonus_score():
    snake = Snake(longuer_fenetre, hauteur_fenetre)
    snake.tete.x=40
    snake.tete.y=40
    bonusScore=BonusScore(longuer_fenetre, hauteur_fenetre)
    bonusScore.disque.x=40
    bonusScore.disque.y=40

    assert snake.collision(bonusScore)

def test_collision_snake_avec_bonus_taille():
    snake = Snake(longuer_fenetre, hauteur_fenetre)
    snake.tete.x=30
    snake.tete.y=40
    bonusTaille=BonusTaille(longuer_fenetre, hauteur_fenetre)
    bonusTaille.disque.x=40
    bonusTaille.disque.y=30

    assert snake.collision(bonusTaille)

def test_collision_snake_avec_malus():
    snake = Snake(longuer_fenetre, hauteur_fenetre)
    snake.tete.x=20
    snake.tete.y=60
    malus=Malus(longuer_fenetre, hauteur_fenetre)
    malus.disque.x=40
    malus.disque.y=40

    assert snake.collision(malus)
