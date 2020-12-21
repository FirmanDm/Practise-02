from factorial import factorial
from exp_root import exponentiation, root
from logarithm import logarithm


def float_check(x):
    while type(x) != float:
        try:
            x = float(x)
        except ValueError:
            x = input("Error: your input is not float. Please, enter another number:")
    return x


def int_check(x):
    while type(x) != int:
        try:
            x = int(x)
        except ValueError:
            x = input("Error: your input is not integer. Please, enter another number:")
    return x


def main():
    while True:
        print("--------------------------")
        print('Choose the operation you want to do. Input:\n'
              '"1" for factorial;\n'
              '"2.1" for square of number, "2.2" for cube of number;\n'
              '"3.1" for square root, "3.2" for cube root;\n'
              '"4.1" for ln of number, "4.2" for lg of number, "4.3" for log of number with your base;\n'
              'anything else to stop the program.')
        ans = input("Your choice:")
        if ans == "1":
            n = int_check(input("Enter your number(must be natural):"))
            while True:
                if n <= 0:
                    print("Error: your number is not natural. Choose another number.")
                    n = int_check(input("Enter your number(must be natural):"))
                else:
                    break
            print("Your factorial is:", factorial.fact(n))
        elif ans == "2.1":
            n = float_check(input("Enter your number:"))
            print("Square of your number is:", exponentiation.exp2(n))
        elif ans == "2.2":
            n = float_check(input("Enter your number:"))
            print("Cube of your number is:", exponentiation.exp3(n))
        elif ans == "3.1":
            n = float_check(input("Enter your number(must be non-negative):"))
            while True:
                if n < 0:
                    print("Can`t find square root of your number. Please, choose another number.")
                    n = float_check(input("Enter your number(must be non-negative):"))
                else:
                    break
            print("Square root of your number is:", root.root2(n))
        elif ans == "3.2":
            n = float_check(input("Enter your number:"))
            print("Cube root of your number is:", root.root3(n))
        elif ans == "4.1":
            n = float_check(input("Enter your number(must be non-negative):"))
            while True:
                if n <= 0:
                    print("Can`t find ln of your number. Please, choose another number.")
                    n = float_check(input("Enter your number(must be non-negative):"))
                else:
                    break
            print("ln of your number is:", logarithm.ln(n))
        elif ans == "4.2":
            n = float_check(input("Enter your number(must be non-negative):"))
            while True:
                if n <= 0:
                    print("Can`t find ln of your number. Please, choose another number.")
                    n = float_check(input("Enter your number(must be non-negative):"))
                else:
                    break
            print("lg of your number is:", logarithm.lg(n))
        elif ans == "4.3":
            a = float_check(input("Enter your base(must be non-negative and not equals to 1):"))
            while True:
                if a < 0 or a == 1:
                    print("Can`t be base of logarithm. Please, choose another number.")
                    a = float_check(input("Enter your number(must be non-negative):"))
                else:
                    break
            b = float_check(input("Enter your number(must be non-negative):"))
            while True:
                if b <= 0:
                    print("Can`t be base of logarithm. Please, choose another number.")
                    a = float_check(input("Enter your number(must be non-negative):"))
                else:
                    break
            print("log of your number with your base is:", logarithm.log(a, b))
        else:
            print("Wrong input, so work is stopped. Thank you for using this program!")
            break


if __name__ == '__main__':
    main()
