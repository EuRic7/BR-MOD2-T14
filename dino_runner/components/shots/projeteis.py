import pygame
from dino_runner.utils.constants import (

    SCREEN_HEIGHT,
    SCREEN_WIDTH,

)

class Projeteis:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.projetil_x_pos = 80
        self.projetil_y_pos = 220


    def retangulo(self):
        self.ret_vermelho = pygame.draw.rect(self.screen, (255, 0, 0),
                                             (self.projetil_x_pos, self.projetil_y_pos, 40, 50))
