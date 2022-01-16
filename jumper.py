import pygame
from pygame import mouse
from pygame.locals import *
import pyganim

pygame.init()
clock = pygame.time.Clock()
fps = 30

# ------------ game variables ----------
screen_width = 800
screen_height = 400
snail_x = 600
player_vspeed = 0
game_over = False
score_check = False
score = 0
snail_speed = 4
# ------------ game setting ------------
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Jumper')


# ------------ font ----------
game_font = pygame.font.Font('font/Pixeltype.ttf', 50)



# ------------ images ----------
sky_img = pygame.image.load('graphics/Sky.png').convert()
sky_img_height = sky_img.get_height()
ground_img = pygame.image.load('graphics/ground.png').convert()
snail_img = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
player_img = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_img.get_rect(midbottom = (120, sky_img_height))
snail_rect = snail_img.get_rect(bottomright = (snail_x, sky_img_height))
player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
restart_img = pygame.image.load('img/restart.png')

# --- palyer animation ---
player_set = []
for i in range(2):
    player_set.append((f'graphics/Player/player_walk_{i+1}.png', 200))

player_anim = pyganim.PygAnimation(
    player_set
)
player_anim.play()
player_height = player_anim.getRect().height
player_width = player_anim.getRect().width


# --- snail animation ---
snail_set = []
for i in range(2):
    snail_set.append((f'graphics/snail/snail{i+1}.png', 200))

snail_anim = pyganim.PygAnimation(
    snail_set
)
snail_anim.play()
snail_height = snail_anim.getRect().height
snail_width = snail_anim.getRect().width


# ------------ sound ----------
player_jump_sound = pygame.mixer.Sound('audio/jump.mp3')
player_jump_sound.set_volume(0.3)
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.play(loops = -1)
bg_music.set_volume(0.1)
lose_music = pygame.mixer.Sound('audio/lose.wav')




def restart():
    global snail_x, game_over, player_anim, player_vspeed,player_rect,snail_rect,score, snail_speed
    score = 0
    snail_x = 800
    snail_speed = 4
    player_anim.play()
    snail_anim.play()
    player_vspeed = 0
    game_over = False
    player_rect = player_img.get_rect(midbottom = (120, sky_img_height))
    snail_rect = snail_img.get_rect(bottomright = (snail_x, sky_img_height))

# ============ Game Start ==============
run = True
while run:

   

    # frame rate
    clock.tick(fps)
    
    # clear screen and draw background image
    screen.blit(sky_img, (0, 0))
    screen.blit(ground_img, (0, sky_img_height))
    # or fill with color
    # screen.fill((255,255,255))


    # score text
    game_txt = game_font.render('Score: '+ str(score), False, 'Black')
    game_txt_rect = game_txt.get_rect(center =(400,50))
    screen.blit(game_txt, game_txt_rect)

    # snail
    snail_anim.blit(screen, snail_rect)
    snail_rect.x -= snail_speed

    # if score == 1 :
    #     print('up speed')
    #     # snail_speed += 
    #     snail_speed =snail_speed+ 4

    if snail_rect.right <= 0:
        score_check=False
        snail_rect.left = 800

    if snail_rect.x < 0 and score_check == False:
        score += 1
        snail_speed =snail_speed+ 1
        score_check = True
        

    # player
    # screen.blit(player_img, (100, sky_img_height - 84))
    player_anim.blit(screen, player_rect)

    # jump
    player_rect.y += player_vspeed

    # fall
    player_vspeed += 1

    # fall only if not on ground
    if player_rect.bottom >= sky_img_height:
        # make speed to zero
        player_vspeed = 0
        # reset the ground position
        player_rect.bottom = sky_img_height
    

    # collision check
    if player_rect.colliderect(snail_rect):
        # print('collison')
        snail_rect.x = 120
        snail_anim.pause()
        player_rect.bottom = 600
        player_anim.pause()
        screen.blit(restart_img, (345, 120))
        game_over = True
        lose_music.play(loops = 0)
        if game_over:
            if pygame.mouse.get_pressed()[0] == 1:
            # print('restart')
            # rectangle of restart image
                restart_rect = restart_img.get_rect()
            # set the top-lef position of restart image
                restart_rect.topleft = (345, 120)
            # get mouse click position
                mouse_pos = pygame.mouse.get_pos()
            # print(mouse_pos)
            # print(restart_rect)
            # if we click on a restart image rectangle
                if restart_rect.collidepoint(mouse_pos):
                    
                    restart()
                    
                # restart game
                    
                # print('restart')
 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            # exit game by ESC key
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_SPACE and player_rect.bottom >= sky_img_height:
                # print('jump')
                if game_over == False:
                    player_vspeed -= 20
                    player_jump_sound.play()
                    screen.blit(player_jump, player_rect)
                
                    

    pygame.display.update()

pygame.quit()