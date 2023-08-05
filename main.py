#key -> movement -> collision -> rendering


import pygame
from sys import exit
import random


#   #   #Initialising
pygame.init()
WINDOW = pygame.display.set_mode((1200,600))
CLOCK = pygame.time.Clock()
pygame.display.set_caption("Abstract Path")
FONT =  pygame.font.Font("data/fonts/Pixeltype.ttf", 50)


class Tiles:
    def __init__(self, img, init_pos):
        self.img = img
        self.init_pos = init_pos
        self.rect = img.get_rect(center =(init_pos))

class ParticleBottom:
    def __init__(self):
        self.particles = []
    def emit(self): # Moves and draws particles
        if self.particles:
            self.remove_particles()
            for particle in self.particles:
                particle[0][1] += particle[2][1]
                particle[0][0] += particle[2][0]
                particle[1] -= 0.2
                pygame.draw.circle(WINDOW, pygame.Color(self.color), particle[0],int(particle[1])) #Radius must be int


    def add_particles(self, color): #Adds particles
        #pos_x = 250
        #pos_y = 250
        self.color = color
        pos_x = player_rect.x
        pos_y = player_rect.y + 60

        radius = 10
        #direction = -3
        direction_x = random.randint(-4,-1)
        direction_y = random.randint(-3,1)

        particle_circle = [[pos_x, pos_y], radius, [direction_x, direction_y]]
        self.particles.append(particle_circle)


    def remove_particles(self): #Removes particles
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy

class ParticleRight:
    def __init__(self):
        self.particles = []
    def emit(self): # Moves and draws particles
        if self.particles:
            self.remove_particles()
            for particle in self.particles:
                particle[0][1] += particle[2][1]
                particle[0][0] += particle[2][0]
                particle[1] -= 0.2
                pygame.draw.circle(WINDOW, pygame.Color(self.color), particle[0],int(particle[1])) #Radius must be int


    def add_particles(self, color): #Adds particles
        #pos_x = 250
        #pos_y = 250
        self.color = color
        pos_x = player_rect.x + 60
        pos_y = player_rect.y + 30

        radius = 10
        #direction = -3
        direction_x = random.randint(-4,-1)
        direction_y = random.randint(-3,3)

        particle_circle = [[pos_x, pos_y], radius, [direction_x, direction_y]]
        self.particles.append(particle_circle)


    def remove_particles(self): #Removes particles
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy

class ParticleTop:
    def __init__(self):
        self.particles = []
    def emit(self): # Moves and draws particles
        if self.particles:
            self.remove_particles()
            for particle in self.particles:
                particle[0][1] += particle[2][1]
                particle[0][0] += particle[2][0]
                particle[1] -= 0.2
                pygame.draw.circle(WINDOW, pygame.Color(self.color), particle[0],int(particle[1])) #Radius must be int


    def add_particles(self, color): #Adds particles
        #pos_x = 250
        #pos_y = 250
        self.color = color
        pos_x = player_rect.x + 30
        pos_y = player_rect.y

        radius = 10
        #direction = -3
        direction_x = random.randint(-4,3)
        direction_y = random.randint(2,5)

        particle_circle = [[pos_x, pos_y], radius, [direction_x, direction_y]]
        self.particles.append(particle_circle)


    def remove_particles(self): #Removes particles
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy

class ParticleHome:
    def __init__(self):
        self.particles = []
    def emit(self): # Moves and draws particles
        if self.particles:
            self.remove_particles()
            for particle in self.particles:
                particle[0][1] += particle[2][1]
                particle[0][0] += particle[2][0]
                particle[1] -= 0.5
                pygame.draw.circle(WINDOW, (3, 252, 227), particle[0],int(particle[1])) #Radius must be int


    def add_particles(self): #Adds particles
        #pos_x = 250
        #pos_y = 250
        pos_x = pygame.mouse.get_pos()[0]
        pos_y = pygame.mouse.get_pos()[1]
        radius = 10
        #direction = -3
        direction_x = random.randint(-3,3)
        direction_y = random.randint(-3,3)

        particle_circle = [[pos_x, pos_y], radius, [direction_x, direction_y]]
        self.particles.append(particle_circle)


    def remove_particles(self): #Removes particles
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy

