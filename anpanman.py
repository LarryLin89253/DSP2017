from turtle import *
 
#big face
def bigface():
    up()
    goto(0,-205)
    down()
    width(3)
    color("black","#FFC78E")
    begin_fill()
    circle(220,360)
    end_fill()


#red nose
def rednose():
    up()
    goto(0,-70)
    down()
    width(5)
    color("black","#FF0000")
    begin_fill()
    circle(200/3.,360)
    end_fill()


 #left orange cheek 
def leftCheek():
    up()
    goto(-120,-65)
    down()
    width(5)
    color("black","#FF8000")
    begin_fill()
    circle(200/4.,180)
    end_fill()
    color("#FF8000","#FF8000")
    begin_fill()
    circle(200/4.,180)
    end_fill()


#left orange cheek 
def rightCheek():
    up()
    goto(120,-65)
    down()
    width(5)
    color("#FF8000","#FF8000")
    begin_fill()
    circle(200/4.,180)
    end_fill()
    color("black","#FF8000")
    begin_fill()
    circle(200/4.,180)
    end_fill()
    color("black")


#left eyebrow
def leftEyebrow():
    up()
    goto(-50,130)
    down()
    width(5)
    left(90)
    circle(50,180)


#right eyebrow
def rightEyebrow():
    up()
    goto(150,130)
    down()
    left(180)
    circle(50,180)


 #left eye
def leftEye():
    up()
    goto(-110,110)
    down()
    color("black","black")
    begin_fill()
    width(3)
    right(180)
    backward(25)
    right(180)
    circle(20,180)
    forward(25)
    circle(20,180)
    end_fill()


 #right eye
def rightEye():
    up()
    goto(110,85)
    down()
    color("black","black")
    begin_fill()
    width(3)
    left(180)
    forward(25)
    circle(20,180)
    forward(25)
    circle(20,180)
    end_fill()


 #smile
def smile():
    up()
    goto(-65,-90)
    down()
    width(5)
    color("black","#B87070")
    begin_fill()
    right(180)
    circle(65,180)
    left(90)
    forward(130)
    end_fill()
    
    
#left hand
def leftHand():
    up()
    goto(-165,-163)
    down()
    width(4)
    color("black","#FFD306")
    begin_fill()
    right(20)
    forward(60)
    right(80)
    circle(50,300)
    right(50)
    forward(60)
    up()
    goto(-165,-163)
    down()
    right(96)
    forward(60)
    end_fill()
    
    
#main body
def mainBody():
    up()
    goto(-75,-192)
    down()
    color("black","red")
    begin_fill()
    right(72)
    forward(92)
    left(73)
    forward(60)
    left(97)
    forward(90)
    right(66)
    forward(160)
    up()
    goto(75,-192)
    down()
    left(112)
    forward(90)
    right(73)
    forward(60)
    right(97)
    forward(90)
    left(66)
    forward(160)
    end_fill()
    
    
#right hand
def rightHand():
    up()
    goto(198,-210)
    down()
    width(4)
    color("black","#FFD306")
    begin_fill()
    left(113)
    forward(60)
    right(60)
    circle(50,300)
    right(65)
    forward(65)
    up()
    goto(165,-163)
    down()
    left(101)
    forward(59)
    end_fill()
    
    
#clothes_smile_logo
def clothes_smile_logo():
    up()
    goto(-27,-295)
    down()
    width(3)    
    color("black","#FFD306")
    begin_fill()
    circle(32,360)
    end_fill()
    up()
    goto(-15,-265)
    down()
    right(35)
    forward(10)
    up()
    goto(15,-265)
    down()
    forward(10)
    up()
    goto(-9,-290)
    down()
    left(27)
    circle(10,123)


def main():
    reset()
    bigface()
    rednose()
    leftCheek()
    rightCheek()
    leftEyebrow()
    rightEyebrow()
    leftEye()
    rightEye()
    smile()
    leftHand()
    mainBody()
    rightHand()
    clothes_smile_logo()
    ht()
    return "Done!"

if __name__ == '__main__':
    main()
    mainloop()