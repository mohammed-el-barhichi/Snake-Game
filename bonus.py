from nourriture import Nourriture

rayon_bonus=20

class BonusTaille(Nourriture):
    def __init__(self, longuer_fenetre, hauteur_fenetre):
        super().__init__(rayon_bonus,longuer_fenetre, hauteur_fenetre)
        self.disque.color=(204, 204,0)
        
class BonusScore(Nourriture):
    def __init__(self, longuer_fenetre, hauteur_fenetre):
        super().__init__(rayon_bonus,longuer_fenetre, hauteur_fenetre)
        self.disque.color=(137, 83, 141)