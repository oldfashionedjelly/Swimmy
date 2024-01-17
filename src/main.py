import pygame
import random
class bubble():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(1,3)
        self.pic = pygame.image.load("../assets/Bubble.png")
        self.on_screen = True
        self.size = random.randint(5, 25)
        self.pic = pygame.transform.scale(self.pic, (self.size, self.size))
    def update(self, screen):
        self.y -= self.speed
        screen.blit(self.pic, (self.x, self.y))
        if self.y < -self.pic.get_height():
            self.on_screen = False
class enemy():
    def __init__(self, x , y, speed, size):
        self.x = x
        self.y = y
        self.type = random.randint(0, 4)
        if self.type == 0:
            self.pic = pygame.image.load("../assets/Fish01_A.png")
            self.pic2 = pygame.image.load("../assets/Fish01_B.png")
        if self.type == 1:
            self.pic = pygame.image.load("../assets/Fish02_A.png")
            self.pic2 = pygame.image.load("../assets/Fish02_B.png")
        if self.type == 2:
            self.pic = pygame.image.load("../assets/Fish03_A.png")
            self.pic2 = pygame.image.load("../assets/Fish03_B.png")
        if self.type == 3:
            self.pic = pygame.image.load("../assets/Fish04_A.png")
            self.pic2 = pygame.image.load("../assets/Fish04_B.png")
        if self.type == 4:
            self.pic = pygame.image.load("../assets/Fish05_A.png")
            self.pic2 = pygame.image.load("../assets/Fish05_B.png")
        self.speed = speed
        self.size = size
        self.hitbox = pygame.Rect(self.x, self.y, int(self.size * 1.25), self.size)
        self.animation_timer_max = 3
        self.animation_timer = self.animation_timer_max
        self.animation_frame = 0 
        self.pic = pygame.transform.scale(self.pic, (int(self.size * 1.25), self.size))
        self.pic2 = pygame.transform.scale(self.pic2, (int(self.size * 1.25), self.size))
        if self.speed < 0:
            self.pic = pygame.transform.flip(self.pic, True, False)
            self.pic2 = pygame.transform.flip(self.pic2, True, False)
    def update(self, screen):
        self.animation_timer -= 1
        if self.animation_timer <= 0:
            self.animation_timer = self.animation_timer_max
            self.animation_frame += 1
        if self.animation_frame > 1:
            self.animation_frame = 0
        if self.animation_frame == 0:
            screen.blit(self.pic, (self.x, self.y))
        else:
            screen.blit(self.pic2, (self.x, self.y))
        self.x += self.speed
        self.hitbox.x += self.speed
        # pygame.draw.rect(screen, (0, 255, 0), self.hitbox)
