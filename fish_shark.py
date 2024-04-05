import turtle
import time
import random

# 점수 변수
score = 0
text_score = turtle.Turtle()
text_score.penup()
text_score.hideturtle()
text_score.setposition(-280, 180)
text_score.write("Ready!", move=False, align="left", font=("Arial",10,"normal"))

def updateScore() :
    global score
    score += 10
    text_score.clear()
    text_score.write(score, move=False, align="left", font=("Arial",10,"normal"))

# 화면 설정
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("light blue")

# 거북이 설정
turtle.speed(0)
turtle.penup()
turtle.setposition(-200, 0)
turtle.shape("turtle")
turtle.color("green")

# 거북이 이동 함수
def moveRight():
    x = turtle.xcor()
    x += 2  
    turtle.setx(x)
    
def moveLeft():
    x = turtle.xcor()
    x -= 2  
    turtle.setx(x)
    
def moveUp():
    y = turtle.ycor()
    y += 2  
    turtle.sety(y)
    
def moveDown():
    y = turtle.ycor()
    y -= 2  
    turtle.sety(y)


# 먹이 설정
fish = turtle.Turtle()
fish.hideturtle()
fish.penup()
fish.speed(0)
fish.shape("circle")
fish.color("black")


# 먹이 생성 함수
def makeFish() :
    fish.setposition(300, random.randrange(-180, 180))
    fish.showturtle()

# 먹이 이동 함수
def moveFish() :
    if fish.isvisible() :
        x = fish.xcor()
        x -= 5  
        fish.setx(x)

        if x < -300 :
            fish.hideturtle()

# 먹이를 먹었는지 체크하는 함수
def eatFish() :
    if fish.isvisible() and is_collision(turtle, fish, 0) :
        fish.hideturtle()
        updateScore()


def is_collision(t1, t2, level) :
    if t1.distance(t2) < 20+(level*10) :
        return True
    else :
        return False

# 상어 설정
shark_list = []

for i in range(10) :
    shark = turtle.Turtle()
    shark.hideturtle()
    shark.penup()
    shark.setheading(180)
    shark.speed(10)
    shark.shape("arrow")
    shark.color("red")
    shark.setposition(400, random.randrange(-180, 180))
    shark_list.append(shark)


# 상어 생성 함수
def makeShark(speed) :
    for shark in shark_list :
        if shark.isvisible() == False :
            shark.speed(speed)
            shark.shapesize(speed, speed)
            shark.showturtle()
            break


# 상어에게 먹혔는지 체크하는 함수
def getEatenShark(level) :
    i = 0
    for shark in shark_list :
        if shark.isvisible() and is_collision(turtle, shark, i) :
            return True
        i += 1

# 상어 이동 함수
def moveShark(speed) :
    for shark in shark_list :
        if shark.isvisible() :
            x = shark.xcor()
            if x < -300 :
                shark.hideturtle()
                shark.speed(10)
                shark.setposition(400, random.randrange(-180, 180))
                shark.showturtle()
                shark.speed(speed)
            else :
                x -= speed
                shark.setx(x)


level = 0
# 난이도 업 함수
def difficultyUp() :
    lv = score / 10 
    global level
    if level < 10 and level != lv :
        level += 1
        makeShark(level)
        
        
    
# 시간 설정
prev_time = 0
cur_time = 0
finish = False

def turtleLoop() :
    global prev_time
    global cur_time
    global finish
    if prev_time !=0 and cur_time !=0 :
        if fish.isvisible() == False and cur_time - prev_time > 2 :
            makeFish()
            
        cur_time = time.time()
    else :
        prev_time = time.time()
        cur_time = time.time()

    eatFish()
    moveFish()

    if score > 0 and score % 10 == 0 :
        difficultyUp()

    if getEatenShark(level) :
        finish = True

    if finish == True :
        turtle.done()
    else :
        moveShark(level+6)
        turtle.ontimer(turtleLoop, 100)
        


# 키보드 이벤트 처리
screen.listen()
screen.onkeypress(moveRight, "Right")
screen.onkeypress(moveLeft, "Left")
screen.onkeypress(moveUp, "Up")
screen.onkeypress(moveDown, "Down")

text_score.clear()
text_score.write("0", move=False, align="left", font=("Arial",10,"normal"))
turtleLoop()



