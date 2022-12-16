from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import METEOR_2
import random
class Meteor_2(Obstacle):

    def __init__(self):
        super().__init__(METEOR_2, 0)
        self.rect.y = random.randint(20, 100)
        self.rect.x = random.randint(300,800)
        self.step_index = 0
        self.obstacle_vel = 5

    def draw(self, screen):
        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1

        if self.step_index >= 10:
            self.step_index = 0

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed - 15
        self.rect.y += game_speed - 10
        if self.rect.x < -self.rect.width:
            obstacles.pop()
