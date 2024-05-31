import pygame
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
font = pygame.font.SysFont(None, 50)

#화면 설정
GameDisplay = pygame.display.set_mode((510,510))
pygame.display.set_caption("Pygame Example")

#게임 초기값 설정
pos = [0,0]
start = 18
distance = 25
run = True
finish = False

#블록 생성
block = []
for i in range(20):
    L = []
    for j in range(20):
        L.append(random.randrange(0,2))
    block.append(L)

block[0][0] = 0
block[-1][-1] = 0

def destroy_block(pos, block) :
    dirs = [[0,1], [1,0], [0,-1], [-1,0]]
    for dir in dirs :
        try:
            x = pos[0]+dir[0]
            y = pos[1]+dir[1]
            if x != -1 and y != -1 :
                block[x][y] = 0
        except:
            pass
    

#게임 루프
while run :
    #키보드 이벤트 처리
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT:
                if pos[1]-1 > -1 and block[pos[0]][pos[1]-1] != 1 :
                    pos = [pos[0], pos[1]-1]
            elif event.key == pygame.K_RIGHT :
                if pos[1]+1 < 20 and block[pos[0]][pos[1]+1] != 1 :
                    pos = [pos[0], pos[1]+1]
            elif event.key == pygame.K_UP :
                if pos[0]-1 > -1 and block[pos[0]-1][pos[1]] != 1 :
                    pos = [pos[0]-1, pos[1]]
            elif event.key == pygame.K_DOWN :
                if pos[0]+1 < 20 and block[pos[0]+1][pos[1]] != 1 :
                    pos = [pos[0]+1, pos[1]]
            elif event.key == pygame.K_d :
                destroy_block(pos, block);

    if pos[0] == 19 and pos[1] == 19 :
        finish = True
    
    #화면 초기화
    GameDisplay.fill(WHITE)
    

    #화면 그리기
    #맵 그리기
    for i in range(5, 510,25):
        pygame.draw.line(GameDisplay, BLACK, [5,i], [505,i], 2)
        pygame.draw.line(GameDisplay, BLACK, [i,5], [i,505], 2)

    #블록 그리기
    for i in range(20):
        for j in range(20):
            if block[i][j] == 1 :
                pygame.draw.circle(GameDisplay, BLACK, [start+j*distance, start+i*distance], 10)
            

    #사용자 그리기
    pygame.draw.circle(GameDisplay, BLUE, [start+pos[1]*distance, start+pos[0]*distance], 10)

    if finish :
        pygame.draw.rect(GameDisplay, WHITE, [100, 100, 290, 40])
        game_text = font.render("Congratulations!", True, RED)
        GameDisplay.blit(game_text, [100,100])
        
    pygame.display.update()
    FramePerSec.tick(FPS)

#게임 종료
pygame.quit()
