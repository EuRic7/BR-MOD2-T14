import random

import pygame

from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.meteor import Meteor
from dino_runner.components.obstacles.meteor_2 import Meteor_2

class ObstacleManager:
    def __init__(self):
        self.obstacles = []


    def update(self, game):
        obstacle_type = [
            Cactus(),
            Bird(),
            Meteor(),
            Meteor_2(),

        ]

        if len(self.obstacles) == 0:
            self.obstacles.append(
                obstacle_type[random.randint(0, 3)]
            )

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
#a
                else:
                    self.obstacles.remove(obstacle)
            if obstacle.rect.colliderect(game.player.ret_vermelho):
                self.obstacles.remove(obstacle)
                game.score += 100
    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