class ParticleFail:
    def __init__(self):
        self.particles = []
    def emit(self): # Moves and draws particles
        if self.particles:
            self.remove_particles()
            for particle in self.particles:
                particle[0][1] += particle[2][1]
                particle[0][0] += particle[2][0]
                particle[1] -= 0.2
                #pygame.draw.circle(WINDOW, (3, 252, 227), particle[0],int(particle[1])) #Radius must be int
                pygame.draw.rect(WINDOW, (3, 252, 227), (particle[0][0], particle[0][1], particle[1], particle[1])) #Radius must be int


    def add_particles(self): #Adds particles

        pos_x = player_rect.x + 30
        pos_y = player_rect.y

        for i in range(100):
            size = 12
            direction_x = random.randint(-12,12)
            direction_y = random.randint(-10,-2)
            if direction_y < -4:
                size += 3
            if direction_y < -8:
                size +=3
            particle_circle = [[pos_x, pos_y], size, [direction_x, direction_y]]
            self.particles.append(particle_circle)




    def remove_particles(self): #Removes particles
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy
    def remove_all(self):
        self.particles = []

class FinalParticle:
    def __init__(self):
        self.particles = []
    def emit(self): # Moves and draws particles
        if self.particles:
            self.remove_particles()
            for particle in self.particles:
                particle[0][1] += particle[2][1]
                particle[0][0] += particle[2][0]
                particle[1] -= 0.2
                pygame.draw.circle(WINDOW, (136, 44, 153), particle[0],int(particle[1])) #Radius must be int


    def add_particles(self): #Adds particles
        #pos_x = 250
        #pos_y = 250
        pos_x = 950
        pos_y = 300
        radius = 10
        #direction = -3
        direction_x = random.randint(-3,3)
        direction_y = random.randint(-3,3)

        particle_circle = [[pos_x, pos_y], radius, [direction_x, direction_y]]
        self.particles.append(particle_circle)


    def remove_particles(self): #Removes particles
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy


#   #   #Variables
level = 0
###Player
player = pygame.image.load("data/images/sprites/player.png").convert_alpha()
player_rect = player.get_rect(topleft=(0,200)) #250
player_movement = [0,0]
y_momentum = 0
dead = False
pygame.display.set_icon(player)




###Background
home = pygame.image.load("data/images/background/Home.png").convert_alpha()
#Welcome! Place tiles to let the player cross to the other side
#Text
Text_1 = FONT.render("Welcome! Place tiles to let the player cross to the other side ", False , (30,30,30))
Text_1_rect = Text_1.get_rect(center = (600, 100))

Text_2 = FONT.render(""" Press "R" to restart, if you fail or get stuck""", False , (255,255,255))
Text_2_rect = Text_2.get_rect(center = (600,500))

Text_3 = FONT.render(" Be aware of placing tiles too close together", False , (163, 163, 163))
Text_3_rect = Text_3.get_rect(center = (600,100))

Text_4 = FONT.render(" Watch out for obstacles in your way", False , (30,30,30))
Text_4_rect = Text_4.get_rect(center = (600,575))

Text_5 = FONT.render(" You can also use obstacles to assist you", False , (163, 163, 163))
Text_5_rect = Text_5.get_rect(center = (600,575))

Text_6 = FONT.render(" Cant jump if too close to a wall :/", False , (163, 163, 163))
Text_6_rect = Text_6.get_rect(center = (600,75))

Text_7 = FONT.render(" UP! UP! UP!", False , (30,30,30))
Text_7_rect = Text_7.get_rect(center = (550,75))

Text_8 = FONT.render(" Wooooooooooooo!", False , (163, 163, 163))
Text_8_rect = Text_8.get_rect(center = (550,75))

Text_9 = FONT.render("Back to the start but with a twist", False , (163, 163, 163))
Text_9_rect = Text_9.get_rect(center = (550,75))

Text_10 = FONT.render("How well do you remember this?", False , (163, 163, 163))
Text_10_rect = Text_10.get_rect(center = (600,100))

Text_11 = FONT.render("By failing you can see where the tiles are", False , (30,30,30))
Text_11_rect = Text_11.get_rect(center = (600,575))

Text_12 = FONT.render("^", False , (30,30,30))
Text_12_rect = Text_12.get_rect(center = (1100,300))

