C: int = 299792458
def main():
    mass:float = float(input("Enter kilos of mass: "))
    E = mass*(C**2)
    print("e = m * C^2")
    print("mass (m) = ", mass, "kg")
    print("C = ", C , "m/s")
    print(E, "joules of energy")


if __name__ == '__main__':
    main()