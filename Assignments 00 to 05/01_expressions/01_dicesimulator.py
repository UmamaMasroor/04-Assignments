import random 
num_dice = 6

def roll_dice():
    die1: int = random.randint(1, num_dice)
    die2: int = random.randint(1, num_dice)
    total: int = die1 + die2
    print("Total of two dice:", total)

def main():
    

    die1: int = 10
    print("die1 in main() starts as: " , die1)
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " , die1)

if __name__ == '__main__':
    main()