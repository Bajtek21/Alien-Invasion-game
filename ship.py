import pygame


class Ship:
    """Klasa odpowiadająca zachowaniom statku w grze"""

    def __init__(self, game):
        """Inicjalizacja statku i jego położenie początkowe"""

        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # Wczytanie obrazu statku i pobranie jego prostokąta
        self.image = pygame.image.load('obrazy/statek.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Uaktualnienie połozenia statku"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Wyświetlanie statku w jego aktualnym położenmiu"""
        self.screen.blit(self.image, self.rect)
