# Author: 2025 Mikhail Ibrahim
# Date: May 7th, 2025
# Description: A crash-proof Python program that calculates the area of a triangle.
# It accepts base and height values from the user, handles invalid input safely,
# and ensures only positive numeric input is processed.


def calc_area(base, height):
    area = 0.5 * base * height
    print(f"The area of the triangle is {area:.2f} cm²")


def main():
    print("Welcome to the Triangle Area Calculator")

    try:
        base = float(input("Enter base (cm): "))
        height = float(input("Enter height (cm): "))

        if base <= 0 or height <= 0:
            print("Error: Base and height must be positive numbers.")
        else:
            calc_area(base, height)

    except ValueError:
        print("Invalid input. Please enter numeric values only.")


# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
