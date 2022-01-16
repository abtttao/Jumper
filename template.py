import pygame

pygame.init()
clock = pygame.time.Clock()
fps = 30

# ------------ game variables ----------
screen_width = 800
screen_height = 400

# ------------ images ----------
# bg_img = pygame.image.load('img/Background/background.png')

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')

run = True
while run:
    # frame rate
    clock.tick(fps)
    
    # clear screen and draw background image
    # screen.blit(bg_img, (0,0))
    # or fill with color
    # screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            # exit game by ESC key
            if event.key == pygame.K_ESCAPE:
                run = False
    
    pygame.display.update()

pygame.quit()