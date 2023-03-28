import turtle
import random
import os
import time

start,end = 0.0, 0.0
clear = lambda: os.system("clear")
#---------------------Mazes----------------------
maze_list = [
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 'E', 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 'E', 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 'E', 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 'E', 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 'E', 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 'E', 0, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 'E', 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 'E', 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    ],
    [    
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 'E', 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    ],
    [   
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 'E', 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    ],
    [    
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 'E', 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    ],
    [    
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 'E', 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    ],
    [    
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 'E', 0, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    ],
    [    
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 'E', 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 'E', 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
        [1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 'E', 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    ],
    [  
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 'E', 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    ],
    [  
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 'E', 0, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    ]
]

# Get rid of duplicate mazes to ensure accurate randomness since,
# the mazes have been copied from online sources
for maze in maze_list:
    maze_list.remove(maze)
    if maze not in maze_list:
        maze_list.append(maze)
#------------------random-init-------------------
maze = maze_list[random.randint(0, len(maze_list)-1)]
maze_size = len(maze)

cell_size = 25
start_row, start_col = 1, 0
#------------------turtle-setup------------------
screen = turtle.Screen()
screen.setup(600, 600)
turtle.hideturtle()
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
#------------------print_rules-------------------
logo_cmds = '''
          MAZE

=> Commands are NOT case sensitive.
FD - move forward 1 step
BD - move backward 1 step
LT - turn left(heading - left)
RT - turn right(heading - right)
'''
print(logo_cmds)
#-----------------print_example------------------
def example():
  t.hideturtle()
  ex = turtle.Turtle()
  ex.hideturtle()
  ex.penup()
  ex.speed(0)
  ex.setheading(90)
  ex.goto(t.position())
  ex.speed(1)
  ex.color("purple")
  ex.write("EXAMPLE", font=("Verdana", 14, 'normal'), align='right')
  time.sleep(1)
  ex.clear()
  ex.showturtle()
  ex.forward(cell_size)
  ex.write("THIS IS WHAT ONE", font=("Verdana", 14, 'normal'), align='right')
  ex.backward(16)
  ex.write("STEP LOOKS LIKE!", font=("Verdana", 14, 'normal'), align='right')
  ex.color("black")
  time.sleep(2.5)
  ex.backward(cell_size-16)
  ex.clear()
  ex.hideturtle()
  t.showturtle()
#------------------maze-display------------------
def draw_maze():
    for row in range(maze_size):
        for col in range(maze_size):
            if maze[row][col] == 1:
                x = col * cell_size
                y = (maze_size - row - 1) * cell_size
                t.penup()
                t.goto(x, y)
                t.pendown()
                t.setheading(0)
                t.color('black')
                t.begin_fill()
                for _ in range(4):
                    t.forward(cell_size)
                    t.left(90)
                t.color('#4F4F4B')  
                t.end_fill()
                t.color("black")
                
            elif maze[row][col] == "E":
                x = col * cell_size
                y = (maze_size - row - 1) * cell_size
                t.penup()
                t.goto(x, y)
                t.pendown()
                t.setheading(0)
                t.begin_fill()
                t.color('black')
                for _ in range(4):
                    t.forward(cell_size)
                    t.left(90)
                t.color("green")
                t.end_fill()
                t.color("black")

            else:
                x = col * cell_size
                y = (maze_size - row - 1) * cell_size
                t.penup()
                t.goto(x, y)
                t.pendown()
                t.setheading(0)
                t.begin_fill()
                t.color("#FFDFD3")
                for _ in range(4):
                    t.forward(cell_size)
                    t.left(90)
                t.end_fill()
                t.color("black")
    t.setheading(180)
    t.penup()
    t.forward(cell_size/2)
    t.setheading(90)
    t.forward(cell_size/2)
#-------------hit-wall/winner-detect-------------
def hit_wall():
    row = int(round((maze_size * cell_size - t.ycor() - cell_size / 2) / cell_size))
    col = int(round((t.xcor() - cell_size / 2) / cell_size))
    if row < 0 or row >= maze_size or col < 0 or col >= maze_size or maze[row][col] == 1:
        return True
    if row < 0 or row >= maze_size or col < 0 or col >= maze_size or maze[row][col] == "E":
        t.color("purple")
        t.write("YOU WIN!", font=("Verdana", 24, "normal"))
        end = time.time()
        elapsed_time = str(end - start) + str('sec')
        time.sleep(1)
        t.undo()
        print("Your Time:" + str(elapsed_time))
        return False
    else:
        return False
#----------------turtle-movement-----------------
def execute_command(dir):
    stride = cell_size
    current_heading = t.heading()
    if dir == "FD":
        t.forward(stride)
        if hit_wall():
            # t.penup()
            t.backward(stride)
            # t.pendown()
    elif dir == "BD":
        t.backward(stride)
        if hit_wall():
            t.penup()
            t.forward(stride)
            t.pendown()
    elif dir == "LT":
        t.setheading(current_heading+90)
    elif dir == "RT":
        t.setheading(current_heading-90)
    elif dir == "EXIT":
        sys.exit()
    else:
        t.setheading(current_heading)
#--------------------console---------------------
def read_script():
    script = []
    start_command = input(">>").upper()
    if start_command == "START":
        start = time.time()
        while True:
            command = input(">>").upper()
            script.append(command)
            if command == "END":
                print("Script Saved.")
                break
    return script
#-------------------gameloop---------------------
while True:
    draw_maze()
    example()
    
    clear()
    print("=>Type 'start' in the console, press enter and write your script!")
    print("=>Type 'end' once you're done and press enter.")
    print("=>You will be timed, so be quick!!")
    
    script = read_script()
    idx = 0
    
    t.pendown()
    while idx <= len(script)-1:
        execute_command(script[idx])
        idx += 1
    
    restart = input("Restart Game?(Y/n): ").upper()
    # number daalke dekh
    if restart == 'n':
        break
    t.clear()
#------------------------------------------------
