def main():
    num1:int = int(input("Please enter an integer to be divided: "))
    num2:int = int(input("Please enter an integer to be divided: "))
    remainder:int = num1 % num2
    quotient:int = num1 // num2
    print("The result of this division is ", quotient ," with a remainder of ", remainder)

if __name__ == '__main__':
    main()