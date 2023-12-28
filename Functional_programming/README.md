# Functional Programming


 Python also supports the Functional Programming Paradigm, in which functions are treated as values just like any other variable.

 ### Decorators

One thing made possible by functional programming is the idea of a decorator, which is a higher-order function that can modify another function. For example, let’s write a decorator that announces when a function is about to begin, and when it ends. We can then apply this decorator using an @ symbol.


### Lambda Functions

Lambda functions provide another way to create functions in python. For example, if we want to define the same square function we did earlier, we can write:
```bash
    square = lambda x: x * x
```
Where the input is to the left of the : and the output is on the right.

This can be useful when we don’t want to write a whole separate function for a single, small use. For example, if we want to sort some objects where it’s not clear at first how to sort them. Imagine we have a list of people, but with names and houses instead of just names that we wish to sort:
