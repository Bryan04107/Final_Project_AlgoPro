import pygame, random, sys, math
pygame.mixer.init()

#Seperates The Sprite Sheets Into Idividual Pieces
class SpriteSheet():
	def __init__(self, image):
		self.sheet = image

	def get_image(self, frame, image_width, image_height, gap_width, gap_height, scale, row):
		image = pygame.Surface((image_width, image_height))
		image.blit(self.sheet, (0, 0), ((frame * (image_width + gap_width * 2) + gap_width), (row * (image_height + gap_height * 2) + gap_height), image_width, image_height))
		image = pygame.transform.scale(image, (image_width * scale, image_height * scale))
		image.set_colorkey((0, 0, 0))
		return image

boss_chase_cycle = []
boss_attack_cycle = []
boss_death_cycle = []
idle_down_frame_cycle = []
idle_left_frame_cycle = []
idle_right_frame_cycle = []
idle_up_frame_cycle = []
walk_down_frame_cycle = []
walk_left_frame_cycle = []
walk_right_frame_cycle = []
walk_up_frame_cycle = []
heart = []
heart2 = []
ground = []
boss_scale = 8
player_scale = 2
get_frame1 = SpriteSheet(pygame.image.load('Img\Boss1.png'))
get_frame2 = SpriteSheet(pygame.image.load('Img\Heart.png'))
get_frame3 = SpriteSheet(pygame.image.load('Img\Player.png'))
get_frame4 = SpriteSheet(pygame.image.load('Img\Ground.png'))
get_frame5 = SpriteSheet(pygame.image.load('Img\Heart2.png'))
for a in range(4):
    boss_chase_cycle.append(get_frame1.get_image(a, 22, 18, 2, 0, boss_scale, 2))
for b in range(10):
    boss_attack_cycle.append(get_frame1.get_image(b, 22, 18, 2, 0, boss_scale, 0))
for c in range(7):
    boss_attack_cycle.append(get_frame1.get_image(c, 22, 18, 2, 0, boss_scale, 1))
for d in range(9):
    boss_death_cycle.append(get_frame1.get_image(d, 22, 18, 2, 0, boss_scale, 3))
for e in range(5):
    heart.append(get_frame2.get_image(e, 17, 17, 0, 0, 7, 0))
    heart2.append(get_frame5.get_image(e, 17, 17, 0, 0, 7, 0))
for f in range(4):
    idle_down_frame_cycle.append(get_frame3.get_image(f, 12, 14, 10, 9, player_scale, 0))
    idle_left_frame_cycle.append(get_frame3.get_image(f, 12, 14, 10, 9, player_scale, 1))
    idle_right_frame_cycle.append(get_frame3.get_image(f, 12, 14, 10, 9, player_scale, 2))
    idle_up_frame_cycle.append(get_frame3.get_image(f, 12, 14, 10, 9, player_scale, 3))
    walk_down_frame_cycle.append(get_frame3.get_image(f, 12, 14, 10, 9, player_scale, 4))
    walk_left_frame_cycle.append(get_frame3.get_image(f, 12, 14, 10, 9, player_scale, 5))
    walk_right_frame_cycle.append(get_frame3.get_image(f, 12, 14, 10, 9, player_scale, 6))
    walk_up_frame_cycle.append(get_frame3.get_image(f, 12, 14, 10, 9, player_scale, 7))