Text_13 = FONT.render(""" Well Done! You have completed Absrtact Path""", False , (255,255,255))
Text_13_rect = Text_13.get_rect(center = (600,100))

Text_14 = FONT.render(""" Made by FrogTesseract """, False , (255,255,255))
Text_14_rect = Text_14.get_rect(center = (600,500))







#Buttons
start = pygame.image.load("data/images/background/start.png").convert_alpha()
starth = pygame.image.load("data/images/background/starth.png").convert_alpha()
start_rect = start.get_rect(center = (600, 200))


###Tiles
tile_amount = 3
block1 = pygame.image.load("data/images/sprites/block.png").convert_alpha()
block1w = pygame.image.load("data/images/sprites/blockw.png").convert_alpha()
platform = pygame.image.load("data/images/sprites/platform.png").convert_alpha()
platformw = pygame.image.load("data/images/sprites/platformw.png").convert_alpha()
verticalblock = pygame.image.load("data/images/sprites/verticalblock.png").convert_alpha()
verticalblockw = pygame.image.load("data/images/sprites/verticalblockw.png").convert_alpha()

collisionrect = pygame.image.load("data/images/sprites/collisionrect.png").convert_alpha()
collisionrect_rect = collisionrect.get_rect(center = (950, 300))

tiles = []


###Cursor
cursor = pygame.image.load("data/images/sprites/cursor.png").convert_alpha()
cursor1 = pygame.image.load("data/images/sprites/cursor1.png").convert_alpha()
cursor2 = pygame.image.load("data/images/sprites/cursor2.png").convert_alpha()
cursor3 = pygame.image.load("data/images/sprites/cursor3.png").convert_alpha()
cursor_rect = cursor.get_rect(center=(0,0))

cursors = [cursor, cursor1, cursor2, cursor3]
current_cursor = cursors[tile_amount]



###Finish
# finish1 = pygame.image.load("data/images/sprites/finish1.png").convert_alpha()
# finish_rect = player.get_rect(center=(1100,320))

###Music
music = pygame.mixer.music.load("data/audio/GameJam_e1.mp3")
pygame.mixer.music.play(-1)
explosion = pygame.mixer.Sound("data/audio/explosion.wav")
jumpsound = pygame.mixer.Sound("data/audio/jump.wav")




#   #   #Functions
def collision_test(player, tiles):
    hit_list = []
    for tile in tiles:
        if player.colliderect(tile.rect):
            hit_list.append(tile.rect)
    return hit_list #Tests for collisions between player and tiles