pygame.init()
game_width = 1000        
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True
background_pic = pygame.image.load("../assets/Scene_A.png")
background_pic2 = pygame.image.load("../assets/Scene_B.png")
player_pic = pygame.image.load("../assets/Fish04_A.png")
player_pic2 = pygame.image.load("../assets/Fish04_B.png")
player_eating_pic = pygame.image.load("../assets/Fish04_open.png")
bg_animation_timer_max = 5
bg_animation_timer = bg_animation_timer_max
bg_animation_frame = 0
play_button_pic = pygame.image.load("../assets/BtnPlayIcon.png")
play_button_x = game_width / 2 - play_button_pic.get_width() / 2
play_button_y = game_height / 2 - play_button_pic.get_height() / 2
title_pic = pygame.image.load("../assets/swimmy.png")
title_x = game_width / 2 - title_pic.get_width() / 2 
title_y = play_button_y - 200
player_starting_x = 475 
player_starting_y = 300
player_speed = 0.4
player_speed_x = 0
player_speed_y = 0
player_starting_size = 50
player_x = player_starting_x
player_y = player_starting_y
player_size = player_starting_size
player_facing_left = False
player_hitbox = pygame.Rect(player_x,player_y, int(player_size * 1.25), player_size)
player_alive = False
player_eating_timer_max = 2
player_eating_timer = 0
player_animation_timer_max = 3
player_animation_timer = player_animation_timer_max 
player_animation_frame = 0
score = -1
font = pygame.font.SysFont("markerfeltttc", 30)
score_text = font.render("Score : " + str(score), 1, (0,0,255))
enemy_timer_max = 15
enemy_timer = enemy_timer_max
enemies = []
enemies_to_remove = []
bubbles = []
bubbles_to_remove = []
bubble_timer = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_speed_x += player_speed
    if keys[pygame.K_LEFT]:
        player_speed_x -= player_speed
    if keys[pygame.K_UP]:
        player_speed_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_speed_y += player_speed
    if player_speed_x > 1:
        player_speed_x -= 0.15
    if player_speed_x < -1:
        player_speed_x += 0.15
    if player_speed_y > 1:
        player_speed_y -= 0.15
    if player_speed_y < -1:
        player_speed_y += 0.15
    player_x += player_speed_x
    player_y += player_speed_y
    if player_speed_x > 0:
        player_facing_left = False
    else:
        player_facing_left = True
     # if keys[pygame.K_SPACE]:
        # player_size += 5
    if player_x < 0:
        player_x = 0
        player_speed_x = 0
    if player_x > game_width - player_size * 1.25:
        player_x = game_width - player_size * 1.25
        player_speed_x = 0
    if player_y < 0:
        player_y = 0
        player_speed_y = 0
    if player_y > game_height - player_size:
        player_y = game_height - player_size
        player_speed_y = 0
    bg_animation_timer -= 1
    if bg_animation_timer <= 0:
         bg_animation_frame += 1
         if bg_animation_frame > 1:
             bg_animation_frame = 0
         bg_animation_timer = bg_animation_timer_max
    if bg_animation_frame == 0:
         screen.blit(background_pic, (0, 0))
    else:
         screen.blit(background_pic2, (0, 0))
    enemy_timer -= 1
    if enemy_timer <= 0:
        new_enemy_size = random.randint(int(player_size / 2) ,player_size*2)
        new_enemy_y = random.randint(0, game_height)
        new_enemy_speed = random.randint(3,10)
        if random.randint(0,1) == 0:
            enemies.append(enemy(-new_enemy_size * 2, new_enemy_y, new_enemy_speed, new_enemy_size))
        else:
            enemies.append(enemy(game_width, new_enemy_y, -new_enemy_speed, new_enemy_size))
        enemy_timer = enemy_timer_max
    for counter in enemies_to_remove:
        enemies.remove(counter)
        enemies_to_remove = []
    for counter in enemies:
        counter.update(screen)
        if counter.x < -1000 or counter.x > game_width + 1000:
            enemies_to_remove.append(counter)
    bubble_timer -= 1
    if bubble_timer <= 0:
        bubbles.append(bubble(random.randint(0, game_width), game_height))
        bubble_timer = random.randint(30, 80)
    for counter in bubbles:
        if counter.on_screen:
            counter.update(screen)
        else:
            bubbles_to_remove.append(counter)
    for counter in bubbles_to_remove:
        bubbles.remove(counter)
    bubbles_to_remove = []
    if player_alive: 
        player_hitbox.x = player_x
        player_hitbox.y = player_y
        player_hitbox.width = player_size * 1.25
        player_hitbox.height = player_size
        # pygame.draw.rect(screen, (255, 0, 0), player_hitbox)
        for counter in enemies:
            if player_hitbox.colliderect(counter.hitbox):
                if player_size > counter.size:
                    score += counter.size
                    player_size += 5
                    enemies.remove(counter)
                    player_eating_timer = player_eating_timer_max
                elif player_size < counter.size:
                    player_alive = False
        player_animation_timer -= 1
        if player_animation_timer <= 0:
            player_animation_timer = player_animation_timer_max
            player_animation_frame += 1
            if player_animation_frame > 1:
                player_animation_frame = 0
        if player_eating_timer > 0:
            player_pic_small = pygame.transform.scale(player_eating_pic, (int(player_size * 1.25), player_size))
            screen.blit(player_pic_small, (player_x, player_y)) 
            player_eating_timer -= 1
        else:
            if player_animation_frame == 0:
                player_pic_small = pygame.transform.scale(player_pic, (int(player_size * 1.25), player_size))
            else:
                player_pic_small = pygame.transform.scale(player_pic2, (int(player_size * 1.25), player_size))
            if player_facing_left:
                player_pic_small = pygame.transform.flip(player_pic_small, True, False)
            screen.blit(player_pic_small, (player_x, player_y))
    if player_alive:
        if score >= 0:
            screen.blit(score_text, (30,30)) 
        score_text = font.render("Score : " + str(score), 1, (0,0,255))
    else:
        if score != -1:
            score_text = font.render("Your Final Score is " + str(score), 1, (0,0,255))
            screen.blit(score_text, (30, 30))
    if not player_alive:
        screen.blit(play_button_pic, (play_button_x, play_button_y))
        screen.blit(title_pic, (title_x, title_y))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if mouse_x > play_button_x and mouse_x < play_button_x + play_button_pic.get_width():
                if mouse_y > play_button_y and mouse_y < play_button_y + play_button_pic.get_height():
                    player_alive = True
                    score = 0
                    player_x = player_starting_x
                    player_y = player_starting_y
                    player_size = player_starting_size
                    player_speed_x = 0
                    player_speed_y = 0
                    for counter in enemies:
                        enemies_to_remove.append(counter)
    pygame.display.flip()
    clock.tick(50)
    pygame.display.set_caption("MY GAME fps: " + str(clock.get_fps()))