for g in range(8):
    ground.append(get_frame4.get_image(g, 32, 32, 0, 0, 1.25, 0))
    ground.append(get_frame4.get_image(g, 32, 32, 0, 0, 1.25, 1))
    ground.append(get_frame4.get_image(g, 32, 32, 0, 0, 1.25, 2))
    ground.append(get_frame4.get_image(g, 32, 32, 0, 0, 1.25, 3))
    ground.append(get_frame4.get_image(g, 32, 32, 0, 0, 1.25, 4))
    ground.append(get_frame4.get_image(g, 32, 32, 0, 0, 1.25, 5))
    ground.append(get_frame4.get_image(g, 32, 32, 0, 0, 1.25, 6))
    ground.append(get_frame4.get_image(g, 32, 32, 0, 0, 1.25, 7))


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.music.load('Img\Main.mp3')
        pygame.mixer.music.play(-1)
        self.width = 1200
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.difficulty = 0
        self.health_inc = 4
        self.speed_inc = 4
        self.score = 0
        self.ground = Ground(self.width, self.height)
        self.bullets = []
        self.bosses = []
        self.boss1_bullets = []
        self.boss2_bullets = []
        self.boss3_bullets = []
        self.boss4_bullets = []
        self.offset = 45
        self.start_screen = True
        self.vic_screen = False
        self.end_screen = False
        self.running = False
        self.pframe = 0
        self.cycle_timer = 200
        self.x = 1
        self.y = 1
        self.counter = 0
        self.s_attack = 0
        self.vic_screen_cd = 0
        self.last_pupdate = pygame.time.get_ticks()
        self.boss_state2 = pygame.time.get_ticks()
        self.boss_state3 = pygame.time.get_ticks()
        self.boss_state4 = pygame.time.get_ticks()
        self.boss_state5 = pygame.time.get_ticks()
        self.boss_state6 = pygame.time.get_ticks()
        self.cooldown_time = pygame.time.get_ticks()
        self.cooldown_time1 = pygame.time.get_ticks()
        self.cooldown_time2 = pygame.time.get_ticks()
        self.cooldown_time3 = pygame.time.get_ticks()
        self.button_width = 300
        self.button_height = 50

    #On BootUp
    def starting_screen(self):
        self.button1_x = 30
        self.button1_y = self.height - self.button_height - 30
        self.button2_x = 30
        self.button2_y = self.button1_y - self.button_height - 30
        self.button3_x = 30
        self.button3_y = self.button2_y - self.button_height - 30

        self.ground.random_gen()
        self.ground.gen(self.screen)
        while self.start_screen:
            for self.boss in self.bosses:
                self.bosses.remove(self.boss)
            for boss1bullet in self.boss1_bullets:
                self.boss1_bullets.remove(boss1bullet)
            for boss2bullet in self.boss2_bullets:
                self.boss2_bullets.remove(boss2bullet)
            for boss3bullet in self.boss3_bullets:
                self.boss3_bullets.remove(boss3bullet)
            for boss4bullet in self.boss4_bullets:
                self.boss4_bullets.remove(boss4bullet)
            for bullet in self.bullets:
                self.bullets.remove(bullet)
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button3_x <= self.mouse_x <= self.button3_x + self.button_width and self.button3_y <= self.mouse_y <= self.button3_y + self.button_height:
                        self.difficulty = 1
                        self.running = True
                        self.start_screen = False
                        game.run()
                    if self.button2_x <= self.mouse_x <= self.button2_x + self.button_width and self.button2_y <= self.mouse_y <= self.button2_y + self.button_height:
                        self.difficulty = 2
                        self.running = True
                        self.start_screen = False
                        game.run()
                    if self.button1_x <= self.mouse_x <= self.button1_x + self.button_width and self.button1_y <= self.mouse_y <= self.button1_y + self.button_height:
                        self.difficulty = 3
                        self.running = True
                        self.start_screen = False
                        game.run()
                if event.type == pygame.QUIT:
                    self.start_screen = False
                    pygame.quit()
                    sys.exit()
            self.ground.gen(self.screen)
            if self.button1_x <= self.mouse_x <= self.button1_x + self.button_width and self.button1_y <= self.mouse_y <= self.button1_y + self.button_height:
                pygame.draw.rect(self.screen, (247, 210, 112), [self.button1_x, self.button1_y, self.button_width ,self.button_height])
                pygame.draw.rect(self.screen, (227, 180, 72), [self.button2_x, self.button2_y, self.button_width ,self.button_height])
                pygame.draw.rect(self.screen, (227, 180, 72), [self.button3_x, self.button3_y, self.button_width ,self.button_height])
            elif self.button2_x <= self.mouse_x <= self.button2_x + self.button_width and self.button2_y <= self.mouse_y <= self.button2_y + self.button_height:
                pygame.draw.rect(self.screen, (247, 210, 112), [self.button2_x, self.button2_y, self.button_width ,self.button_height])
                pygame.draw.rect(self.screen, (227, 180, 72), [self.button1_x, self.button1_y, self.button_width ,self.button_height])
                pygame.draw.rect(self.screen, (227, 180, 72), [self.button3_x, self.button3_y, self.button_width ,self.button_height])
            elif self.button3_x <= self.mouse_x <= self.button3_x + self.button_width and self.button3_y <= self.mouse_y <= self.button3_y + self.button_height:
                pygame.draw.rect(self.screen, (247, 210, 112), [self.button3_x, self.button3_y, self.button_width ,self.button_height])
                pygame.draw.rect(self.screen, (227, 180, 72), [self.button1_x, self.button1_y, self.button_width ,self.button_height])
                pygame.draw.rect(self.screen, (227, 180, 72), [self.button2_x, self.button2_y, self.button_width ,self.button_height])
            else:
                pygame.draw.rect(self.screen, (227, 180, 72), [self.button1_x, self.button1_y, self.button_width ,self.button_height])
                pygame.draw.rect(self.screen, (227, 180, 72), [self.button2_x, self.button2_y, self.button_width ,self.button_height])
                pygame.draw.rect(self.screen, (227, 180, 72), [self.button3_x, self.button3_y, self.button_width ,self.button_height])
            font = pygame.font.SysFont('Calibri',40)
            button3_text = font.render('Easy' , True , (0, 0, 0))
            self.screen.blit(button3_text, (self.button3_x + 30, self.button3_y + 5))
            button2_text = font.render('Medium' , True , (0, 0, 0))
            self.screen.blit(button2_text, (self.button2_x + 30, self.button2_y + 5))
            button1_text = font.render('Extreme' , True , (0, 0, 0))
            self.screen.blit(button1_text, (self.button1_x + 30, self.button1_y + 5))
            pygame.display.flip()
            self.clock.tick(60)

    #On Win
    def victory_screen(self):
        self.button4_x = self.width/2 - self.button_width/2
        self.button4_y = self.height - self.button_height - 30
        self.button5_x = self.width/2 - self.button_width/2
        self.button5_y = self.button4_y - self.button_height - 30
        while self.vic_screen:
            current_ptime = pygame.time.get_ticks()
            if current_ptime - self.last_pupdate >= 200:
                self.pframe += 1
                self.last_pupdate = current_ptime
                if self.pframe >= 4:
                    self.pframe = 0
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button5_x <= self.mouse_x <= self.button5_x + self.button_width and self.button5_y <= self.mouse_y <= self.button5_y + self.button_height:
                        self.vic_screen = False
                        self.running = False
                        self.start_screen = True
                        game.starting_screen()
                    if self.button4_x <= self.mouse_x <= self.button4_x + self.button_width and self.button4_y <= self.mouse_y <= self.button4_y + self.button_height:
                        self.vic_screen = False
                        self.running = False
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.QUIT:
                    self.vic_screen = False
                    self.running = False
                    pygame.quit()
                    sys.exit()
            self.ground.gen(self.screen)
            self.player.move(self.width, self.height)
            self.player.draw(self.screen, self.pframe)
            self.screen.blit(heart2[4], (10, 10))
            if self.player.health <= 0:
                self.screen.blit(heart[4], (self.width - 129, 10))
            elif self.player.health <= 25:
                self.screen.blit(heart[3], (self.width - 129, 10))
            elif self.player.health <= 50:
                self.screen.blit(heart[2], (self.width - 129, 10))
            elif self.player.health <= 75:
                self.screen.blit(heart[1], (self.width - 129, 10))
            elif self.player.health <= 100:
                self.screen.blit(heart[0], (self.width - 129, 10))
            if self.button4_x <= self.mouse_x <= self.button4_x + self.button_width and self.button4_y <= self.mouse_y <= self.button4_y + self.button_height:
                pygame.draw.rect(self.screen, (247, 210, 112), [self.button4_x, self.button4_y, self.button_width ,self.button_height])
                pygame.draw.rect(self.screen, (227, 180, 72), [self.button5_x, self.button5_y, self.button_width ,self.button_height])
            elif self.button5_x <= self.mouse_x <= self.button5_x + self.button_width and self.button5_y <= self.mouse_y <= self.button5_y + self.button_height:
                pygame.draw.rect(self.screen, (247, 210, 112), [self.button5_x, self.button5_y, self.button_width ,self.button_height])
                pygame.draw.rect(self.screen, (227, 180, 72), [self.button4_x, self.button4_y, self.button_width ,self.button_height])
            else:
                pygame.draw.rect(self.screen, (227, 180, 72), [self.button4_x, self.button4_y, self.button_width ,self.button_height])
                pygame.draw.rect(self.screen, (227, 180, 72), [self.button5_x, self.button5_y, self.button_width ,self.button_height])
            font = pygame.font.SysFont('Calibri',40)
            score_text = font.render('Final Score: ' + str(self.score) , True , (0, 0, 0))
            self.screen.blit(score_text, (self.width/2 - 135, 30))
            button5_text = font.render('Again?' , True , (0, 0, 0))
            self.screen.blit(button5_text, (self.button5_x + 40, self.button5_y + 5))
            button4_text = font.render('Leave?' , True , (0, 0, 0))
            self.screen.blit(button4_text, (self.button4_x + 40, self.button4_y + 5))
            pygame.display.flip()
            self.clock.tick(60)

    #On Death
    def end_game(self):
        self.button4_x = self.width/2 - self.button_width/2
        self.button4_y = self.height - self.button_height - 30
        self.button5_x = self.width/2 - self.button_width/2
        self.button5_y = self.button4_y - self.button_height - 30
        while self.end_screen:
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button5_x <= self.mouse_x <= self.button5_x + self.button_width and self.button5_y <= self.mouse_y <= self.button5_y + self.button_height:
                        self.end_screen = False
                        self.running = False
                        self.start_screen = True
                        game.starting_screen()
                    if self.button4_x <= self.mouse_x <= self.button4_x + self.button_width and self.button4_y <= self.mouse_y <= self.button4_y + self.button_height:
                        self.end_screen = False
                        self.running = False
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.QUIT:
                    self.end_screen = False
                    self.running = False
                    pygame.quit()
                    sys.exit()
            if self.boss.health <= 0:
                self.screen.blit(heart2[4], (10, 10))
            elif self.boss.health <= self.boss.orihealth/10:
                self.screen.blit(heart2[3], (10, 10))
            elif self.boss.health <= self.boss.orihealth/5:
                self.screen.blit(heart2[2], (10, 10))
            elif self.boss.health <= self.boss.orihealth/2:
                self.screen.blit(heart2[1], (10, 10))
            elif self.boss.health <= self.boss.orihealth:
                self.screen.blit(heart2[0], (10, 10))
            self.screen.blit(heart[4], (self.width - 129, 10))
            if self.button4_x <= self.mouse_x <= self.button4_x + self.button_width and self.button4_y <= self.mouse_y <= self.button4_y + self.button_height:
                pygame.draw.rect(self.screen, (247, 210, 112), [self.button4_x, self.button4_y, self.button_width ,self.button_height])
                pygame.draw.rect(self.screen, (227, 180, 72), [self.button5_x, self.button5_y, self.button_width ,self.button_height])
            elif self.button5_x <= self.mouse_x <= self.button5_x + self.button_width and self.button5_y <= self.mouse_y <= self.button5_y + self.button_height:
                pygame.draw.rect(self.screen, (247, 210, 112), [self.button5_x, self.button5_y, self.button_width ,self.button_height])
                pygame.draw.rect(self.screen, (227, 180, 72), [self.button4_x, self.button4_y, self.button_width ,self.button_height])
            else:
                pygame.draw.rect(self.screen, (227, 180, 72), [self.button4_x, self.button4_y, self.button_width ,self.button_height])
                pygame.draw.rect(self.screen, (227, 180, 72), [self.button5_x, self.button5_y, self.button_width ,self.button_height])
            font = pygame.font.SysFont('Calibri',40)
            score_text = font.render('Final Score: ' + str(self.score) , True , (0, 0, 0))
            self.screen.blit(score_text, (self.width/2 - 135, 30))
            button5_text = font.render('Again?' , True , (0, 0, 0))
            self.screen.blit(button5_text, (self.button5_x + 40, self.button5_y + 5))
            button4_text = font.render('Leave?' , True , (0, 0, 0))
            self.screen.blit(button4_text, (self.button4_x + 40, self.button4_y + 5))
            pygame.display.flip()
            self.clock.tick(60)

    #Trigger Phase
    def final_boss1(self):
        self.boss.speed = self.boss.orispeed*2
        self.cycle_timer = 50
        self.boss_frame = 17
        current_time_b6 = pygame.time.get_ticks()
        if current_time_b6 - self.boss_state6 > 200:
            for self.boss in self.bosses:
                self.boss1_bullets.append(Boss1Bullet(self.player, self.boss, 5, 0))
                self.boss1_bullets.append(Boss1Bullet(self.player, self.boss, -5, 0))
                self.boss1_bullets.append(Boss1Bullet(self.player, self.boss, 5, 0.1))
                self.boss1_bullets.append(Boss1Bullet(self.player, self.boss, -5, 0.1))
                self.boss1_bullets.append(Boss1Bullet(self.player, self.boss, 5, -0.1))
                self.boss1_bullets.append(Boss1Bullet(self.player, self.boss, -5, -0.1))
                self.boss1_bullets.append(Boss1Bullet(self.player, self.boss, 5, 0.5))
                self.boss1_bullets.append(Boss1Bullet(self.player, self.boss, -5, 0.5))
                self.boss1_bullets.append(Boss1Bullet(self.player, self.boss, 5, -0.5))
                self.boss1_bullets.append(Boss1Bullet(self.player, self.boss, -5, -0.5))
                self.boss3_bullets.append(Boss3Bullet(self.boss, self.x*1, self.y*0))
                self.boss3_bullets.append(Boss3Bullet(self.boss, self.x*0.5, self.y*0.5))
                self.boss3_bullets.append(Boss3Bullet(self.boss, self.x*0, self.y*1))
                self.boss3_bullets.append(Boss3Bullet(self.boss, self.x*-0.5, self.y*0.5))
                self.boss3_bullets.append(Boss3Bullet(self.boss, self.x*-1, self.y*0))
                self.boss3_bullets.append(Boss3Bullet(self.boss, self.x*-0.5, self.y*-0.5))
                self.boss3_bullets.append(Boss3Bullet(self.boss, self.x*0, self.y*-1))
                self.boss3_bullets.append(Boss3Bullet(self.boss, self.x*0.5, self.y*-0.5))
            self.counter += 1
            self.boss_state6 = current_time_b6

    def run(self):
        #Difficulty Check
        if self.difficulty == 1:
            self.health_inc = 1
            self.speed_inc = 2
            self.boss_x = self.width/2
            self.boss_y = 0
        if self.difficulty == 2:
            self.s_attack = 1
            self.health_inc = 2
            self.speed_inc = 1
            self.boss_x = self.width/2
            self.boss_y = 0
        if self.difficulty == 3:
            self.s_attack = 2
            self.health_inc = 3
            self.speed_inc = 0.75
            self.boss_x = 0
            self.boss_y = self.height/2        
            self.bosses.append(Boss(self.boss_x, self.boss_y, self.health_inc, self.speed_inc))
            self.boss_x = self.width
            self.boss_y = self.height/2
            self.speed_inc = 1
 
        self.player = Player(self.width, self.height)
        self.bosses.append(Boss(self.boss_x, self.boss_y, self.health_inc, self.speed_inc))
        while self.running:
            #Used To Change The Frame After A Time Period
            current_ptime = pygame.time.get_ticks()
            if current_ptime - self.last_pupdate >= 200:
                self.pframe += 1
                self.last_pupdate = current_ptime
                if self.pframe >= 4:
                    self.pframe = 0
            for self.boss in self.bosses:
                current_time = pygame.time.get_ticks()
                if current_time - self.boss.last_update >= self.cycle_timer:
                    self.boss.frame += 1
                    self.boss.last_update = current_time
                    if self.boss.frame >= self.boss.boss_frame:
                        self.boss.frame = 0
                        #Changes Boss State 1 to 5 After Every Completed Frame Cycle
                        if self.boss.boss_state in (1, 2, 3, 4, 5):
                            self.boss.boss_state = random.randrange(1, 6)
                            if self.boss.boss_state in (1, 2, 3, 5):
                                self.boss.boss_frame = 4
                            elif self.boss.boss_state in (4, 6):
                                self.boss.boss_frame = 17

                #Boss Attacks and Behaviour
                if self.boss.boss_state == 2:
                    current_time_b2 = pygame.time.get_ticks()
                    if current_time_b2 - self.boss_state2 > 500:
                        self.boss1_bullets.append(Boss1Bullet(self.player, self.boss, 5, 0))
                        self.boss_state2 = current_time_b2
                if self.boss.boss_state == 3:
                    current_time_b3 = pygame.time.get_ticks()
                    if current_time_b3 - self.boss_state3 > 200:
                        self.boss2_bullets.append(Boss2Bullet(self.player, self.boss, self.offset*0))
                        self.boss2_bullets.append(Boss2Bullet(self.player, self.boss, self.offset*-1))
                        self.boss2_bullets.append(Boss2Bullet(self.player, self.boss, self.offset*1))
                        self.boss_state3 = current_time_b3                
                if self.boss.boss_state == 4:
                    current_time_b4 = pygame.time.get_ticks()
                    if current_time_b4 - self.boss_state4 > 1500:
                        self.boss3_bullets.append(Boss3Bullet(self.boss, self.x*1, self.y*0))
                        self.boss3_bullets.append(Boss3Bullet(self.boss, self.x*0.5, self.y*0.5))
                        self.boss3_bullets.append(Boss3Bullet(self.boss, self.x*0, self.y*1))
                        self.boss3_bullets.append(Boss3Bullet(self.boss, self.x*-0.5, self.y*0.5))
                        self.boss3_bullets.append(Boss3Bullet(self.boss, self.x*-1, self.y*0))
                        self.boss3_bullets.append(Boss3Bullet(self.boss, self.x*-0.5, self.y*-0.5))
                        self.boss3_bullets.append(Boss3Bullet(self.boss, self.x*0, self.y*-1))
                        self.boss3_bullets.append(Boss3Bullet(self.boss, self.x*0.5, self.y*-0.5))
                        self.boss_state4 = current_time_b4
                if self.boss.boss_state == 5:
                    current_time_b5 = pygame.time.get_ticks()
                    if current_time_b5 - self.boss_state5 > 500:
                        self.boss4_bullets.append(Boss4Bullet(self.boss))
                        self.boss_state5 = current_time_b5
                if self.boss.boss_state == 6:
                    self.final_boss1()
                    if self.difficulty == 1:
                        if self.counter >= 5 and self.boss.frame <= 1:
                            self.boss.boss_state = 0
                    if self.difficulty == 2:
                        if self.counter >= 5 and self.boss.frame <= 1 and self.s_attack >= 1:
                            self.s_attack -= 1
                            self.boss.speed = self.boss.orispeed
                            self.boss.health += self.boss.orihealth/5
                            self.boss.boss_state = 3
                        elif self.counter >= 20 and self.boss.frame <= 1 and self.s_attack == 0:
                            self.boss.boss_state = 0
                    if self.difficulty == 3:
                        if self.counter >= 5 and self.boss.frame <= 1 and self.s_attack >= 1:
                            self.s_attack -= 1
                            self.boss.speed = self.boss.orispeed
                            self.boss.health += self.boss.orihealth/5
                            self.boss.boss_state = 3
                        elif self.counter >= 30 and self.boss.frame <= 1 and self.s_attack == 0:
                            self.boss.boss_state = 0
                if self.boss.boss_state == 0:
                    self.cycle_timer = 150
                    self.boss.boss_frame = 8
                    if self.boss.frame >= 6:
                        self.boss.frame = 6
                        self.vic_screen_cd += 1
                        if self.vic_screen_cd >= 300:
                            self.vic_screen_cd = 0
                            self.counter = 0
                            # Calculates Score
                            self.score = int(self.difficulty * self.player.health)
                            self.vic_screen = True
                            for boss4bullet in self.boss4_bullets:
                                self.boss4_bullets.remove(boss4bullet)
                            game.victory_screen()
                elif self.boss.health <= 0:
                    self.boss.center(self.width, self.height)
                elif self.boss.health <= self.boss.orihealth/10:
                    self.boss.speed = self.boss.orispeed*3
                    self.cycle_timer = 25
                elif self.boss.health <= self.boss.orihealth/5:
                    self.cycle_timer = 50
                elif self.boss.health <= self.boss.orihealth/2:
                    self.boss.speed = self.boss.orispeed*2
                    self.cycle_timer = 100
                if self.boss.health > 0:
                    self.boss.chase(self.player)

                #Bullet Collision Against Boss
                for bullet in self.bullets:
                    if bullet.rect.colliderect(self.boss.rect) and self.boss.boss_state != 0:
                        self.bullets.remove(bullet)
                        self.boss.health -= bullet.damage
                        if self.boss.health <= self.boss.orihealth/2 and self.s_attack >= 1:
                            self.boss.boss_state = 6
                        elif self.boss.health <= 1: 
                            self.boss.boss_state = 6

                #Bullet Collision Against Player
                for boss1bullet in self.boss1_bullets:
                    if boss1bullet.rect.colliderect(self.player.rect):
                        self.boss1_bullets.remove(boss1bullet)
                        self.player.health -= boss1bullet.damage
                for boss2bullet in self.boss2_bullets:
                    if boss2bullet.rect.colliderect(self.player.rect):
                        self.boss2_bullets.remove(boss2bullet)
                        self.player.health -= boss2bullet.damage
                for boss3bullet in self.boss3_bullets:
                    if boss3bullet.rect.colliderect(self.player.rect):
                        self.boss3_bullets.remove(boss3bullet)
                        self.player.health -= boss3bullet.damage
                for boss4bullet in self.boss4_bullets:
                    if boss4bullet.rect.colliderect(self.player.rect):
                        self.boss4_bullets.remove(boss4bullet)
                        self.player.health -= boss4bullet.damage
                    current_time_b6 = pygame.time.get_ticks()
                    if current_time_b6 - self.cooldown_time3 > 3500:
                        self.boss4_bullets.remove(boss4bullet)
                        self.cooldown_time3 = current_time_b6
                #Boss Collision Against Players
                if self.player.rect.colliderect(self.boss.rect) and self.boss.boss_state != 0:
                    self.player.health -= 5
            
            for event in pygame.event.get():
                #Quit
                if event.type == pygame.QUIT:
                    self.running = False
                #Dash
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        current_time = pygame.time.get_ticks()
                        if current_time - self.cooldown_time > 400:
                            keys = pygame.key.get_pressed()
                            if keys[pygame.K_a]:
                                if keys[pygame.K_w]:
                                    self.player.x -= 100
                                    self.player.y -= 100
                                elif keys[pygame.K_s]:
                                    self.player.x -= 100
                                    self.player.y += 100
                                else:   
                                    self.player.x -= 200
                            elif keys[pygame.K_d]:
                                if keys[pygame.K_w]:
                                    self.player.x += 100
                                    self.player.y -= 100
                                elif keys[pygame.K_s]:
                                    self.player.x += 100
                                    self.player.y += 100
                                else:   
                                    self.player.x += 200
                            elif keys[pygame.K_w]:
                                self.player.y -= 200
                            elif keys[pygame.K_s]:
                                self.player.y += 200
                            self.cooldown_time = current_time
                #Weapons
                self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    current_time0 = pygame.time.get_ticks()
                    if current_time0 - self.cooldown_time1 > 500:
                        if event.button == 1:
                            self.bullets.append(Bullet(self.player, self.mouse_x, self.mouse_y, 175, 0))
                        if event.button == 3:
                            self.bullets.append(Bullet(self.player, self.mouse_x, self.mouse_y, 75, 0))
                            self.bullets.append(Bullet(self.player, self.mouse_x, self.mouse_y, 75, 0.2))
                            self.bullets.append(Bullet(self.player, self.mouse_x, self.mouse_y, 75, -0.2))
                        self.cooldown_time1 = current_time0
            #Player
            self.player.move(self.width, self.height)
            if self.player.health <= 0:
                self.score = 0
                self.counter = 0
                self.end_screen = True
                self.end_game()
            
            #Drawing Layers
            self.ground.gen(self.screen)
            for bullet in self.bullets:
                bullet.draw(self.screen)
            for boss1bullet in self.boss1_bullets:
                boss1bullet.draw(self.screen, self.boss)
            for boss2bullet in self.boss2_bullets:
                boss2bullet.draw(self.screen, self.boss)
            for boss3bullet in self.boss3_bullets:
                boss3bullet.draw(self.screen, self.boss)
            for boss4bullet in self.boss4_bullets:
                boss4bullet.draw(self.screen, self.boss)
            for self.boss in self.bosses:
                self.boss.draw(self.screen)
            self.player.draw(self.screen, self.pframe)

            #Health UI
            for self.boss in self.bosses:
                if self.boss.health <= 0:
                    self.screen.blit(heart2[4], (10, 10 + ((129 + 10) * (self.bosses.index(self.boss)))))
                elif self.boss.health <= self.boss.orihealth/10:
                    self.screen.blit(heart2[3], (10, 10 + ((129 + 10) * (self.bosses.index(self.boss)))))
                elif self.boss.health <= self.boss.orihealth/5:
                    self.screen.blit(heart2[2], (10, 10 + ((129 + 10) * (self.bosses.index(self.boss)))))
                elif self.boss.health <= self.boss.orihealth/2:
                    self.screen.blit(heart2[1], (10, 10 + ((129 + 10) * (self.bosses.index(self.boss)))))
                elif self.boss.health <= self.boss.orihealth:
                    self.screen.blit(heart2[0], (10, 10 + ((129 + 10) * (self.bosses.index(self.boss)))))
            if self.player.health <= 0:
                self.screen.blit(heart[4], (self.width - 129, 10))
            elif self.player.health <= 25:
                self.screen.blit(heart[3], (self.width - 129, 10))
            elif self.player.health <= 50:
                self.screen.blit(heart[2], (self.width - 129, 10))
            elif self.player.health <= 75:
                self.screen.blit(heart[1], (self.width - 129, 10))
            elif self.player.health <= 100:
                self.screen.blit(heart[0], (self.width - 129, 10))


            pygame.display.flip()
            self.clock.tick(60)

