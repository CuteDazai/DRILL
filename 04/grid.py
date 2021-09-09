import turtle

count = 0;
while count!=6:
  turtle.penup()
  turtle.goto(-200,200-count*100)
  turtle.pendown()
  turtle.forward(500)
  count+=1

turtle.right(90)

count = 0;
while count!=6:
  turtle.penup()
  turtle.goto(-200+count*100,200)
  turtle.pendown()
  turtle.forward(500)
  count+=1
