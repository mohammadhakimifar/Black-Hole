import pygame
import math
import random
import time
pygame.init()
#####<< variable >>####
crash_sound=pygame.mixer.Sound("crash.wav")
shoot_sound=pygame.mixer.Sound("shoot.wav")
r=220
teta=0
teta_change=0
sheet_w=999
sheet_h=747
sheet_menu_w=1000
sheet_menu_h=747
sheet=pygame.display.set_mode((sheet_w,sheet_h))
sheet_menu=pygame.display.set_mode((sheet_menu_w,sheet_menu_h))
back_ground=pygame.image.load("back ground.jpg")
menu_back_ground=pygame.image.load("menu.png")
######(colors)#####
light_blue=(102, 204, 255)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
##################
pygame.display.set_caption("Black Hole")##(name of game)##
clock=pygame.time.Clock()
    
def distance(x1,y1,x2,y2):
    dist=math.sqrt((x1-x2)**2+(y1-y2)**2)
    return dist
def text_objects(text,font,color):
    textSurface = font.render(text, True , color)
    return textSurface, textSurface.get_rect()
def message_display(text,x,y,color,size):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(str(text),largeText,color)
    TextRect.center = ((x),(y))
    sheet.blit(TextSurf,TextRect)
    pygame.display.update()
def menu(): 
    play_x_chang=0
    play_y_chang=0
    play_x=200
    play_y=200
    play_color=white
    intro=True
    while intro:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        sheet_menu.blit(menu_back_ground,(-200,0))
        message_display("Mohammad Hakimifar: 09378948099",200,50,play_color,20)
        message_display("Play!",play_x,play_y,play_color,70)
        if play_x<mouse[0]:
            play_x_chang=5
        else:
            play_x_chang=-5
        if play_y<mouse[1]:
            play_y_chang=5
        else:
            play_y_chang=-5
        play_x+=play_x_chang
        play_y+=play_y_chang
        if play_x-50<mouse[0]<play_x+50 and play_y-50<mouse[1]<play_y+50 :
            play_color=blue
            if click[0]==1:
                game()
        else:
            play_color=white
        pygame.display.update()
        clock.tick(220)
def poolar_to_dekart(r,teta):
    X=r*math.cos(-teta*math.pi/180)
    Y=r*math.sin(-teta*math.pi/180)
    x=X+sheet_w/2
    y=Y+sheet_h/2
    return [int(x),int(y)]
def stuff(stuff_r,stuff_teta,rad,color):
    pygame.draw.circle(sheet,color,(stuff_r,stuff_teta),rad)
def crash():
    message_display("Game Over",sheet_w/2,sheet_h/2,red,50)
    pygame.mixer.music.stop
    pygame.mixer.Sound.stop(shoot_sound)
    pygame.mixer.Sound.play(crash_sound)
    time.sleep(2)
    intro=False
