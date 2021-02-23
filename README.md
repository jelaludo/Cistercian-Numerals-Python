# Cistercian-Numerals-Python
Drawing  the 14th century Cistercian representation of numbers from 1 to 9999 using Python 

https://en.wikipedia.org/wiki/The_Ciphers_of_the_Monks
inspiration from this article

There's actually a late 2020 proposal to add the Cistercian  numerals to unicode
http://www.unicode.org/L2/L2020/20290-cistercian-digits.pdf

This is my first program, I used this to learn and play around with Python.

It relies on Turtle Graphics  (import turtle)
https://docs.python.org/3/library/turtle.html

The basic symbols have a 2x3 ratio, I mapped 6 squares with 12 points, assigned each a plot value;
1   2  3
4   5  6
7   8  9
10 11 12

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

Then simply  drew lines : 2 to 11 for a straight vertical line in the center, 5 to 1 for a small angled one to represent "40", etc.

user inputs a  number
number is mapped to a list
extract value for thousands, hundreds, tens, units.
then map them by drawing with turtle 
turtle.penup()
turtle.goto(point11)
turtle.pendown()
turtle.goto(point2)

fun little project. 
