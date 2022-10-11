'''Problem: How to write a program that prints a shape with a number of characters closest to but not greater than the entered number'''
'''Variables used:
charnum = number of characters entered 
shapenum = number of characters in the shape
rem = extra characters (charnum - shapenum)
n = variable in formula, range definer, number of lines in shape-square,triangle and half the number of lines in diamond
ch = character
t = temporary value (for better readability)
nw = number of whitespaces
nc = number of characters'''

def triangle(charnum,ch):    # function for triangle shape
#   shapenum = n*(n+1)/2 (1+2+3+..+n)
    shapenum = 0
    for i in range(1,charnum):   #loop to find out number of characters used and n where n is the number of lines in triangle
        if shapenum+i <= charnum:    #finds maximum value of shapenum until shapenum+i>charnum
            shapenum += i            #maximum value of shapenum gets assigned
            n = i                    #maximum value of i gets assigned to n
            
    rem = charnum - shapenum    #finds the number of unused characters in the shape
    print(f"\n!!! THE TRIANGLE OF {ch} !!!")
    for i in range(1,n+1):      #loop for printing triangle shape
        print()                 #prints an empty line
        for j in range(i):     
            print(ch, end="")   #end="" causes printing characters in the same line 
    print()
    
    if rem>0:
        print("\nExtra character(s): ", ch*rem)  #prints the unused characters
            
def square(charnum,ch):    # function for square shape
#   shapenum = (n**2)
    shapenum = 0
    for i in range(1,charnum): #loop to find out number of characters used and n where n is the number of lines in square
        t = (i**2)  #as for the shape square, number of characters used will always be the sqaure of a number so t=1,4,9,16...
        if t <= charnum:   #finds maximum value of t until t>charnum
            shapenum = t   #maximum value of t gets assigned
            n = i          #maximum value of i gets assigned n

    rem = charnum - shapenum      #finds the number of unused characters in the shape
    print("\n!!! THE SQUARE OF ",ch," !!!")
    for i in range(n):            #loop for printing square shape
        print()                   #prints an empty line
        for j in range(n):
            print(ch," " , end="")  #end="" causes printing characters in the same line
    print()

    if rem>0:
        print("\nExtra character(s): ", ch*rem)  #prints the unused characters
            
def diamond(charnum,ch):   #function for diamond shape
#   shapenum = (1+3+5+...(2*n-1))
    shapenum = 0
    for i in range(1,charnum):  #loop to find out number of characters used and n where n is the number of lines in diamond
        if shapenum <= charnum: #finds maximum value of shapenum
            t = (2*i)-1    #temp value which is equal to the number of charc in "i"th line i.e first line 1 char, second line 3 char..
            if shapenum + 3*t + 2  <= charnum: #t*2 because the number is added from both ends of the pattern, t+2 to get the next number in the series
                shapenum += 2*t   #2*t added as the next number in series satisfies condition
            else:
                shapenum += t     #if the next number in the series doesnt statisfy, only t gets added
                n = i             #maximum value of i gets assigned n
                break

    rem = charnum - shapenum     #finds the number of unused characters in the shape
    print("\n!!! THE DIAMOND OF ",ch," !!!")
    for i in range(1,2*n):    #loop for printing diamond shape, (1,n) would only print half of the shape 
        print()
        if i < (n+1):      #n+1 to print the middle row
            nc = (2*i)-1   #finds number of character 
            nw = n-i       #finds number of character 
            print(' '*nw, ch*nc)     #prints accordingly
        else:
            nc = 2*((2*n)-i)-1  #finds number of character 
            nw = i-n            #finds number of character 
            print(' '*nw, ch*nc)     #prints accordingly

    if rem>0:
        print("\nExtra character(s): ", ch*rem)
    
def prompt():    #function for welcome message
    ques = "Hello there! Would you like to print a shape? (y/n): "
    choice = input(ques)
    choice=choice.lower()     #changs the input to lowercase if user inputs character in uppercase
    while choice not in ['y','n']:  #checks whether user input is either y or n
        print("Invalid input!")     #prints accordingly
        choice = input(ques)
    if choice == 'y':         #checks whether both choice and 'y' are same
        return True
    else:
        return False
    
def __main__():  
    choice = prompt()   #calls the prompt() function
    while choice == True: 
        print("""Which of these shapes would you like to print?
    1. Triangle
    2. Square
    3. Diamond""")
        
        shape = input("Enter 1, 2 or 3: ")
        while shape not in ['1','2','3']:  #checks whether user input is either 1,2 or 3
            print("Invalid input!")        #prints accordingly
            shape = input("Enter 1, 2 or 3: ")
            
        ch = input("Enter any character: ")  #user input where ch is the character used in the shape
        while len(ch) != 1:        #checks whether user input is more than 1
            print("Please enter exactly one character!")
            ch = input("Enter any character: ")
            
        charnum = int(input("Enter number of characters for your shape (min: 20): "))   #user input where charnum is possibly the number of times ch will be repeated 
        while charnum < 20:
            print("The number entered is too small!")
            charnum = int(input("Enter number of characters for your shape (min: 20): "))
            
        if shape == "1":
            triangle(charnum,ch)  #calls the triangle() function
        elif shape == "2":
            square(charnum,ch)    #calls the square() function
        else:
            diamond(charnum,ch)   #calls the diamond() function
            
        choice = prompt()         #calls the prompt() function again if user wishes to print another shape 
    
__main__()  #calls the __main__() function