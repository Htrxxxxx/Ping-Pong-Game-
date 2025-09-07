import turtle 

screen = turtle.Screen()
screen.title("Ping Pong Game")
screen.setup(width= 800 , height=600) 
screen.tracer(0) # No delay for drawing 
screen.bgcolor(.1 , .2 , .2) 

# setup game objects  
# ball 
ball = turtle.Turtle() 
ball.speed(0) # fastest as possible 
ball.shape("square") 
ball.color("white")
ball.shapesize(stretch_len=1 , stretch_wid=1) # actual stretch is * by 20 px 
ball.goto(0 , 0) 
ball.penup() 
ball_dx , ball_dy = 1 , 1 
ball_speed = .5 
#center line 
center_line = turtle.Turtle() 
center_line.speed(0) 
center_line.shape("square")
center_line.color("white") 
center_line.shapesize(stretch_len=.1 , stretch_wid=25)
center_line.penup() 
center_line.goto(0 , 0)

# Player 1 
player1 = turtle.Turtle() 
player1.speed(0) 
player1.color("red") 
player1.shape("square")
player1.shapesize(stretch_len=1 , stretch_wid=5) 
player1.penup()
player1.goto(x = -350 , y = 0)
p1_score , p2_score = 0 , 0
#Player 2 
player2 = turtle.Turtle() 
player2.speed(0) 
player2.color("blue") 
player2.shape("square")
player2.shapesize(stretch_len=1 , stretch_wid=5) 
player2.penup()
player2.goto(x = 350 , y = 0) 

# score board 
board = turtle.Turtle() 
board.speed(0)
board.color("white")
board.penup()
board.goto(0 , 250) 
board.write("Player1 : 0  Player2 : 0" , align="center" , font= ("Courier" , 14 , "normal")) 
board.hideturtle() 

# Players Movements 
shift  = 20 
def move_up_p1():
    player1.sety(player1.ycor() + shift) 

def move_down_p1():
    player1.sety(player1.ycor() - shift) 


def move_up_p2():
    player2.sety(player2.ycor() + shift) 

def move_down_p2():
    player2.sety(player2.ycor() - shift) 


# Interactive with Players inputs 
screen.listen() 
screen.onkeypress(move_up_p1 , "w")
screen.onkeypress(move_down_p1 , "s")
screen.onkeypress(move_up_p2 , "Up")
screen.onkeypress(move_down_p2 , "Down")
 
# Game Loop 
while True :
    screen.update()

    # ball movement
    ball.setx(ball.xcor() + (ball_dx * ball_speed))
    ball.sety(ball.ycor() + (ball_dy * ball_speed))

    # borders collisions 

    if(ball.ycor() > 290):
        ball.sety(290) 
        ball_dy *= -1 

    if(ball.ycor() < -290):
        ball.sety(-290) 
        ball_dy *= -1

    if(ball.xcor() < -340 and ball.xcor() > -350
        and ball.ycor() > (player1.ycor() - 60) 
        and ball.ycor() < (player1.ycor() + 60)):
        ball.setx(-340)
        ball_dx *= -1

    if (ball.xcor() > 340 and ball.xcor() < 350 
        and ball.ycor() > (player2.ycor() - 60) 
        and ball.ycor() < (player2.ycor() + 60)):
        ball.setx(340)
        ball_dx *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_dx *= -1
        board.clear()
        p1_score+=1 
        board.write(f"Player1: {p1_score} Player2: {p2_score}",
                    align="center", font=("Courier", 14, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball_dx *= -1
        board.clear()
        p2_score+=1 
        board.write(f"Player1: {p1_score} Player2: {p2_score}",
                    align="center", font=("Courier", 14, "normal"))


