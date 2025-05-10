print("This program converts temperature from fahrenheit to celsius")

def main():
    user_input = float (input("Enter temperature in Fahrenheit: "))
    degrees_celsius = (user_input - 32) * 5.0/9.0
    print("Temperature: ", user_input , "F = ", degrees_celsius , "C")

if __name__ == '__main__':
    main()