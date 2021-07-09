#author Matthias Lellouche

#this function is to define the size of the star and to check if the value entered by the user is correct
# if the value is incorrect (different than a positive integer), a error message is displayed
def starSize():
    try:
        print("size of the star (only positive integer)")
        size = int(input())
    except ValueError:
        print("the value input is not an positive integer")
    if(size <= 0):
        print("NULL")
    return size

#this function is to draw the top of the star
def drawTopStar():
    #diagonal bars
    for row in range(size):
        for col in range(size, size*6):
            #diagonal bar from the bottom to the top and from the top to the bottom
            if (col == size*4 - row or col == size*4 + row):
                print("*", end = "")
            else:
                print(" ", end = "")
        print()
    #horizontal bar
    for line in range(size*6 + 1):
        if(line < size*2 or line > size * 4):
            print("*", end = "")
        else:
            print(" ", end = "")
    print("")

#this function is to draw the middle of the star
def drawMiddleStar():
    #top middle diagonal bars
    for rowUp in range(size):
        for col in range(size * 6):
            if (col == rowUp or col == size * 6 - 1 - rowUp):
                print("*", end = "")
            else:
                print(" ", end = "")
        print()
    #bottom middle diagonal bars
    for rowLow in range(size -1):
        for col in range(size * 6):
            if (col == (size - 1) - rowLow or col == size*5 + 1 + rowLow):
                print("*", end = "")
            else:
                print(" ", end = "")
        print()

#this function is to draw the bottom of the star
def drawBottomStar():
    #horizontal bar
    for line in range(size*6 + 1):
        if(line < size*2 or line > size * 4):
            print("*", end = "")
        else:
            print(" ", end = "")
    print("")
    #diagonal bars
    for row in range(size):
        for col in range(size, size*6):
            #diagonal bar from the top to the bottom and from the bottom to the top
            if (col == size*3 + 1 + row or col == size * 5 - 1 - row):
                print("*", end = "")
            else:
                print(" ", end = "")
        print()



#this is the main part of this code
size = starSize()
#check if the value is correct
if (size > 0):
    #if it's correct we call functions
    drawTopStar()
    drawMiddleStar()
    drawBottomStar()
