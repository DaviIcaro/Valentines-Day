import turtle
import time

# Configuração da janela
window = turtle.Screen()
window.bgcolor("black")

# Configuração da tartaruga
t = turtle.Turtle()
t.speed(0)
t.pensize(5)

# Função para desenhar um coração
def draw_heart():
    t.color("red")
    t.begin_fill()
    t.left(50)
    t.forward(133)
    t.circle(50, 200)
    t.right(140)
    t.circle(50, 200)
    t.forward(133)
    t.end_fill()

# Função para escrever o texto central
def write_text(text, x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.write(text, font=("Times New Roman", size, "bold"))

# Desenhar o coração
draw_heart()
time.sleep(1)

# Desenhar a flecha
t.penup()
t.goto(-90, 30)
t.pendown()
t.left(90)
t.pencolor("white")
t.forward(270)
t.right(150)
t.forward(30)
t.backward(30)
t.right(60)
t.forward(30)
time.sleep(1)

# Desenhar a ponta da flecha
t.penup()
t.goto(-90, 30)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.forward(30)
t.right(150)
t.forward(50)
t.right(30)
t.forward(30)
t.right(120)
t.forward(30)
t.right(30)
t.forward(50)
t.right(150)
t.forward(30)
t.end_fill()
time.sleep(1)

# Escrever o texto
write_text("Happy Valentine's", -220, -100, 45, "white")
write_text("Day!", 60, -210, 55, "white")
time.sleep(0.5)

# Adicionar estrelas
def draw_star(size, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

draw_star(20, -150, 50)
draw_star(30, 100, 100)
draw_star(40, -70, -150)
time.sleep(1)

# Permitir que o usuário insira uma mensagem
# na Mensagem voce pode digitar o nome da sua Namorada, exemplo "Sofia"
message = turtle.textinput("Happy Valentine's Day!", "Digite sua mensagem:")
write_text(message, -250, 0, 30, "white")

# Esconder a tartaruga e finalizar o desenho
t.hideturtle()
turtle.done()
