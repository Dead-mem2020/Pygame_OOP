from os import name
import pygame
from config import *
from game.player import Player
from game.platform import Platform
from game.coin import Coin
import random

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.all_sprites = pygame.sprite.Group()
        self.platform = pygame.sprite.Group()
        
        self.player = Player(100, 100)
        self.all_sprites.add(self.player)

        # Platformy
        ground = Platform(0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40)
        self.platform.add(ground)
        self.all_sprites.add(ground)

        platform1 = Platform(200, 421, 150, 20)
        self.platform.add(platform1)
        self.all_sprites.add(platform1)

        platform2 = Platform(250, 300, 150, 20)
        self.platform.add(platform2)
        self.all_sprites.add(platform2)

        platform3 = Platform(600, 320, 150, 20)
        self.platform.add(platform3)
        self.all_sprites.add(platform3)

        # Náhodné generování mincí
        self.coin = pygame.sprite.Group()
        for coins in range(5):
            x = random.randint(50, SCREEN_WIDTH - 50) # Meze kde se mince může generovat (šířka)
            y = random.randint(200, SCREEN_HEIGHT - 100) # Meze kde se mince může generovat (výška)

            coin = Coin(x, y) 
            self.coin.add(coin)
            self.all_sprites.add(coin)


    def handle_events(self):
        for event in pygame.event.get():
            evt_name = pygame.event.event_name(event.type)

            if event.type == pygame.QUIT:
                self.running = False


            if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                evt_name = pygame.key.name(event.key)
                print(f"{evt_name}: {event.key}")

            elif event.type == pygame.MOUSEMOTION:
                print(f"{evt_name}: {event.pos}")

            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP):
                print(f"{evt_name}: {event.button} at {event.pos}")
    
                

    def update(self):
        game_over = self.player.update(self.platform)
        if game_over:
            self.running = False

        pygame.sprite.spritecollide(self.player, self.coin, True)

        if len(self.coin) == 0:
            print("Vyhrál jsi! Všechny mince jsou vysbírané.")
            self.running = False

    def draw(self):
        self.screen.fill(SKY_BLUE)
        
        for sprite in self.all_sprites:
            sprite.draw(self.screen)

        pygame.display.flip()



    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)