class Ground:
    def __init__(self, width, height):
        self.ground_val = [0, 1, 2, 3, 8, 9, 10, 11, 16, 17, 18, 19, 24, 25, 26, 27]
        self.current_ground_val = random.choice(self.ground_val)
        self.current_ground_val1 = random.choice(self.ground_val)
        self.current_ground_val2 = random.choice(self.ground_val)
        self.current_ground_val3 = random.choice(self.ground_val)
        self.current_ground_val4 = random.choice(self.ground_val)
        self.current_ground_val5 = random.choice(self.ground_val)
        self.current_ground_val6 = random.choice(self.ground_val)
        self.current_ground_val7 = random.choice(self.ground_val)
        self.flower_val = [32, 33, 34, 35, 40, 41, 42, 43, 48, 49, 50, 51, 56, 57, 58, 59]
        self.current_flower_val = random.choice(self.flower_val)
        self.current_flower_val1 = random.choice(self.flower_val)
        self.current_flower_val2 = random.choice(self.flower_val)
        self.current_stone_val = 14
        self.current_stone_val1 = 38
        self.x = 40
        self.y = 40
        self.row = width/40
        self.column = height/40

    def random_gen(self):
        self.test2 = []
        for _ in range(int(self.column)):#20
            self.test = []
            for _ in range(int(self.row)): #30
                self.test.append(random.randrange(0, 13))
                #Grass 0 1 2 3 4 5 6 7
                #Flower 8 9 10
                #Stone 11 12
            self.test2.append(self.test)

    def gen(self, surface):
        for x in range(int(self.column)):
            for y in range(int(self.row)):
                if self.test2[x][y] == 0:
                    surface.blit(ground[self.current_ground_val], (self.x*y, self.y*x))
                if self.test2[x][y] == 1:
                    surface.blit(ground[self.current_ground_val1], (self.x*y, self.y*x))
                if self.test2[x][y] == 2:
                    surface.blit(ground[self.current_ground_val2], (self.x*y, self.y*x))
                if self.test2[x][y] == 3:
                    surface.blit(ground[self.current_ground_val3], (self.x*y, self.y*x))
                if self.test2[x][y] == 4:
                    surface.blit(ground[self.current_ground_val4], (self.x*y, self.y*x))
                if self.test2[x][y] == 5:
                    surface.blit(ground[self.current_ground_val5], (self.x*y, self.y*x))
                if self.test2[x][y] == 6:
                    surface.blit(ground[self.current_ground_val6], (self.x*y, self.y*x))
                if self.test2[x][y] == 7:
                    surface.blit(ground[self.current_ground_val7], (self.x*y, self.y*x))
                if self.test2[x][y] == 8:
                    surface.blit(ground[self.current_flower_val], (self.x*y, self.y*x))
                if self.test2[x][y] == 9:
                    surface.blit(ground[self.current_flower_val1], (self.x*y, self.y*x))
                if self.test2[x][y] == 10:
                    surface.blit(ground[self.current_flower_val2], (self.x*y, self.y*x))
                if self.test2[x][y] == 11:
                    surface.blit(ground[self.current_stone_val], (self.x*y, self.y*x))
                if self.test2[x][y] == 12:
                    surface.blit(ground[self.current_stone_val1], (self.x*y, self.y*x))