def move(player, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    player.x += movement[0] #Move on x-axis
    hit_list = collision_test(player, tiles) #Find colliding tiles
    for tile in hit_list: # Loop for each colliding tile
        if movement[0] > 0: #If moving right
            player.right = tile.left # Set right edge of rectangle to left edge of colliding tile
            collision_types['right'] = True
        elif movement[0] < 0:
            player.left = tile.right
            collision_types['left'] = True
    player.y += movement[1] # Move on y-axis
    hit_list = collision_test(player, tiles) #Find colliding tiles
    for tile in hit_list: # Loop for each colliding tile
        if movement[1] > 0:
            player.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            player.top = tile.bottom
            collision_types['top'] = True
    jump(player,collision_types, hit_list)

    return player, collision_types #return player and collision dict #Moves the player and adresses collisions

def jump(player, collision_types, tiles):
    global y_momentum
    if collision_types["bottom"]:
        for tile in tiles:
            if tile.right - player.left < 20:
                y_momentum -= 27
                #jumpsound.play()
                 #print("a") #Causes the player to jump at the end of the current block its on

def display_tiles(tiles):
    for tile in tiles:
        WINDOW.blit(tile.img, tile.rect)

def level_move(level, tiles, tile_amount):
    if player_rect.x > 1300 and collisions["bottom"]:
        level += 1
        tiles, tile_amount = reset(tiles, tile_amount)
        tiles = level_setup(level, tiles)

    return level, tiles, tile_amount

def level_setup(level, tiles):
    if level == 1:
        tiles = [Tiles(block1, (200,325)), Tiles(block1, (1300,325))]
    elif level == 2:
        tiles = [Tiles(block1w, (70,325)), Tiles(block1w, (1300,325))]
    elif level == 3:
        tiles = [Tiles(block1, (70, 325)), Tiles(verticalblock, (575, 100)),Tiles(block1, (1250,325))]
    elif level == 4:
        tiles = [Tiles(block1w, (-100,325)) , Tiles(platformw, (450, 150)) , Tiles(block1w, (1300,325))]
    elif level == 5:
        tiles = [Tiles(block1, (-100,325)), Tiles(verticalblock, (375,100)),Tiles(verticalblock, (550,700)), Tiles(block1, (1325, 325))]
    elif level == 6:
        tiles = [Tiles(block1w, (-100,325)) , Tiles(verticalblockw, (300,100)), Tiles(verticalblockw, (600,450)), Tiles(verticalblockw, (900,100)), Tiles(block1w, (1250,525))]
    elif level  == 7:
        tiles = [Tiles(block1, (-50,525)),Tiles(verticalblock, (100,150)),Tiles(platform, (500, 400)), Tiles(block1, (1250,200))]
    elif level == 8:
        tiles = [Tiles(block1w, (150, 150)), Tiles(block1w, (550, 150)),Tiles(block1w, (950, 150)),Tiles(block1w, (1000, 150)),
         Tiles(platformw, (0, 350)), Tiles(platformw, (75, 350)), Tiles(platformw, (150, 350)),
         Tiles(platformw, (225, 350)), Tiles(platformw, (300, 350)),Tiles(platformw, (305, 350)),
         Tiles(platformw, (380, 350)), Tiles(platformw, (455, 350)), Tiles(platformw, (520, 350)),
         Tiles(platformw, (585, 350)), Tiles(platformw, (660, 350)), Tiles(platformw, (735, 350)),
         Tiles(platformw, (810, 350)), Tiles(platformw, (885, 350)), Tiles(platformw, (960, 350)),
         Tiles(platformw, (1035, 350)),Tiles(platformw, (1110, 350)), Tiles(block1w, (1285, 350)
            )]
    elif level == 9:
        tiles = [Tiles(block1w, (200,325)), Tiles(block1w, (1300,325))]
    elif level == 10:
        tiles = [Tiles(block1, (70,325)), Tiles(block1, (1300,325))]
    elif level == 11:
        tiles = [Tiles(block1w, (70, 325)), Tiles(verticalblockw, (575, 100)),Tiles(block1w, (1250,325))]
    elif level == 12:
        tiles = [Tiles(block1, (-100,325)) , Tiles(platform, (450, 150)) , Tiles(block1, (1300,325))]
    elif level == 13:
        tiles = [Tiles(block1w, (-100,325)), Tiles(verticalblockw, (375,100)),Tiles(verticalblockw, (550,700)), Tiles(block1w, (1325, 325))]
    elif level == 14:
        tiles = [Tiles(block1, (-100,325)) , Tiles(verticalblock, (300,100)), Tiles(verticalblock, (600,450)), Tiles(verticalblock, (900,100)), Tiles(block1, (1250,525))]
    elif level == 15:
        tiles = [Tiles(block1w, (-50,525)),Tiles(verticalblockw, (100,150)),Tiles(platformw, (500, 400)), Tiles(block1w, (1250,200))]
    elif level == 16:
        tiles = [Tiles(block1w, (150, 325)), Tiles(block1w, (550, 325))]



    return tiles

def reset(tiles, tile_amount):
    global current_cursor
    global particlefail
    global count
    count = 0
    tiles = []
    player_rect.topleft = (0,200)
    tile_amount = 3
    current_cursor = cursors[tile_amount]
    particlefail.remove_all()

    return tiles, tile_amount

def text(level):
    if level == 0:WINDOW.blit(Text_2, Text_2_rect)
    #if level == 1:WINDOW.blit(Text_1, Text_1_rect)
    if level == 2:WINDOW.blit(Text_3, Text_3_rect)
    if level == 3:WINDOW.blit(Text_4, Text_4_rect)
    if level == 4:WINDOW.blit(Text_5, Text_5_rect)
    if level == 6:WINDOW.blit(Text_6, Text_6_rect)
    if level == 7:WINDOW.blit(Text_7, Text_7_rect)
    if level == 8:WINDOW.blit(Text_8, Text_8_rect)
    if level == 9:WINDOW.blit(Text_9, Text_9_rect)
    if level == 10:WINDOW.blit(Text_10, Text_10_rect)
    if level == 11:WINDOW.blit(Text_11, Text_11_rect)
    if level == 15:WINDOW.blit(Text_12, Text_12_rect)
    if level == -1:
        WINDOW.blit(Text_13, Text_13_rect)
        WINDOW.blit(Text_14, Text_14_rect)

def background(level):
    if level != 0 and level % 2 == 0:
        WINDOW.fill((0,0,0))
    elif level != 0 and not level % 2 == 0:
        WINDOW.fill((255,255,255))





#   #   #Main loop


particle1 = ParticleBottom()
particle2 = ParticleRight()
particle3 = ParticleTop()
particlehome = ParticleHome()
particlefail = ParticleFail()
finalparticles = FinalParticle()

PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT, 25)


