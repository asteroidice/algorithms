def newton_sqrt(D):
    if 0 > D:
        raise ValueError("math domain error")
    # the case where n = 0
    x_n = __x_0(D)
    # perform teh first iteration to calculate n = 1.
    x_np1 = __x_np1(D, x_n)

    # itteratively calculate x_(n+1) and update x_n to reflect the new values.
    # Do this until x_n is sufficiently close to x_(n+1).
    while abs(x_n - x_np1) > 0.00001:
        x_n = x_np1
        x_np1 = __x_np1(D, x_np1)
    return (x_np1)

"""
The following two functions represent the recurence relation for newton's
method when calculating the value of a square root.
"""
def __x_0(D):
    return ((1 + D) / 2)

def __x_np1(D, x_n):
    return ( 0.5*( x_n + D/x_n ) )