class Player:
    def __init__(self, width, height):
        self.width = 16
        self.height = 24
        self.x = width/2 - self.width
        self.y = height - self.height*2
        self.speed = 3
        self.health = 100
        self.state = 'idle'
        self.direction = 'down'
        self.rect = pygame.Rect(self.x + 4, self.y + 2, self.width, self.height)

    def move(self, width, height):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_s]:
            self.state = 'walk'
            if keys[pygame.K_w]:
                self.y -= self.speed
                self.direction = 'up'
            if keys[pygame.K_a]:
                self.x -= self.speed
                self.direction = 'left'
            if keys[pygame.K_d]:
                self.x += self.speed
                self.direction = 'right'
            if keys[pygame.K_s]:
                self.y += self.speed
                self.direction = 'down'
        else:
            self.state = 'idle'
        if self.x < 0:
            self.x = 0
        if self.x > width - self.width:
            self.x = width - self.width
        if self.y < 0:
            self.y = 0
        if self.y > height - self.height:
            self.y = height - self.height
        self.rect.x = self.x + 4
        self.rect.y = self.y + 2

    def draw(self, surface, pframe):
        if self.state == 'walk':
            if self.direction == 'up':
                surface.blit(walk_up_frame_cycle[pframe], (self.rect.x, self.rect.y))
            elif self.direction == 'left':
                surface.blit(walk_left_frame_cycle[pframe], (self.rect.x, self.rect.y))
            elif self.direction == 'right':
                surface.blit(walk_right_frame_cycle[pframe], (self.rect.x, self.rect.y))
            elif self.direction == 'down':
                surface.blit(walk_down_frame_cycle[pframe], (self.rect.x, self.rect.y))
        elif self.state == 'idle':
            if self.direction == 'up':
                surface.blit(idle_up_frame_cycle[pframe], (self.rect.x, self.rect.y))
            elif self.direction == 'left':
                surface.blit(idle_left_frame_cycle[pframe], (self.rect.x, self.rect.y))
            elif self.direction == 'right':   
                surface.blit(idle_right_frame_cycle[pframe], (self.rect.x, self.rect.y))
            elif self.direction == 'down':       
                surface.blit(idle_down_frame_cycle[pframe], (self.rect.x, self.rect.y))

