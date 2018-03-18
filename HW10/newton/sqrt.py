def newton_sqrt(D):
    x_n = __x_0(D)
    x_np1 = __x_np1(D, x_n)
    while abs(x_n - x_np1) > 0.00001:
        x_n = x_np1
        x_np1 = __x_np1(D, x_np1)
    return (x_np1)


def __x_0(D):
    return ((1 + D) / 2)

def __x_np1(D, x_n):
    return ( 0.5*( x_n + D/x_n ) )
