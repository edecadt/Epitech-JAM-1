import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, texture, attack_damage):
        super().__init__()
        self.x = x
        self.y = y
        self.health = 100
        self.max_health = 100
        self.is_alive = True
        self.texture = pygame.image.load(texture)
        self.animation_state = False
        self.attack_damage = attack_damage

        self.player_clock = pygame.time.Clock()
        self.animation_start_time = pygame.time.get_ticks()
        self.animation_interval = 500
        self.texture = pygame.transform.scale(self.texture, (width, height))

    def update_player(self):
        current_time = pygame.time.get_ticks()

        elapsed_time = current_time - self.animation_start_time
        if elapsed_time >= self.animation_interval:
            self.animation_start_time = current_time

        # TODO: Add animation here
        self.player_clock.tick(60)

    def render_player(self, screen):
        screen.blit(self.texture, (self.x, self.y))

    def damage_player(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
