# Importing 'pygame' 
import pygame

# Initialising 'pygame' 
pygame.init()

# Creating game window of width 400 and height 600
screen = pygame.display.set_mode((400,600))

# Setting the title of the game
pygame.display.set_caption("Shooting Spaceship")

# Loading the background image
background_image = pygame.image.load("bg2.jpg").convert()

# Displaying the 'background_image' at the location [0,0]
screen.blit(background_image,[0,0])

# Creating BLUE color using RGB combinations and naming it as 'BLUE'
BLUE=(0,0,255)

# Creating a rectangle at the coordinates 200,200 with width and height as 30
# Name the rectangle as 'player'
player=pygame.Rect(200,200,30,30)

# Drawing the 'player' rectangle in the screen in BLUE color
pygame.draw.rect(screen,BLUE,Blue_rect)

# Creating WHITE color using RGB combinations and naming it as 'WHITE'
WHITE=(255,255,255)

# Creating a rectangle at the coordinates 100,100 with width and height as 30
# Name the rectangle as 'enemy'
enemy=pygame.Rect(100,100,30,30)

# Drawing the 'enemy' rectangle in the screen in WHITE color
pygame.draw.rect(screen,WHITE,enemy)

# Updating the screen display
pygame.display.update()
