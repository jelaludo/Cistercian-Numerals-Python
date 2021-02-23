

Cistercian = int(input("Please Input number from 1 to 9999: "))
print(Cistercian)
List_digits = [0,0,0] + [int(x) for x in str(Cistercian)]
# Concatenating [0,0,0] for "padding"

units = List_digits[-1]
tens = List_digits[-2]
hundreds = List_digits[-3]
thousands = List_digits[-4]

print(thousands, " = Thousands")
print(hundreds, " = Hundreds")
print(tens, " = Tens")
print(units, " = Units")

import turtle
point1 = (-50, 150)
point2 = (0, 150)
point3 = (50,150)
point4 = (-50,100)
point5 = (0,100)
point6 = (50,100)
point7 = (-50,50)
point8 = (0,50)
point9 = (50,50)
point10 = (-50,0)
point11 = (0,0)
point12 = (50,0)
point50 = (0,-100)

## Structure of the matrix to represent Cistercian numbers, e.g. 11 to  2 is a straigth line.
## 1  2  3
## 4  5  6
## 7  8  9
##10 11  12

turtle.penup()
turtle.goto(point11)
turtle.pendown()
turtle.goto(point2)
turtle.penup()

## apparently sets the speed of the drawing
turtle.delay(5)

## Draw corresponding Cistercian coordinates for thousands
if thousands == 1:
    turtle.penup()
    turtle.goto(point11)
    turtle.pendown()
    turtle.goto(point10)
elif thousands == 2:
    turtle.penup()
    turtle.goto(point8)
    turtle.pendown()
    turtle.goto(point7)
elif thousands == 3:
    turtle.penup()
    turtle.goto(point11)
    turtle.pendown()
    turtle.goto(point7)
elif thousands == 4:
    turtle.penup()
    turtle.goto(point8)
    turtle.pendown()
    turtle.goto(point10)
elif thousands == 5:
    turtle.penup()
    turtle.goto(point8)
    turtle.pendown()
    turtle.goto(point10)
    turtle.pendown()
    turtle.goto(point11)
elif thousands == 6:
    turtle.penup()
    turtle.goto(point10)
    turtle.pendown()
    turtle.goto(point7)
elif thousands == 7:
    turtle.penup()
    turtle.goto(point11)
    turtle.pendown()
    turtle.goto(point10)
    turtle.pendown()
    turtle.goto(point7)
elif thousands == 8:
    turtle.penup()
    turtle.goto(point8)
    turtle.pendown()
    turtle.goto(point7)
    turtle.pendown()
    turtle.goto(point10)
elif thousands == 9:
    turtle.penup()
    turtle.goto(point8)
    turtle.pendown()
    turtle.goto(point7)
    turtle.pendown()
    turtle.goto(point10)
    turtle.pendown()
    turtle.goto(point11)
else:
    turtle.penup()

## Draw corresponding Cistercian coordinates for hundreds
if hundreds == 1:
    turtle.penup()
    turtle.goto(point11)
    turtle.pendown()
    turtle.goto(point12)
elif hundreds == 2:
    turtle.penup()
    turtle.goto(point8)
    turtle.pendown()
    turtle.goto(point9)
elif hundreds == 3:
    turtle.penup()
    turtle.goto(point11)
    turtle.pendown()
    turtle.goto(point9)
elif hundreds == 4:
    turtle.penup()
    turtle.goto(point8)
    turtle.pendown()
    turtle.goto(point12)
elif hundreds == 5:
    turtle.penup()
    turtle.goto(point8)
    turtle.pendown()
    turtle.goto(point12)
    turtle.pendown()
    turtle.goto(point11)
elif hundreds == 6:
    turtle.penup()
    turtle.goto(point9)
    turtle.pendown()
    turtle.goto(point12)
elif hundreds == 7:
    turtle.penup()
    turtle.goto(point11)
    turtle.pendown()
    turtle.goto(point12)
    turtle.pendown()
    turtle.goto(point9)
elif hundreds == 8:
    turtle.penup()
    turtle.goto(point8)
    turtle.pendown()
    turtle.goto(point9)
    turtle.pendown()
    turtle.goto(point12)
elif hundreds == 9:
    turtle.penup()
    turtle.goto(point8)
    turtle.pendown()
    turtle.goto(point9)
    turtle.pendown()
    turtle.goto(point12)
    turtle.pendown()
    turtle.goto(point11)
else:
    turtle.penup()

## Draw corresponding Cistercian coordinates for tens

