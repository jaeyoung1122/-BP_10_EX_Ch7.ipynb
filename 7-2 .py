import turtle 
t = turtle.Turtle()
t.shape("turtle")
t.speed(10)

def hexagon():
  for i in range(6):
      t.forward(100)
      t.left(360/6)

for i in range (6):
    hexagon()
    t.forward(100)
    t.right(60)
