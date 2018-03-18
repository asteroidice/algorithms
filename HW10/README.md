# HW 10 - Newton's Method
## Problem statement:
> 11.4 - 8
>
> Write a computer program to solve the equation ax^2 + bx + c = 0

Other requirements:

> Your submission must run on the CS Lab computers and include a detailed
README.md explaining how to execute your program. The code must be well
formatted and commented. You may use any programming language.

## Running the program
In the directory of this README, run the following command.
```bash
python main.py
```
Follow the prompts and then feast your eyes on the glories of newtons method.
### Example output
```
Enter a, b and c to solve for the folllowing equaiton.
 ax^2 + bx + c = 0
a = 1
b = 10E5
c = 1

Newton's method solution:
(-0.000001, -999999.999999)
Default python solution:
(-0.000001, -999999.999999)
Sqrt comparison:
newton: 999999.999998 , native: 999999.999998
```

## Diving into code
There are two main scripts/packages responsible for this program.
1. **`newton/sqrt.py`** is the script responsible for calculating the square root
using newton's method.

2. **`main.py`** is the main script that handles user input and calculates the
remaining portion of the quadratic formula.

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
There are a number of methods for ensuring the answer is sufficiently close to
√D. One such way to ensure this is to arbitrarily choose an accuracy and
and iterate till this accuracy is met. See the following snippet from the book.

>We can stop generating its elements either when the difference between its two consecutive elements is less than a predefined error tolerance ε > 0

Another way of ensuring accuracy is as follows. The above recursion relation
quickly converges to the correct value of √D if 0.25 < D < 1. It can be
proven that it will only take four (4) iterations and be within very reasonable tolerances.
However, because the book didn't elaborate well on how to scale any value of D
while maintaining the actual value of a square root, this method was not used.
