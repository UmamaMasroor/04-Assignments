import random
def main():
    die_1:int = random.randint(1, 6)
    die_2:int = random.randint(1, 6)
    total:int= die_1 + die_2

    print("First die:", die_1)
    print("Second die:", die_2)
    print("Total of two dice:", total)

if __name__ == '__main__':
    main()