import pgzrun
HEIGHT = 600
WIDTH = 800
title = "quiz master"
marquee_box = Rect(0,0,880,80)
question_box = Rect(0,0,650,150)
timer_box = Rect(0,0,150,150)
skip_box = Rect(0,0,150,330)
answer_box1 = Rect(0,0,301,150)
answer_box2 = Rect(0,0,300,151)
answer_box3 = Rect(0,0,299,150)
answer_box4 = Rect(0,0,300,149)
score = 0
time_left = 10
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
    screen.draw.filled_rect(marquee_box"black")
    screen.draw.filled_rect(question_box"blue")
    screen.draw.filled_rect(timer_box"blue")
    screen.draw.filled_rect(skip_box"green")
    for i in answer_boxes:
        screen.draw.filled_rect(i,"orange")
    marquee_message = "Welcome to QWIZ MASTER"
    marquee_message = marquee_message + f"q:{question_index}off{question_count}"
    screen.draw.textbox(marquee_message, marquee_box, color = "white")
    screen.draw.textbox(str(time_left), timer_box, color = "white")
    screen.draw.textbox("skip", skip_box, color = "black" angle = -90)
    screen.draw.textbow(questions[0].strip(),question_box, color = "white")
    index = 1
    for i in answer_boxes:
        screen.draw.textbox(questions[index].strip(),i, color = "black")
        index = index + 1