class Boss():
    def __init__(self, x, y, health_inc, speed_inc):
        self.last_update = pygame.time.get_ticks()
        self.boss_frame = 4
        self.frame = 0
        self.boss_state = 1
        self.width = 100
        self.height = 100
        self.x = x - self.width/2
        self.y = y - self.height/2
        self.speed = 1 / speed_inc
        self.health = 2500 * health_inc
        self.orihealth = self.health
        self.orispeed = self.speed
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def chase(self, player):
        if self.x + self.width/2 < player.rect.x + player.width/2:
            self.x += self.speed
        if self.x + self.width/2 > player.rect.x + player.width/2:
            self.x -= self.speed
        if self.y + self.height/2 < player.rect.y + player.height/2:
            self.y += self.speed
        if self.y + self.width/2 > player.rect.y + player.width/2:
            self.y -= self.speed
        self.rect.x = self.x
        self.rect.y = self.y    
        
    def center(self, width, height):
        if self.x < width/2 - self.width/2:
            self.x += self.speed
        if self.x > width/2 - self.width/2:
            self.x -= self.speed
        if self.y < height/2 - self.height/2:
            self.y += self.speed
        if self.y > height/2 - self.height/2:
            self.y -= self.speed
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, surface):
        if self.boss_state in (1, 2, 3, 5):
            try:
                surface.blit(boss_chase_cycle[self.frame], (self.x - 30, self.y - 44))
            except IndexError:
                surface.blit(boss_chase_cycle[0], (self.x - 30, self.y - 44))
        elif self.boss_state in (4, 6):
            surface.blit(boss_attack_cycle[self.frame], (self.x - 30, self.y - 44))
        elif self.boss_state == 0:
            surface.blit(boss_death_cycle[self.frame], (self.x - 30, self.y - 44))

