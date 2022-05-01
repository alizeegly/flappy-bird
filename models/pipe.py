import pygame, random

class Pipe(pygame.sprite.Sprite):
    
    def __init__(self, game, y, position):
        super().__init__() 
        self.game = game
        self.image = pygame.image.load("assets/pipe-green.png")
        self.position = position
        self.rect = self.image.get_rect()

        if self.position == "top":
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect(midbottom=(self.game.screen.get_width(), y))
        else:
            self.rect = self.image.get_rect(midtop=(self.game.screen.get_width(), y))

    def remove(self):
        # Delete a pipe
        self.game.all_pipes.remove(self)

    def move_pipe(self):
        self.rect.x -= 1.1
        y_random = random.choice([50, 150, 250])
        
        # vérifier si le pipe passe à gauche de l'écran
        if self.rect.x <= -10:
            self.can_update_score = True
            self.game.add_score() # Add score
            for pipe in self.game.all_pipes:
                pipe.remove() # Remove it from the list
            # Create 2 new pipes
            self.game.create_pipe(self.game.screen.get_width(), y_random, "top")
            self.game.create_pipe(self.game.screen.get_width(), y_random, "bottom")
