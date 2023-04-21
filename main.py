import turtle

def slnko(n, strana, luc):
    t = turtle.Turtle()
    t.speed(1) #Možeme zmeniť rýchlost kresby
    #Výpočet úhlu otáčok kolmých na jednotlivé strany
    u = 90-(360/n)
    #Vykreslý stred
    for i in range(n):
        t.forward(strana)
        t.right(360/n)
    t.hideturtle()
    #Vykreslý lúče
    obdlznik(strana,luc,u,n)

def obdlznik (a,b,c,d):
  
  t = turtle.Turtle()
  t.speed(1) #Možeme zmeniť rýchlost kresby
  
  for i in range(d):
    t.left(90)
    t.forward(b)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.left(c)
    
    
slnko(6,20,50) #Volám funkciu s parametrami: počet strán | dľžka strany | dľžka lúčov
