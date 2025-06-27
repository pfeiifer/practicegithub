"""
A program to produce this output:
r= no of stars in a row , s= no of spaces btwn the stars in the middle rows
s - r=0                    s - r=1                                           s - r=2
* * *                      * * * *                                           * * * * *
*   *                      *     *                                           *       *
* * *                      *     *                                           *       *
                           * * * *                                           *       *
                                                                             * * * * *
3 spaces btwn              5 spaces btwn                                     7 spaces btwn
the midlle stars           the middle stars                                  the middle stars
"""
def take_input():
    user_input=int(input("Enter an integer: "))
    return(user_input) # Throws the value out of this function; changes the variable scope from local to global
    # A local variable is destroyed at the end of executing the function from where it has been defined

def draw_square(value):
    Subtractor=3# Local variable
    if value>=3:
        n=value-Subtractor
    else:
        print(f'Sorry, the value {value} should be greater than 3')
        take_input()

    """
    The difference between the number of asterisks in a row and the number of empty spaces across asterisks that are 
    between the first and last rows is n where n=0,1,2,3,...
    Except for r=3(3 asterisks in a row), the method you can use to determine the amount of empty spaces you should
    leave to be able to draw a square is just taking r+n where n is the difference between the number of asterisks 
    per row and a standard subtractor=3.
    """

    for row in range(value):
        if value==3: 
        # condition is only applicable when r1 is filled with 3 spaced stars. r=3 has a unique xtic where the s=r
        # s= number of empty spaces btwn the stars(first and last) in the middle rows
            if row==0 or row==value-1:# first and last rows
                print("* " * value)
            else:
                print("*" + " "*value + "*")
        else:
            if row==0 or row==value-1:
                print("* " * value)
            else:
                print("*" + " "*(value+n) + "*")

def main():
    print("Enter a number n and I'll display a square with n rows and n columns.")
    value=take_input()
    draw_square(value)

if __name__=="__main__":
    main()

