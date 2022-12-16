import pygame
from dino_runner.utils.constants import (
    RUNNING,
    JUMPING,
    DUCKING,
    DEFAULT_TYPE,
    DUCKING_SHIELD,
    SHIELD_TYPE,
    JUMPING_SHIELD,
    RUNNING_SHIELD,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,

)
from dino_runner.components.shots.projeteis import Projeteis

Y_POS_DUCK = 280
X_POS = 80
Y_POS = 220
p_x_pos = 100
p_y_pos = 250

JUMP_VEL = 8.5

DUCK_IMG = {
    DEFAULT_TYPE: DUCKING,
    SHIELD_TYPE:  DUCKING_SHIELD,
}
JUMP_IMG = {
    DEFAULT_TYPE: JUMPING,
    SHIELD_TYPE: JUMPING_SHIELD,
}

RUN_IMG = {
    DEFAULT_TYPE: RUNNING,
    SHIELD_TYPE: RUNNING_SHIELD,
}


class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.jump_vel = JUMP_VEL
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_firing = False
        self.setup_state()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.projetil_y_pos = p_y_pos
        self.projetil_x_pos = p_x_pos
        self.ret_vermelho = pygame.draw.circle(self.screen, (255, 0, 0), (self.projetil_x_pos, self.projetil_y_pos), 20)
        self.count = 0
            #pygame.draw.rect(self.screen, (255, 0, 0), (self.projetil_x_pos, self.projetil_y_pos, 40, 50))

        #self.muni = Projeteis()

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0

    def run(self):

        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            if not self.dino_firing:
                self.projetil_y_pos -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS_DUCK
        self.step_index += 1
        self.dino_duck = False

    def firing(self):                       #Física do Projétil
        self.count += 1
        self.projetil_x_pos += 15
        if self.count < 10:
            self.projetil_y_pos -= 5
        elif (self.count > 10) and (self.count < 15):
            self.projetil_y_pos -= 2
        else:
            self.projetil_y_pos += 5
        if self.projetil_x_pos > 1000:
            self.projetil_x_pos = p_x_pos
            self.projetil_y_pos = p_y_pos
            self.count = 0
            self.dino_firing = False
#a
    def update(self, user_input):
        if self.dino_run:
            self.run()

        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
        if self.dino_firing:    #Se projetil estiver em curso
            self.firing()
        if user_input[pygame.K_LEFT]:
            self.dino_firing = True

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True

        elif not self.dino_jump:
            if not self.dino_firing:
                self.projetil_y_pos = p_y_pos
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False

        if self.step_index >= 9:
            self.step_index = 0
        self.p_pos_reset()
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        self.ret_vermelho = pygame.draw.circle(self.screen, (255, 0, 0), (self.projetil_x_pos, self.projetil_y_pos), 20)

        #self.muni.retangulo()
    def p_pos_reset(self):
        self.p_x_pos = 100
        self.p_y_pos = 250