pygame.mixer.music.load("game.mp3")
def game():
    pygame.mixer.music.play(-1)
    object_r=10
    conter=0
    global r
    global teta
    global teta_change
    global sheet_h
    global sheet_w
    stuff_start_teta_1=random.randrange(0,360,_int=int)
    stuff_start_rad_1=600
    stuff_speed_1=-10
    stuff_rad_1=70
    stuff_start_teta_2=random.randrange(0,360,_int=int)
    stuff_start_rad_2=600
    stuff_speed_2=-7
    stuff_rad_2=90
    stuff_start_teta_3=random.randrange(0,360,_int=int)
    stuff_start_rad_3=600
    stuff_speed_3=-7
    stuff_rad_3=90
    stuff_start_teta_4=random.randrange(0,360,_int=int)
    stuff_start_rad_4=600
    stuff_speed_4=-7
    stuff_rad_4=90
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    teta_change=2
                elif event.key==pygame.K_RIGHT:
                    teta_change=-2
            
        c_1=poolar_to_dekart(stuff_start_rad_1,stuff_start_teta_1)
        c_2=poolar_to_dekart(stuff_start_rad_2,stuff_start_teta_2)
        c_3=poolar_to_dekart(stuff_start_rad_3,stuff_start_teta_3)
        c_4=poolar_to_dekart(stuff_start_rad_4,stuff_start_teta_4)
        teta+=teta_change
        if teta==360 or teta==-360:
            teta=0
            conter+=1
        message_display("Your Score=",100,50,white,20)
        message_display(conter,180,50,white,20)
        sheet.blit(back_ground,(0,0)) 
        if stuff_start_rad_1>=0:
            stuff_start_rad_1+=stuff_speed_1
            stuff_rad_1-=1
            stuff(c_1[0],c_1[1],stuff_rad_1,green)
            if stuff_start_rad_1<=0:
                stuff_rad_1=70
                stuff_start_rad_1=600
                stuff_start_teta_1=random.randrange(0,360,_int=int)
        if conter>5:
            object_r=12    
            if stuff_start_rad_2>=0:
                stuff_start_rad_2+=stuff_speed_2
                stuff_rad_2-=1
                stuff(c_2[0],c_2[1],stuff_rad_2,red)
                if stuff_start_rad_2<=0:
                    stuff_rad_2=90
                    stuff_start_rad_2=600
                    stuff_start_teta_2=random.randrange(0,360,_int=int)
        if conter>10:
            object_r=15    
            if stuff_start_rad_3>=0:
                stuff_start_rad_3+=stuff_speed_3
                stuff_rad_3-=1
                stuff(c_3[0],c_3[1],stuff_rad_3,black)
                if stuff_start_rad_3<=0:
                    stuff_rad_3=90
                    stuff_start_rad_3=600
                    stuff_start_teta_3=random.randrange(0,360,_int=int)
        if conter>15: 
            object_r=18   
            if stuff_start_rad_4>=0:
                stuff_start_rad_4+=stuff_speed_4
                stuff_rad_4-=1
                stuff(c_4[0],c_4[1],stuff_rad_4,light_blue)
                if stuff_start_rad_4<=0:
                    stuff_rad_4=90
                    stuff_start_rad_4=600
                    stuff_start_teta_4=random.randrange(0,360,_int=int)
        
        pygame.draw.circle(sheet,blue,poolar_to_dekart(r,teta),object_r)
        if distance(poolar_to_dekart(r,teta)[0],poolar_to_dekart(r,teta)[1],c_1[0],c_1[1])<=object_r+stuff_rad_1+90: 
            pygame.mixer.Sound.play(shoot_sound)
        if distance(poolar_to_dekart(r,teta)[0],poolar_to_dekart(r,teta)[1],c_2[0],c_2[1])<=object_r+stuff_rad_2+90: 
            pygame.mixer.Sound.play(shoot_sound)
        if distance(poolar_to_dekart(r,teta)[0],poolar_to_dekart(r,teta)[1],c_3[0],c_3[1])<=object_r+stuff_rad_3+90: 
            pygame.mixer.Sound.play(shoot_sound)  
        if distance(poolar_to_dekart(r,teta)[0],poolar_to_dekart(r,teta)[1],c_4[0],c_4[1])<=object_r+stuff_rad_4+90: 
            pygame.mixer.Sound.play(shoot_sound)
        if distance(poolar_to_dekart(r,teta)[0],poolar_to_dekart(r,teta)[1],c_1[0],c_1[1])<=object_r+stuff_rad_1:
            crash()
            game()
        if distance(poolar_to_dekart(r,teta)[0],poolar_to_dekart(r,teta)[1],c_2[0],c_2[1])<=object_r+stuff_rad_2:
            crash()
            game()
        if distance(poolar_to_dekart(r,teta)[0],poolar_to_dekart(r,teta)[1],c_3[0],c_3[1])<=object_r+stuff_rad_3:
            crash()
            game()
        if distance(poolar_to_dekart(r,teta)[0],poolar_to_dekart(r,teta)[1],c_4[0],c_4[1])<=object_r+stuff_rad_4:
            crash()
            game()
        pygame.display.update()
        clock.tick(120)
menu()
        