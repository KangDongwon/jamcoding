import ColabTurtle.Turtle as t
import random

# 거북이 초기값 설정
t.initializeTurtle()
t.penup()
t.goto(15,15)
t.setheading(0)
t.speed(13)
t.width(3)
t.bgcolor("white")
t.color("black")

# 맵 그리기
# 맵 그릴 크기 설정
width = 763
height = 478

# 외곽선 그리기
t.pendown()
t.forward(width)
t.setheading(90)
t.forward(height)
t.setheading(180)
t.forward(width)
t.setheading(270)
t.forward(height)

# 가로 구분선 그리기
for i in range(1,12) :
    t.penup()
    t.goto(15,15+i*40)
    t.setheading(0)
    t.pendown()
    t.forward(width)
# 세로 구분선 그리기
for i in range(1,19) :
    t.penup()
    t.goto(15+i*40,15)
    t.setheading(90)
    t.pendown()
    t.forward(height)

t.penup()
t.goto(35,35+(11*40))

# 맵 생성 : 이차원 배열
map = []
map_hori = 19
map_vert = 12

for i in range(map_vert) :
    L = []
    for j in range(map_hori) :
        L.append(random.randrange(0,2))
    map.append(L)

map[0][0] = 0
map[map_vert-1][map_hori-1] = 0

# 생성한 맵을 화면에 그리기
for i in range(map_vert) :
    for j in range(map_hori) :
        t.penup()
        t.goto(35+j*40, 35+i*40)
        if map[i][j] == 0 :
            pass
        else :
            t.pendown()
            t.width(25)
            t.forward(2.5)

# 미로 길 찾기에 쓰일 초기값 설정
stack = []
start = (0,0)
end = (map_vert-1, map_hori-1)
# 이동 방향
dx = [1, 1, 0, -1, -1, -1,  0,  1]
dy = [0, 1, 1,  1,  0, -1, -1, -1]
# 거북이 위치 초기화
t.penup()
t.color("red")
t.goto(35,35)
t.setheading(0)
t.speed(3)
t.width(25)

# 스택과 재귀함수를 활용한 길 찾기 알고리즘
def dfs(visit) :
    nx, ny = visit
    if nx < 0 or ny < 0 or nx >= map_vert or ny >= map_hori :
        return False
    elif map[nx][ny] == 1 :
        return False
    elif visit == end :
        stack.append(visit)
        t.goto(35+40*ny, 35+40*nx)
        return True

    t.goto(35+40*ny, 35+40*nx)
    t.pendown()
    t.forward(2.5)
    t.penup()
    stack.append(visit)
    map[nx][ny] = 1

    for i in range(8) :
        x, y = nx+dy[i], ny+dx[i]
        if dfs((x, y)) :
            return True

    stack.pop()
    if stack :
        ret_x, ret_y = stack[-1]
        t.goto(35+40*ret_y, 35+40*ret_x)
    return False

if dfs(start) :
    print("출구를 찾았습니다.")
else :
    print("출구를 찾을 수 없습니다.")