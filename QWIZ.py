import pgzrun
HEIGHT = 700
WIDTH = 900
title = "qwiz master"
marquee_box = Rect(0,0,880,80)
question_box = Rect(0,0,650,150)
timer_box = Rect(0,0,150,150)
skip_box = Rect(0,0,150,330)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
score = 0
time_left = 100
question_filename = "questions.txt"
marquee_message = ""
is_gameover = False
answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]
questions = []
question_count = 0
question_index = 0
marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
skip_box.move_ip(700,270)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)

def draw():
    global marquee_message
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(marquee_box,"black")
    screen.draw.filled_rect(question_box,"blue")
    screen.draw.filled_rect(timer_box,"blue")
    screen.draw.filled_rect(skip_box,"green")
    for i in answer_boxes:
        screen.draw.filled_rect(i,"orange")
    marquee_message = "Welcome to QWIZ MASTER"
    marquee_message = marquee_message + f"q:{question_index}off{question_count}"
    screen.draw.textbox(marquee_message, marquee_box, color = "white")
    screen.draw.textbox(str(time_left), timer_box, color = "white")
    screen.draw.textbox("skip", skip_box, color = "black", angle = -90)
    screen.draw.textbox(question[0].strip(),question_box, color = "white")
    index = 1
    for i in answer_boxes:
        screen.draw.textbox(question[index].strip(),i, color = "black")
        index += 1
def move_marquee():
    marquee_box.x = marquee_box.x - 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH

def read_question_file():
    global question_count, questions #global hamster, microwaves, dinosaurs_from_mars
    q_file = open(question_filename, "r")
    for question in q_file:
        questions.append(question)
        question_count += 1
    q_file.close()

def read_next_question():
    global question_index
    question_index += 1
    return questions.pop(0).split(",")

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos): # Checks if cursor is on the question boxes / which on it's on
            if index is int(question[5]): # Check if answer is correct or not
                correct_answer()
            else:
                gameover()
        index += 1
    if skip_box.collidepoint(pos):
        skip_question()

def correct_answer():
    global score, question, time_left, questions
    score += 1
    if questions:
        question = read_next_question()
        time_left = 100
    else:
        gameover()

def gameover():
    global question, time_left, is_gameover
    message = f"Gameover you got {score} questions correct."
    question = [message, "THE END", "THE END", "THE END", "THE END", 5]
    time_left = 0
    is_gameover = True

def skip_question():
    global time_left, question
    if questions and not is_gameover:
        question = read_next_question()
        time_left = 100
    else:
        gameover()

def update_time_left():
    global time_left
    if time_left:
        time_left -= 1
    else:
        gameover()

def update():
    move_marquee()

read_question_file()
question  = read_next_question()
clock.schedule_interval(update_time_left,0.05)
pgzrun.go()
