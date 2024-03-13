#A simple calculator using the concept of oop's in python having multiple funtionality including Addition, substracion, mumtiplication, divide, modulous, square, squareroot, cube, cuberoot

class calculator:
    def __init__(self, num):
        self.number =num
    def square(self):
        print(f"The square of {self.number} is {self.number**2}")
    def squareroot(self):
        print(f"The squareroot of {self.number} is {self.number**0.5}")
    def cube(self):
        print(f"The cube of {self.number} is {self.number**3}")
    def cuberoot(self):
        print(f"The cuberoot of {self.number} is {self.number**(1/3)}")
    def __add__(self, num2):
        return self.number + num2.number    
    def __sub__(self, num2):
        return self.number - num2.number    
    def __mul__(self, num2):
        return self.number * num2.number    
    def __truediv__(self, num2):
        return self.number / num2.number  
    def __mod__(self, num2):
        return self.number % num2.number    
       
opp =input('''Enter the operation you want to perform 
           Enter '+' for addition
           Enter '-' for substraction
           Enter '*' for multiplication
           Enter '/' for division
           Enter '%' for modulous
           Enter square for square
           Enter squareroot for squareroot
           Enter cube for cube
           Enter cuberoot for cuberoot\n''')

if opp == 'square' or opp == 'squaroot' or opp =='cube' or opp =='cuberoot':
    num=int(input('Enter a number: '))
    obj =calculator(num)
    if opp=='square':
        obj.square()
    elif opp=='squareroot':
        obj.squareroot()
    elif opp=='cube':
        obj.cube()
    elif opp=='cuberoot':
        obj.cuberoot()
else:
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    a=calculator(num1)
    b=calculator(num2)
    if opp=='+':
        add=a+b
        print(f'The sum of the number is {a+b}')
    if opp=='-':
        add=a-b
        print(f'The substraction of the number is {a-b}')
    if opp=='*':
        add=a*b
        print(f'The multiplication of the number is {a*b}')
    if opp=='/':
        add=a/b
        print(f'The dividation of the number is {a/b}')
    if opp=='%':
        add=a%b
        print(f'The modulous of the number is {a%b}')
print("Thank you for using this calculator")