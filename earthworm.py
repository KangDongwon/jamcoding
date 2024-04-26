import pygame 
from pygame.locals import *
import time
import random

#초기화
pygame.init()

#FPS 설정
FPS = 60
FramePerSec = pygame.time.Clock()

#색상 설정
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
SKY = (150,200,255)
RED = (255,0,0)

#폰트 설정
font = pygame.font.SysFont(None, 100)

#화면 설정
GameDisplay = pygame.display.set_mode((600,400))
pygame.display.set_caption("Pygame Example")

#게임 초기값 설정
move = [[50,50]]
speed = 0.3
dir = (1,0)
run = True
dead = False
moved_time = time.time()
food_time = time.time()
food = [-10, -10]

#게임 루프
while run :
    #게임 이벤트 처리
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT:
                dir = (-1,0)
            elif event.key == pygame.K_RIGHT :
                dir = (1,0)
            elif event.key == pygame.K_UP :
                dir = (0,-1)
            elif event.key == pygame.K_DOWN :
                dir = (0,1)

    if dead :
        continue

    #2초마다 먹이 생성
    if time.time() - food_time > 2 and food[0] < 0 :
        make = False
        while not make :
            food = [random.randrange(10,570,20), random.randrange(10,370,20)]
            for pos in move :
                if food[0] != pos[0] or food[1] != pos[1] :
                    make = True
                else :
                    make = False
                    break

        food_time = time.time()
        
    #좌표값 계산
    if time.time() - moved_time > speed :
        for i in range(len(move)-1,0,-1) :
            move[i] = move[i-1]
        
        head = move[0]
        move[0] = [head[i]+dir[i]*20 for i in range(len(head))]
        moved_time = time.time()
    
        #화면 벗어나면 게임 종료
        head = move[0]
        if head[0] < 0 or head[0] > 600 or head[1] < 0 or head[1] > 400 :
            dead = True

        #내몸과 부딪혀도 게임 종료
        for i in range(1, len(move)) :
            body = move[i]
            if head[0] == body[0] and head[1] == body[1] :
                dead = True
                break

        if dead :
            font = pygame.font.SysFont(None, 100)
            text_pos = (100,150)
            text = font.render("Game Finish", True, RED)
            GameDisplay.blit(text, text_pos)

        #먹은거 확인
        head = move[0]
        if head[0] == food[0] and head[1] == food[1] :
            move.append(move[-1])
            food = [-10, -10]
            food_time = time.time()
            speed = max(speed-0.05, 0.1)

    GameDisplay.fill(WHITE)
    pygame.draw.rect(GameDisplay, BLACK, [5,5,590,390],1)
    
    #화면 그리기
    text_pos = (10,10)
    font = pygame.font.SysFont(None, 50)
    text = font.render(str(len(move)), True, BLACK)
    GameDisplay.blit(text, text_pos)
    for pos in move :
        pygame.draw.circle(GameDisplay, BLUE, pos, 10)
    if food[0] > 0 :
        pygame.draw.circle(GameDisplay, RED, tuple(food), 10)
    pygame.display.update()
    FramePerSec.tick(FPS)

#게임 종료
pygame.quit()