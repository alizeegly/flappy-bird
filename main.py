import pygame, math
from models.bird import Bird
from game import Game

pygame.init()

# Create the window
pygame.display.set_caption("Jeu pygame 2")
screen = pygame.display.set_mode((900, 500))

# Assets
background = pygame.image.load("assets/background.png").convert()
logo = pygame.image.load("assets/logo2.png")
logo = pygame.transform.scale(logo, (420, 132))
playBtn =pygame.image.load("assets/playbtn.png").convert_alpha()
playBtn = pygame.transform.scale(playBtn, (133, 83))
play_button_rect = playBtn.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/ 2 - playBtn.get_width()/2)
play_button_rect.y = math.ceil(350)
floor = pygame.image.load("assets/floor.png").convert()
floor = pygame.transform.scale(floor, (900, 80))

# Create the party and the bird 
game = Game(screen)
bird = Bird(game)

# New event to create pipe every 1000 ms
new_event = pygame.USEREVENT
pygame.time.set_timer(new_event, 1000)

# Read the high score saved in data.txt
with open('data.txt') as file:
    saved_score = file.read()
    game.high_score = int(saved_score)

running = True

# Loop for keeping window open
while running:
    screen.blit(background, (0, 0)) # Add background to the window
    screen.blit(floor, (0, 450)) # Add floor to the window
    
    if game.is_playing: # In game
        game.update() 
    else: # If not playing, show the menu 
        screen.blit(logo, (screen.get_width()/ 2 - logo.get_width()/2 , 50)) # Add bird to the window
        screen.blit(playBtn, play_button_rect) # Add bird to the window


    # Check the events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Quit the window
            running = False
            print("End game")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game.is_playing == True: # player press space tab
                # bird go up
                game.bird_movement = -3
            if event.key == pygame.K_SPACE and game.is_playing == False: # player press space tab
                game.start()
        elif event.type == pygame.MOUSEBUTTONDOWN: # If user click on menu button
            if play_button_rect.collidepoint(event.pos):
                game.start()
                if game.is_playing == True: # bird go up on click too
                    game.bird_movement = -3


    pygame.display.flip()

# Clear the cache
pygame.quit()