class Bullet():
    def __init__(self, player, mouse_x, mouse_y, damage, offset):
        self.x = player.x + player.width/2
        self.y = player.y + player.height/2
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.damage = damage
        self.speed = 10
        self.angle = math.atan2(player.y - mouse_y, player.x - mouse_x)
        self.x_vel = math.cos(self.angle + offset) * self.speed
        self.y_vel = math.sin(self.angle + offset) * self.speed
        self.rect = pygame.Rect(self.x, self.y, 10, 10)

    def draw(self, surface):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)
        self.rect.x = self.x
        self.rect.y = self.y
        pygame.draw.circle(surface, (255, 255, 255), (self.x + 10, self.y + 10), 5)

class Boss1Bullet():
    def __init__(self, player, boss, speed, offset):
        self.start_x = boss.x
        self.start_y = boss.y
        self.speed = speed
        self.damage = 35
        self.angle = math.atan2(boss.y - player.y, boss.x - player.x)
        self.x_vel = math.cos(self.angle + offset) * self.speed
        self.y_vel = math.sin(self.angle + offset) * self.speed
        self.rect = pygame.Rect(self.start_x, self.start_y, 30, 30)

    def draw(self, surface, boss):
        self.start_x -= int(self.x_vel)
        self.start_y -= int(self.y_vel)
        self.rect.x = self.start_x + 30
        self.rect.y = self.start_y + 30
        pygame.draw.circle(surface, (96, 177, 190), (self.start_x + boss.width/2, self.start_y + boss.height/2), 15)
        pygame.draw.circle(surface, (192, 253, 255), (self.start_x + boss.width/2, self.start_y + boss.height/2), 10)

