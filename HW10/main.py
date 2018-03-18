from newton.sqrt import newton_sqrt
import math, sys

def prompt(query):
    sys.stdout.write(query)
    try:
        return(float(input()))
    except ValueError:
        print("The value you entered cannot be typecased to float.")
        sys.exit(1)


def main():
    print("Enter a, b and c to solve for the folllowing equaiton.\n ax^2 + bx + c = 0")

    a = prompt("a = ")
    b = prompt("b = ")
    c = prompt("c = ")

    print("Newton's method solution:")
    x_1 = 2*c / (-b - newton_sqrt( b*b - 4*a*c ) )
    x_2 = ( -b - newton_sqrt( b*b - 4*a*c ) ) / 2*a


    print("(%f, %f)" % (x_1, x_2))    

    print("Default python solution:")
    x_1p = ( -b + math.sqrt( b*b - 4*a*c ) ) / 2*a
    x_2p = ( -b - math.sqrt( b*b - 4*a*c ) ) / 2*a

    print("(%f, %f)" % (x_1p, x_2p))

    print("Sqrt comparison")
    D = b*b - 4*a*c
    print("newton: %f , native: %f" % (newton_sqrt(D), math.sqrt(D)))

if __name__ == "__main__":
    main()
