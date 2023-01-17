import pygame

WHITE = (255, 255, 255)


class Game_instance:

    def __init__(self, titre, width=1280, hidth=720, color=WHITE):
        self.titre = titre
        self.width = width
        self.hidth = hidth
        self.color = color
        self.win = pygame.display.set_mode((self.width, self.hidth))
        pygame.display.set_caption(self.titre)
        self.run = True
        self.acteurs = []
        self.players = []
        self.vivants_save = None
        self.solides_save = None

    @property
    def vivants(self):
        if self.vivants_save is not None:
            return self.vivants_save

        return filter(lambda x: x.vivant, self.acteurs)

    @property
    def solides(self):
        if self.solides_save is not None:
            return self.solides_save

        return filter(lambda x: x.solide, self.acteurs)

    def affiche_pv(self, acteur):
        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render(str(round(acteur.pv)), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (acteur.x + 10, acteur.y - 10)
        self.win.blit(text, textRect)

    def draw_game(self):
        self.win.fill(self.color)
        for acteur in self.acteurs:
            acteur.affiche()

        pygame.display.update()

    def update(self):
        for acteur in self.acteurs:
            acteur.hidden = False

        for acteur in self.acteurs:
            acteur.comportement()

        self.draw_game()

