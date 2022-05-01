import pygame

class Bird(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__() 
        self.game = game
        self.fall_speed = 0.05
        self.image = pygame.transform.scale(pygame.image.load('assets/yellowbird-upflap.png'), (48, 35)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 200

    def fall(self):
        # Speed and fall of the bird
        self.game.bird_movement = self.fall_speed + self.game.bird_movement # Speed of falling
        self.rect.centery += self.game.bird_movement
        for pipe in self.game.all_pipes: 
            if self.game.check_collision(pipe, self.game.all_birds): # If bird touch a pipe
                self.game.game_over()