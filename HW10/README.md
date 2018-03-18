# HW 10 - Newton's Method
## Problem statement:
> 11.4 - 8
>
> Write a computer program to solve the equation ax^2 + bx + c = 0

Advisement:

> Your submission must run on the CS Lab computers and include a detailed
README.md explaining how to execute your program. The code must be well
formatted and commented. You may use any programming language.

## Design Process

### Mathematics
The quadratic formula can be used to solve for the aforementioned equation. The
quadratic equation is as follows.
```
x_1,2 = ( -b ± sqrt( b^2 - 4ac ) ) / 2a
```
From the description in the book it seems that the only non-basic operation
listed in this process is the Square root operation. Thankfully there are other
 ways to calculate the square-root of a given function.

### Newton's Method for Square Roots
Newton's method for Square Roots is an iterative way to calculate the square
root of a value. To do this the following formula can be used.
```
x_0 = (1 + D) / 2
x_(n + 1) = 1/2 ( x_n + D/x_n )
```
This recursion relation quickly converges to the correct value of √D. It can be
proven that it will only take four (4) iterations and be within reasonable tolerances.

### Other implications with the discretization of the quadratic formula
#### subtractive cancellation
The book mentions that there are cases such as `x^2 + 10E5x + 1 = 0` where the
risk of subtractive cancellation is very high. To rectify this issue the
following formula can be used for x_1 instead.
```
x_1 = 2c / (-b - sqrt( b^2 - 4ac) )
```

## Running the program