class Boss2Bullet():
    def __init__(self, player, boss, offset):
        self.start_x = boss.x
        self.start_y = boss.y
        self.speed = 7
        self.damage = 15
        self.angle = math.atan2(boss.y - player.y, boss.x - player.x)
        self.x_vel = math.cos(self.angle + offset) * self.speed
        self.y_vel = math.sin(self.angle + offset) * self.speed
        self.rect = pygame.Rect(self.start_x, self.start_y, 20, 20)


    def draw(self, surface, boss):
        self.start_x -= int(self.x_vel)
        self.start_y -= int(self.y_vel)
        self.rect.x = self.start_x + 38
        self.rect.y = self.start_y + 38
        pygame.draw.circle(surface, (96, 177, 190), (self.start_x + boss.width/2, self.start_y + boss.height/2), 10)
        pygame.draw.circle(surface, (192, 253, 255), (self.start_x + boss.width/2, self.start_y + boss.height/2), 7)

class Boss3Bullet():
    def __init__(self, boss, x, y):
        self.x = x
        self.y = y
        self.start_x = boss.x
        self.start_y = boss.y
        self.speed = 7
        self.damage = 40
        self.rect = pygame.Rect(self.start_x, self.start_y, 30, 30)

    def draw(self, surface, boss):
        self.start_x -= int(self.speed * self.x)
        self.start_y -= int(self.speed * self.y)
        self.rect.x = self.start_x + 30
        self.rect.y = self.start_y + 30
        pygame.draw.circle(surface, (96, 177, 190), (self.start_x + boss.width/2, self.start_y + boss.height/2), 15)
        pygame.draw.circle(surface, (192, 253, 255), (self.start_x + boss.width/2, self.start_y + boss.height/2), 10)

class Boss4Bullet():
    def __init__(self, boss):
        self.x = boss.x
        self.y = boss.y
        self.damage = 50
        self.rect = pygame.Rect(self.x, self.y, 40, 40)

    def draw(self, surface, boss):
        self.rect.x = self.x + 20
        self.rect.y = self.y + 20
        pygame.draw.circle(surface, (96, 177, 190), (self.x + boss.width/2, self.y + boss.height/2), 20)
        pygame.draw.circle(surface, (192, 253, 255), (self.x + boss.width/2, self.y + boss.height/2), 15)

game = Game()
game.starting_screen()
pygame.quit()



#final difficulty increase 1h
#video 30mwwa
#report 1h
