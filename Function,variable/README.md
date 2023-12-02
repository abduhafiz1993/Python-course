# Functions
Functions are verbs or actions that the computer or computer language will already know how to perform.
In your hello.py program, the print function knows how to print to the terminal window.
The print function takes arguments. In this case, "hello, world" are the arguments that the print function takes
## Comments
Comments are a way for programmers to track what they are doing in their programs and even inform others about their intentions for a block of code. In short, they are notes for yourself and others that will see your code!
You can add comments to your program to be able to see what it is that your program is doing. You might edit your code as follows


We can use a comma , to pass in multiple arguments by editing our code as follows
Notice how adding quotation marks as part of your string is challenging.
print("hello,"friend"") will not work and the compiler will throw an error.
Generally, there are two approaches to fixing this. First, you could simply change the quotes to single quote marks.
Another, more commonly used approach would be code as print("hello, \"friend\""). The backslashes tell the compiler that the following character should be considered a quotation mark in the string and avoid a compiler error.

## String and their function

You should never expect your user will cooperate as intended. Therefore, you will need to ensure that the input of your user is corrected or checked.
It turns out that built into strings is the ability to remove whitespace from a string.
By utilizing the method strip on name as name = name.strip(), it will strip all the whitespaces on the left and right of the users input. You can modify your code to be

## Integers

In Python, an integer is referred to as an int.
In the world of mathematics, we are familiar with +, -, *, /, and % operators. That last operator % or modulo operator may not be very familiar to you.
You don’t have to use the text editor window in your compiler to run Python code. Down in your terminal, you can run python alone. You will be presented with >>> in the terminal window. You can then run live, interactive code. You could type 1+1 and it will run that calculation. This mode will not commonly be used during this course.

## Float Basics

A floating point value is a real number that has a decimal point in it, such as 0.52.

Let’s imagine, however, that you want to round the total to the nearest integer. Looking at the Python documentation for round you’ll see that the available arguments are round(number[n, ndigits]). Those square brackets indicate that something optional can be specified by the programmer. Therefore, you could do round(n) to round a digit to its nearest integer.

## DEf

It use to create our function

## Returning Values

You can imagine many scenarios where you don’t just want a function to perform an action, but also to return a value back to the main function. For example, rather than simply printing the calculation of x + y, you may want a function to return the value of this calculation back to another part of your program. This “passing back” of a value we call a return value.