if tens == 1:
    turtle.penup()
    turtle.goto(point2)
    turtle.pendown()
    turtle.goto(point1)
elif tens == 2:
    turtle.penup()
    turtle.goto(point5)
    turtle.pendown()
    turtle.goto(point4)
elif tens == 3:
    turtle.penup()
    turtle.goto(point2)
    turtle.pendown()
    turtle.goto(point4)
elif tens == 4:
    turtle.penup()
    turtle.goto(point5)
    turtle.pendown()
    turtle.goto(point1)
elif tens == 5:
    turtle.penup()
    turtle.goto(point5)
    turtle.pendown()
    turtle.goto(point1)
    turtle.pendown()
    turtle.goto(point2)
elif tens == 6:
    turtle.penup()
    turtle.goto(point1)
    turtle.pendown()
    turtle.goto(point4)
elif tens == 7:
    turtle.penup()
    turtle.goto(point2)
    turtle.pendown()
    turtle.goto(point1)
    turtle.pendown()
    turtle.goto(point4)
elif tens == 8:
    turtle.penup()
    turtle.goto(point5)
    turtle.pendown()
    turtle.goto(point4)
    turtle.pendown()
    turtle.goto(point1)
elif tens == 9:
    turtle.penup()
    turtle.goto(point5)
    turtle.pendown()
    turtle.goto(point4)
    turtle.pendown()
    turtle.goto(point1)
    turtle.pendown()
    turtle.goto(point2)
else:
    turtle.penup()

## Draw corresponding Cistercian coordinates for units
if units == 1:
    turtle.penup()
    turtle.goto(point11)
    turtle.pendown()
    turtle.goto(point2)
    turtle.penup()
    turtle.goto(point2)
    turtle.pendown()
    turtle.goto(point3)
elif units == 2:
    turtle.penup()
    turtle.goto(point11)
    turtle.pendown()
    turtle.goto(point2)
    turtle.penup()
    turtle.goto(point5)
    turtle.pendown()
    turtle.goto(point6)
elif units == 3:
    turtle.penup()
    turtle.goto(point11)
    turtle.pendown()
    turtle.goto(point2)
    turtle.penup()
    turtle.goto(point2)
    turtle.pendown()
    turtle.goto(point6)
elif units == 4:
    turtle.penup()
    turtle.goto(point11)
    turtle.pendown()
    turtle.goto(point2)
    turtle.penup()
    turtle.goto(point5)
    turtle.pendown()
    turtle.goto(point3),
elif units == 5:
    turtle.penup()
    turtle.goto(point11)
    turtle.pendown()
    turtle.goto(point2)
    turtle.penup()
    turtle.goto(point5)
    turtle.pendown()
    turtle.goto(point3)
    turtle.pendown()
    turtle.goto(point2),
elif units == 6:
    turtle.penup()
    turtle.goto(point11)
    turtle.pendown()
    turtle.goto(point2)
    turtle.penup()
    turtle.goto(point3)
    turtle.pendown()
    turtle.goto(point6),
elif units == 7:
    turtle.penup()
    turtle.goto(point11)
    turtle.pendown()
    turtle.goto(point2)
    turtle.pendown()
    turtle.goto(point3)
    turtle.pendown()
    turtle.goto(point6),
elif units == 8:
    turtle.penup()
    turtle.goto(point11)
    turtle.pendown()
    turtle.goto(point2)
    turtle.pendown()
    turtle.goto(point5)
    turtle.pendown()
    turtle.goto(point6)
    turtle.pendown()
    turtle.goto(point3),
elif units == 9:
    turtle.penup()
    turtle.goto(point11)
    turtle.pendown()
    turtle.goto(point2)
    turtle.pendown()
    turtle.goto(point3)
    turtle.pendown()
    turtle.goto(point6)
    turtle.pendown()
    turtle.goto(point5)
else:
    turtle.penup()



turtle.penup()
turtle.goto(point50)


turtle.getscreen().getcanvas().postscript(file='CistercianNumber.ps')



turtle.hideturtle()
turtle.exitonclick()


###Graveyeard of dead code
#if Cistercian>10:
#    tens = List_digits[-2]
#else:
#    tens  = 0
#if Cistercian>100:
#    hundreds = List_digits[-3]
#else:
#    hundreds = 0
#if Cistercian>1000:
#    thousands = List_digits[-4]
#else:
#    thousands = 0

#print(List_digits)
#count=(len(List_digits))
#list_length_int=int(count)
#print(count)
#print(list_length_int)