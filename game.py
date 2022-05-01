import pygame
from models.bird import Bird
from models.pipe import Pipe
import random

class Game:
    def __init__(self, screen):
        self.is_playing = False
        self.screen = screen
        self.is_playing = False
        self.all_birds = pygame.sprite.Group()
        self.all_pipes = pygame.sprite.Group()
        self.bird = Bird(self)
        self.all_birds.add(self.bird)
        self.bird_movement = 0
        self.score = 0
        self.high_score = 0
        self.font_score = pygame.font.Font("assets/04B_19.TTF", 40)
        self.font_high_score = pygame.font.Font("assets/04B_19.TTF", 25)
        self.can_update_score = True

    def update(self):
        # Set score and high score
        score_text = self.font_score.render(str(int(self.score)), 1, (255, 255, 255))
        self.screen.blit(score_text, (self.screen.get_width()/2, 40))
        high_score_text = self.font_high_score.render(f"High Score : {str(self.high_score)}", 1, (255, 255, 255))
        self.screen.blit(high_score_text, (self.screen.get_width()/2 - high_score_text.get_width()/2, 90))

        self.screen.blit(self.bird.image, self.bird.rect) # Add bird to the window
        self.bird.fall()

        # Draw all pipes into the screen
        for pipe in self.all_pipes:
            pipe.move_pipe()
        self.all_pipes.draw(self.screen)

        if self.bird.rect.top < 0 or self.bird.rect.bottom >= 450: # If user touch the top or bottom of the screen
            self.game_over()

    def create_pipe(self, x, y, position):
        if position == "bottom": # Create bottom pipe
            bottom_pipe = Pipe(self, y+200, "bottom")
            self.all_pipes.add(bottom_pipe)
        else: # Create top pipe
            top_pipe = Pipe(self, y, "top")
            self.all_pipes.add(top_pipe)

    def check_collision(self, element, group):
        # Check collision between pipes (group) and bird (element)
        return pygame.sprite.spritecollide(element, group, False, pygame.sprite.collide_mask)

    def game_over(self):
        # If user loose
        if self.score > self.high_score: # if user get a better score than the high score
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.is_playing = False # Back to the menu
        self.all_pipes = pygame.sprite.Group() # Group of pipes empty
        self.bird_movement = 0 # Bird doesn't move
        self.bird.rect.y = 200 # position of the beggining
        self.score = 0 # Reset score 
        self.can_update_score = True
    
    def start(self):
        # Start the game
        self.is_playing = True
        y_random = random.choice([50, 150, 250])
        self.create_pipe(self.screen.get_width(), y_random, "top")
        self.create_pipe(self.screen.get_width(), y_random, "bottom")

    def add_score(self):
        # For every pipe of the list
        if self.all_pipes:
            for pipe in self.all_pipes:
                if pipe.rect.centerx < self.bird.rect.centerx: # If the bird is between the two pipes
                    # Update the score
                    self.score += 1/2
                    self.can_update_score = False