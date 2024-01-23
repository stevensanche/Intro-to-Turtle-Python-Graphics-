'''
CIS 122 Spring 2022 Project 3-2
Author(s): Steven Sanchez-Jimenez
Credit: CIS 122 Resources only
Description: Intro to Python Turtle Graphics
'''
from turtle import*
def poly():
    '''
    this function is what is giving the house all of its sides,colors, etc
    '''

    color('green')
    begin_fill()
    fd(50)
    lt(90)
    print('this is the main frame of the house')
    for i in range(3):
        x = fd(200), lt(90)
        print(x)
    fd(150)
    end_fill()
    #below is the code for the door that is on the house
    color('yellow')
    begin_fill()
    #below will be a loop so the same code isn't typed multiple times
    print('this is the door to the house')
    for k in range(4):
         y = lt(90), fd(50)
         print(y)
    end_fill()
    pu()
    setpos(-250,100)
    pd()
    #the next lines will be the start of the triangle above the house (square)
    color('yellow')
    begin_fill()
    fd(200)
    lt(90)
    lt(30)
    #another loop will be performed below so the code doesn't look super clumped
    print('this is the roof of the house')
    for t in range(2):
        z = fd(200), lt(120)
        print(z)
    end_fill()

def house():
    '''
    this will be the main function that is going to be called
    '''
    shape('turtle')
    pensize=2
    pu()
    setpos(-100,-100)
    pd()
    print(poly())

def main():
    '''
    this will be the attributes of the turtle
    '''
    speed(2)
    print(house())


print(main())


