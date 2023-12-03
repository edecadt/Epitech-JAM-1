import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, texture, attack_damage, color_map):
        super().__init__()
        self.color_map = color_map
        self.init_y = y
        self.x = x
        self.y = y
        self.health = 100
        self.max_health = 100
        self.is_alive = True
        self.texture = pygame.image.load(texture)
        self.animation_state = False
        self.attack_damage = attack_damage
        self.jump_velocity = 0
        self.is_jumping = 0
        self.jump_moment = 0

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

    def jump_setup(self):
        if self.is_jumping:
            return
        self.jump_moment = pygame.time.get_ticks() / 60
        self.is_jumping = 1
        self.jump_velocity = 65

    def next_y(self, time):
        return int((4.91 * (time ** 2) - self.jump_velocity * time) + self.init_y)

    def is_green(self, x, y):
        return self.color_map.image.get_at((x, y))[1] != 0

    def jump(self):
        time = pygame.time.get_ticks() / 60 - self.jump_moment

        # Check if above height limit
        if self.next_y(time) < 10:
            self.y = self.next_y(time)
            return

        # If not jumping decrease height linearly
        if not self.is_jumping:
            self.jump_moment = time
            self.jump_velocity = 0
            if self.is_green(-self.color_map.map_x + self.x, self.y + 20 + 99) or \
                    self.is_green(-self.color_map.map_x + self.x + 99, self.y + 20 + 99):
                for i in range(self.y, 432):
                    if self.is_green(-1 * self.color_map.map_x + self.x, i + 99) or \
                            self.is_green(-self.color_map.map_x + self.x + 99, i + 99):
                        self.y = i - 1
                        self.init_y = i - 1
                        return
                return
            self.y += 15
            return

        # Check collision under
        if self.is_green(-self.color_map.map_x + self.x, self.next_y(time) + 99) or \
                self.is_green(-self.color_map.map_x + self.x + 99, self.next_y(time) + 99):
            for i in range(self.y, 432):
                if self.is_green(-self.color_map.map_x + self.x, i + 99) or \
                        self.is_green(-self.color_map.map_x + self.x + 99, i + 99):
                    self.y = i - 1
                    self.init_y = i - 1
                    break
            self.is_jumping = 0
            return

        # Check collision above
        if self.is_green(-self.color_map.map_x + self.x, self.next_y(time)) or \
                self.is_green(-self.color_map.map_x + self.x + 99, self.next_y(time)):
            self.jump_moment = time
            self.jump_velocity = 0
            self.is_jumping = 0
            return

        # Set new position
        self.y = self.next_y(time)
