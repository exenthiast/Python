import turtle

t = turtle.Turtle()
s = turtle.Screen()
y = -125

def draw_circle_on_top_of_stick(fill_color, border_color, x, y, radius):
    t.penup()
    t.pensize(3)
    t.color(fill_color)
    t.fillcolor(border_color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.getscreen().update()

def draw_candle_for_cake(fill_color, border_color, x, y):
    t.penup()
    t.color(border_color)
    t.fillcolor(fill_color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.forward(25)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.end_fill()
    t.getscreen().update()

def draw_stick_on_candle(fill_color, x, y, cursor_size):
    t.penup()
    t.color(fill_color)
    t.fillcolor(fill_color)
    t.goto(x, y)
    t.pensize(cursor_size)
    t.begin_fill()
    t.pendown()
    t.right(90)
    t.forward(12)
    t.end_fill()
    t.getscreen().update()

def write_happy_inside_circle(text_color, x, y):
    t.penup()
    t.color(text_color)
    t.goto(x, y)
    t.begin_fill()
    t.pendown()
    t.write("Happy", font=("sans-serif", 26, "bold"))
    t.getscreen().update()

def write_birthday_inside_circle(text_color, x, y):
    t.penup()
    t.color(text_color)
    t.goto(x, y)
    t.begin_fill()
    t.pendown()
    t.write("Birthday", font=("sans-serif", 26, "bold"))
    t.getscreen().update()
    
def write_evyy_inside_circle(text_color, x, y):
    t.penup()
    t.color(text_color)
    t.goto(x, y)
    t.begin_fill()
    t.pendown()
    t.write("Evyy", font=("sans-serif", 26, "bold"))
    t.getscreen().update()

def draw_stick(fill_color, border_color, x, y):
    t.penup()
    t.pensize(3)
    t.color(border_color)
    t.fillcolor(fill_color)
    t.goto(x, y)
    t.begin_fill()
    t.pendown()
    t.left(180)
    t.forward(200)
    t.end_fill()

def draw_toppings_on_cake(fill_color, border_color, x, y, radius):
    t.penup()
    t.color(border_color)
    t.fillcolor(fill_color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.forward(10)
    t.left(90)
    t.circle(radius, extent = 180)
    t.left(90)
    t.forward(10)
    t.end_fill()
    t.getscreen().update()

def draw_layer_of_the_cake(fill_color, border_color, cursor_size, x, y, width, height):
    t.hideturtle()
    t.penup()
    t.pensize(cursor_size)
    t.color(border_color)
    t.fillcolor(fill_color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()

    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

    t.end_fill()
    t.setheading(0)
    t.getscreen().update()

s.bgcolor("#FFFDD0")

parts_of_cake = []
parts_of_cake.append(["#A020F0", "#000000", 3, 30])
parts_of_cake.append(["#55FF55", "#000000", 3, 20])
parts_of_cake.append(["#B87333", "#000000", 3, 60])

draw_layer_of_the_cake("#FFC0CB", "#000000", 3, -220, y - 70, 400, 10)

for parts in parts_of_cake:
    draw_layer_of_the_cake(parts[0], parts[1], parts[2], -135, y - 60, 240, parts[3])
    y += parts[3]

draw_toppings_on_cake("#C20067", "#000000", -120, y - 60, 10)
draw_toppings_on_cake("#FFFF00", "#000000", -80, y - 60, 10)
draw_toppings_on_cake("#FF0000", "#000000", 25, y - 60, 10)
draw_toppings_on_cake("#0000FF", "#000000", 59, y - 60, 10)
draw_toppings_on_cake("#FFA500", "#000000", -135, y - 80, 10)
draw_toppings_on_cake("#E4E6EB", "#000000", -135, y - 100, 10)
draw_toppings_on_cake("#FFA500", "#000000", -135, y - 120, 10)
draw_toppings_on_cake("#181A18", "#000000", -80, y - 80, 10)
draw_toppings_on_cake("#0000FF", "#000000", -65, y - 110, 10)
draw_toppings_on_cake("#FFD700", "#000000", -95, y - 140, 10)
draw_toppings_on_cake("#181A18", "#000000", 10, y - 80, 10)
draw_toppings_on_cake("#E4E6EB", "#000000", -20, y - 110, 10)
draw_toppings_on_cake("#181418", "#000000", 35, y - 140, 10)
draw_toppings_on_cake("#FFA500", "#000000", 75, y - 80, 10)
draw_toppings_on_cake("#E4E6EB", "#000000", 75, y - 110, 10)
draw_toppings_on_cake("#FFD700", "#000000", 75, y - 140, 10)
draw_candle_for_cake("#FFF44F", "#000000", -40, y - 60)
draw_stick_on_candle("#181A18", -26, y + 15, 7)
draw_stick("#181A18", "#181A18", 0, y - 60)
draw_circle_on_top_of_stick("#181A18", "#FFFDD0", 100, y + 235, 100)
write_happy_inside_circle("#000000", -50, y + 230)
write_birthday_inside_circle("#000000", -70, y + 190)
write_evyy_inside_circle("#000000", -50, y + 150)

turtle.done()