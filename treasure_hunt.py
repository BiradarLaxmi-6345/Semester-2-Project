# --------------------------------------------------
# GITAM TREASURE HUNT 
# --------------------------------------------------

import turtle
import textwrap
import time

# ---------------- PLAYER ----------------

player_name = input("Enter your name: ")
start_time_game = time.time()

# ---------------- FILE HANDLING ----------------

def load_leaderboard():
    data = []
    try:
        with open("leaderboard.txt", "r") as file:
            for line in file:
                name, t = line.strip().split(",")
                data.append((name, float(t)))
    except FileNotFoundError:
        pass
    return data

def save_leaderboard(data):
    with open("leaderboard.txt", "w") as file:
        for name, t in data:
            file.write(f"{name},{t}\n")

# ---------------- SCREEN ----------------

screen = turtle.Screen()
screen.title("GITAM Treasure Hunt")
screen.bgcolor("lightyellow")
screen.setup(900,600)
screen.tracer(0)

# ---------------- GLOBALS ----------------

time_left = 30
user_input = ""
answer_submitted = False

# ---------------- PENS ----------------

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

timer_pen = turtle.Turtle()
timer_pen.hideturtle()
timer_pen.penup()

input_pen = turtle.Turtle()
input_pen.hideturtle()
input_pen.penup()

# ---------------- MAP DOT ----------------

dot = turtle.Turtle()
dot.shape("circle")
dot.color("red")
dot.penup()
dot.goto(-380,-180)

# ---------------- MAP ----------------

map_pen = turtle.Turtle()
map_pen.hideturtle()
map_pen.penup()

locations = [
("library",(-300,-50)),
("cc",(-180,-100)),
("pet care",(-50,-30)),
("bheemas",(80,-90)),
("shivaji statue",(200,-60)),
("vending machine",(330,-90)),
("bank",(200,-180)),
("d206",(40,-210)),
("veeksha hall",(340,-220))
]

map_pen.goto(-380,-180)
map_pen.dot(20,"green")
map_pen.write("Gate",align="center",font=("Arial",9,"normal"))

# ---------------- DRAW BOX ----------------

def draw_clue_box(text):
    pen.clear()

    pen.goto(-400,260)
    pen.pendown()
    pen.color("black","lightblue")
    pen.begin_fill()

    for _ in range(2):
        pen.forward(800)
        pen.right(90)
        pen.forward(140)
        pen.right(90)

    pen.end_fill()
    pen.penup()

    wrapped = textwrap.fill(text,width=65)

    pen.goto(0,210)
    pen.write(wrapped,align="center",
              font=("Arial",15,"bold"))

# ---------------- TIMER ----------------

def update_timer(t):
    timer_pen.clear()
    timer_pen.goto(380,260)
    timer_pen.color("red")
    timer_pen.write(f"Time: {t}s",
                    align="right",
                    font=("Arial",14,"bold"))

def run_timer():
    global time_left, answer_submitted

    while time_left > 0 and not answer_submitted:
        update_timer(time_left)
        screen.update()
        time.sleep(1)
        time_left -= 1

# ---------------- INPUT ----------------

def update_input():
    input_pen.clear()
    input_pen.goto(0,-250)
    input_pen.write("Your Answer: "+user_input,
                    align="center",
                    font=("Arial",14,"bold"))

def add_char(char):
    global user_input
    user_input += char
    update_input()

def backspace():
    global user_input
    user_input = user_input[:-1]
    update_input()

def submit():
    global answer_submitted
    answer_submitted = True

for c in "abcdefghijklmnopqrstuvwxyz0123456789 ":
    screen.onkey(lambda ch=c: add_char(ch), c)

screen.onkey(backspace,"BackSpace")
screen.onkey(submit,"Return")
screen.listen()

# ---------------- MAP FUNCTIONS ----------------

def reveal_location(name,coord):
    map_pen.goto(coord)
    map_pen.dot(20,"blue")

    map_pen.goto(coord[0],coord[1]+15)
    map_pen.write(name,align="center",
                  font=("Arial",9,"normal"))

