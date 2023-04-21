import turtle

def slnko(n, strana, luc):
    t = turtle.Turtle()
    t.speed(0)
    #Výpočet úhlu otáčok kolmých na jednotlivé strany
    u = 90-(360/n)
    #Vykreslý stred
    for i in range(n):
        t.forward(strana)
        t.right(360/n)
    t.hideturtle()
    #Vykreslý lúče
    obdlznik(strana,luc,u)

def obdlznik (a,b,c):
  
  t = turtle.Turtle()
  t.speed(1)

  t.sety(t.ycor()+b)
  t.forward(a)
  t.sety(t.ycor()-b)
  t.left(c)
  t.forward(b)
  t.right(90)
  t.forward(a)
  t.right(90)
  t.forward(b)
  t.left(c)
  t.forward(a)

slnko(10,20,50)
