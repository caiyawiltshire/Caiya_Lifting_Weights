size (1000,800)
background (255, 227, 245)

#Hair
fill (0,0,0)
arc (500,300,170,170,PI,PI*2)
rect (415,290,170,85)

#theFace
fill (161, 112, 40)
stroke (161, 112, 40)
ellipse (500,300,150,150) #Head
fill (0,0,0)
ellipse (470,270,15,15) #Eyes
ellipse (530,270,15,15)
stroke (0,0,0)
line (500,290,510,305)
line (510,305,500,305) #Nose
fill (255,255,255)
arc (500,320,75,75, 0, PI, CHORD) #smile

#theNeck
stroke (161, 112, 40)
fill (161, 112, 40)
rect (475,372,50,18)

#Arms
rect (300,390,400,30) #LowerArms
rect (300,200,30,190)
rect (670,200,30,190)

#shirtStraps
fill (93, 240, 111)
stroke (93, 240, 111)
rect (440,390,10,30)
rect (550,390,10,30)

#Shirt
rect (440,420,120,130)

#pants
fill (0,0,0)
stroke (0,0,0)
rect (445,550,45,150)
rect (515,550,45,150)

#Shoes
fill (255,255,255)
stroke (255,255,255)
ellipse (465,720,60,40)
ellipse (545,720,60,40)

#barWeight
fill (0,0,0)
stroke (0,0,0)
rect (250,175,500,20)

#Weights
ellipse (250,185,50,150)
ellipse (745,185,50,150)

#Hands
fill (161, 112, 40)
stroke (161, 112, 40)
ellipse (315,185,35,35)
ellipse (685,185,35,35)

fill (0,0,0)
textSize (30)
text ("Caiya",600,700)
