import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, map, x, y, width, height, is_optional, texture, health):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.max_health = health
        self.is_alive = True
        self.is_optional = is_optional
        self.texture = pygame.image.load(texture)
        self.animation_state = False

        self.map = map
        self.enemy_clock = pygame.time.Clock()
        self.animation_start_time = pygame.time.get_ticks()
        self.animation_interval = 500
        self.texture = pygame.transform.scale(self.texture, (width, height))
        self.enemy_rect = self.texture.get_rect()
        self.enemy_rect.topleft = (self.x, self.y)

    def update_enemy(self, player):
        if (player.x >= self.x + self.map.map_x - self.width and
                self.y - self.height <= player.y <= self.y + self.height and self.is_alive):
            player.damage_player(100)
        current_time = pygame.time.get_ticks()

        elapsed_time = current_time - self.animation_start_time
        if elapsed_time >= self.animation_interval:
            self.animation_start_time = current_time

        # TODO: Add animation here
        self.enemy_clock.tick(60)

    def draw_health_bar(self, screen):
        bar_width = self.width
        bar_height = 5
        health_percentage = max(0, self.health / self.max_health)
        bar_color = (0, 255, 0)

        bar_x = self.x + self.map.map_x
        bar_y = self.y - 10

        pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(screen, bar_color, (bar_x, bar_y, bar_width * health_percentage, bar_height))

    def render_enemy(self, screen):
        self.draw_health_bar(screen)
        screen.blit(self.texture, (self.x + self.map.map_x, self.y))

    def damage_enemy(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
