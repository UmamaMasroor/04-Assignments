print("Thiis program calculate the perimeter of the triangle")
def main():
    user_input1= float(input("What is the length of side 1? "))
    user_input2= float( input("What is the length of side 2? "))
    user_input3= float(input("What is the length of side 3? "))

    result = user_input1 + user_input2 + user_input3
    print("The perimeter of the triangle is: ", result)

if __name__ == '__main__':
    main()