tiles, tile_amount = reset(tiles, tile_amount)
tiles = level_setup(level, tiles)


pygame.mouse.set_visible(False)
while True:
    #print("FPS:", int(CLOCK.get_fps()))
    mouse_pos = pygame.mouse.get_pos()

    ### Events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           exit()
        if level > 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tile_amount > 0:
                    if level < 9:
                        if level % 2 == 0 :
                            tiles.append(Tiles(platformw, (mouse_pos)))
                            tile_amount -= 1
                        else:
                            tiles.append(Tiles(platform, (mouse_pos)))
                            tile_amount -= 1
                    elif level > 8:
                        if level % 2 == 0:
                            tiles.append(Tiles(platform, (mouse_pos)))
                            tile_amount -= 1
                        else:
                            tiles.append(Tiles(platformw, (mouse_pos)))
                            tile_amount -= 1


                current_cursor = cursors[tile_amount]
            if event.type == PARTICLE_EVENT:
                if collisions["bottom"]:
                    if level % 2 == 0:
                        particle1.add_particles("White")
                    else:
                        particle1.add_particles("Black")
                if collisions["right"]:
                    if level % 2 == 0:
                        particle2.add_particles("White")
                    else:
                        particle2.add_particles("Black")
                if collisions["top"]:
                    if level % 2 == 0:
                        particle3.add_particles("White")
                    else:
                        particle3.add_particles("Black")
                if level == 16:
                    for i in range(10):
                        finalparticles.add_particles()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    tiles, tile_amount = reset(tiles, tile_amount)
                    tiles = level_setup(level, tiles)

        elif level == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(mouse_pos):
                    level = 1
                    tiles, tile_amount = reset(tiles, tile_amount)
                    tiles = level_setup(level, tiles)
            if event.type == PARTICLE_EVENT:
                particlehome.add_particles()
        elif level == -1:
            if event.type == PARTICLE_EVENT:
                particlehome.add_particles()




    ### Gameplay

    if level > 0:
        player_movement = [4, 0]
        player_movement[1] += y_momentum
        y_momentum += 1

        if y_momentum > 10: y_momentum = 10
        player_rect, collisions = move(player_rect, player_movement, tiles)
        cursor_rect.center = mouse_pos

        background(level)
        particle1.emit()
        particle2.emit()
        particle3.emit()
        particlefail.emit()
        finalparticles.emit()

        WINDOW.blit(player, player_rect)
        text(level)
        display_tiles(tiles)
        #WINDOW.blit(finish1, finish_rect)
        #WINDOW.blit(try cursors[len(tiles)-1] except cursor, cursor_rect)

        WINDOW.blit(current_cursor, cursor_rect)


        if player_rect.y > 600 and player_rect.y < 700:
            particlefail.add_particles()
            if count == 0:
                explosion.play()
                count = 1

        level, tiles, tile_amount = level_move(level, tiles, tile_amount)


    if level == 16:
        if collisionrect_rect.colliderect(player_rect):
            level = -1



    if level == 0:
        WINDOW.fill((30,30,30))
        text(level)
        if start_rect.collidepoint(mouse_pos):
            WINDOW.blit(starth, start_rect)
        else:
            WINDOW.blit(start, start_rect)
        particlehome.emit()

    if level == -1:
        WINDOW.fill((30,30,30))
        text(level)
        particlehome.emit()



    pygame.display.update()
    CLOCK.tick(60)
