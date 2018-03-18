from newton.sqrt import newton_sqrt
import math, sys

"""
This function prompts the user for a number and typecasts that number to
a float. If this cannot be done, the function will stop the execution of the
program with a failed exit code.
"""
def prompt(query):
    sys.stdout.write(query)
    try:
        return(float(input()))
    except ValueError:
        print("The value you entered cannot be typecased to float.")
        sys.exit(1)

"""
This is the main function block. It makes use of the speciallized
`newton_sqrt()` and compares the result of the quadratic equation with the
native python funcitons for sqrt.
"""
def main():
    print("Enter a, b and c to solve for the folllowing equaiton.\n "
        "ax^2 + bx + c = 0\n"
        "NOTE: Values where 4ac > b^2 will raise a ValueError.")

    # prompt the user for values.
    a = prompt("a = ")
    b = prompt("b = ")
    c = prompt("c = ")

    # solve the quadratic equation.
    print("Newton's method solution:")
    x_1 = ( -b + newton_sqrt( b*b - 4*a*c ) ) / 2*a
    x_2 = ( -b - newton_sqrt( b*b - 4*a*c ) ) / 2*a

    # Output results
    print("(%f, %f)" % (x_1, x_2))

    # solve the quadratic equation using native functions.
    print("Default python solution:")
    x_1p = ( -b + math.sqrt( b*b - 4*a*c ) ) / 2*a
    x_2p = ( -b - math.sqrt( b*b - 4*a*c ) ) / 2*a

    # Output results
    print("(%f, %f)" % (x_1p, x_2p))

    # for testing purposes show the similarity between custom and native sqrt().
    print("Sqrt comparison:")
    D = b*b - 4*a*c
    print("newton: %f , native: %f" % (newton_sqrt(D), math.sqrt(D)))

# This ensures that the code will run only if main.py is the script being called.
if __name__ == "__main__":
    main()
