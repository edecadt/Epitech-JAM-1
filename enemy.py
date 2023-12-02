import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, is_optional, texture):
        super().__init__()
        self.x = x
        self.y = y
        self.health = 100
        self.is_alive = True
        self.is_optional = is_optional
        self.texture = pygame.image.load(texture)
        self.animation_state = False

        self.enemy_clock = pygame.time.Clock()
        self.animation_start_time = pygame.time.get_ticks()
        self.animation_interval = 500
        self.texture = pygame.transform.scale(self.texture, (width, height))

    def update_enemy(self):
        current_time = pygame.time.get_ticks()

        elapsed_time = current_time - self.animation_start_time
        if elapsed_time >= self.animation_interval:
            self.animation_start_time = current_time

        # TODO: Add animation here
        self.enemy_clock.tick(60)

    def render_enemy(self, screen):
        screen.blit(self.texture, (self.x, self.y))

    def damage_enemy(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
