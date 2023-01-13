import pygame


class Game_instance:
    def __init__(self, titre, width, hidth):
        self.titre = titre
        self.width = width
        self.hidth = hidth
        self.win = pygame.display.set_mode((self.width, self.hidth))
        pygame.display.set_caption(self.titre)
        self.run = True
        self.player = []
        self.size_playerX = 20
        self.size_playerY = 20
        self.mechant = []
        self.size_mechantX = 40
        self.size_mechantY = 40
        self.buisson = []
        self.size_buissonX = 80
        self.size_buissonY = 40
        self.source = []
        self.size_sourceX = 100
        self.size_sourceY = 100
        self.etre_vivant = self.mechant + self.player
        self.acteurs = []

    def affiche_pv(self, acteur):
        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render(str(acteur.pv), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (acteur.x + 10, acteur.y - 10)
        self.win.blit(text, textRect)

    def draw_game(self):
        self.win.fill((255, 255, 255))
        for source in self.source:
            pygame.draw.rect(self.win, (0, 180, 255), (source.x, source.y, self.size_sourceX, self.size_sourceY))
        for mechant in self.mechant:
            pygame.draw.rect(self.win, (255, 0, 0), (mechant.x, mechant.y, self.size_mechantX, self.size_mechantY))
            self.affiche_pv(mechant)
        for buisson in self.buisson:
            pygame.draw.rect(self.win, (0, 255, 0), (buisson.x, buisson.y, self.size_buissonX, self.size_buissonY))
        for player in self.player:
            pygame.draw.rect(self.win, (0, 0, 255), (player.x, player.y, self.size_playerX, self.size_playerY))
            self.affiche_pv(player)
        pygame.display.update()

    def update(self):
        for acteur in self.acteurs:
            acteur.comportement()
        self.draw_game()
