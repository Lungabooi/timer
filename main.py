import pygame,sys
# setting the game
 
pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

current_time = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    current_time = pygame.time.get_ticks()  
    print(current_time)    
    pygame.display.flip()
    clock.tick(60)