def move_dot(coord):
    dot.setheading(dot.towards(coord))

    while dot.distance(coord) > 5:
        dot.forward(3)
        screen.update()

# ---------------- TREASURE ----------------

def blink_treasure():
    pen.clear()
    map_pen.clear()
    dot.hideturtle()

    treasure = turtle.Turtle()
    treasure.hideturtle()
    treasure.penup()

    for _ in range(6):
        treasure.goto(0,0)
        treasure.color("gold")
        treasure.write("🏆 TREASURE FOUND AT VEEKSHA HALL! 🏆",
        align="center",
        font=("Arial",28,"bold"))

        screen.update()
        time.sleep(0.5)

        treasure.clear()
        screen.update()
        time.sleep(0.5)

    treasure.goto(0,0)
    treasure.color("gold")
    treasure.write("🏆 TREASURE FOUND AT VEEKSHA HALL! 🏆",
    align="center",
    font=("Arial",28,"bold"))

# ---------------- LEADERBOARD ----------------

def show_leaderboard(total_time):

    data = load_leaderboard()

    data.append((player_name, total_time))

    data.sort(key=lambda x: x[1])

    save_leaderboard(data)

    pen.clear()

    pen.goto(0,200)
    pen.write("🏆 LEADERBOARD 🏆",
              align="center",
              font=("Arial",24,"bold"))

    y = 120

    for i, (name, t) in enumerate(data[:5]):
        pen.goto(0,y)
        pen.write(f"{i+1}. {name} - {round(t,2)} sec",
                  align="center",
                  font=("Arial",16,"normal"))
        y -= 40

# ---------------- RIDDLE FUNCTION ----------------

def ask_riddle(question,answer,h1,h2,index):

    global user_input, answer_submitted, time_left

    attempts = 0

    while attempts < 3:

        user_input = ""
        answer_submitted = False
        time_left = 30

        clue = question if attempts == 0 else (h1 if attempts==1 else h2)

        draw_clue_box(clue)
        update_input()

        run_timer()

        if answer_submitted and user_input.strip().lower() == answer:
            reveal_location(*locations[index])
            move_dot(locations[index][1])
            return True

        else:
            attempts += 1

    # SHOW CORRECT ANSWER
    input_pen.clear()
    input_pen.goto(0,-250)
    input_pen.write(f"❌ Correct Answer: {answer}",
                    align="center",
                    font=("Arial",16,"bold"))

    screen.update()
    time.sleep(2)

    return False

# ---------------- RIDDLES ----------------

riddles = [
("This place is usually the quietest area on campus. People come here when they need information.",
"library","Students study here","It is full of books"),

("After silence students go somewhere louder with coffee and snacks.",
"cc","Campus cafe","Students eat snacks here"),

("A place meant not for students but for animals.",
"pet care","It helps animals","Campus dogs and cats"),

("Not a library but sells books. Not a cafe but has snacks.",
"bheemas","Stationery shop","Snacks and notebooks"),

("Someone standing on campus for years.",
"shivaji statue","Famous warrior","It is a statue"),

("Machine giving drinks without cashier.",
"vending machine","Automatic drinks","Press a button"),

("Place trusted with money.",
"bank","Keep money here","Withdraw cash"),

("4th letter of alphabet + smallest even number + zero + number after five.",
"d206","Letter D","Numbers 2 0 6"),

("Place where movies are shown on big screen.",
"veeksha hall","Movies shown here","Auditorium")
]

# ---------------- GAME LOOP ----------------

for i in range(len(riddles)):
    ask_riddle(
        riddles[i][0],
        riddles[i][1],
        riddles[i][2],
        riddles[i][3],
        i
    )

# ---------------- END ----------------

blink_treasure()

total_time = time.time() - start_time_game

pen.goto(0,-100)
pen.write(f"Time Taken: {round(total_time,2)} seconds",
          align="center",
          font=("Arial",18,"bold"))

time.sleep(2)

show_leaderboard(total_time)

screen.update()
turtle.done()