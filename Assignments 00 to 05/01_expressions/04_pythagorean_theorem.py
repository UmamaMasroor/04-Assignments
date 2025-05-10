import math  
print("This program outputs the length of the third side (the hypotenuse) of triangle using the Pythagorean theorem!")
def main():
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    bc: float = math.sqrt(ab**2 + ac**2)
    print("The length of BC (the hypotenuse) is: " , bc)


if __name__ == '__main__':
    main()