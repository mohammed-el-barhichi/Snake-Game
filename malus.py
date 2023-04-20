from nourriture import Nourriture

rayon_malus=40

class Malus(Nourriture):
    def __init__(self, longuer_fenetre, hauteur_fenetre):
        super().__init__(rayon_malus,longuer_fenetre, hauteur_fenetre)
        self.disque.color=(223, 45, 41)