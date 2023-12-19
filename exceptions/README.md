# Runtime Errors
Runtime errors refer to those created by unexpected behavior within your code. For example, perhaps you intended for a user to input a number, but they input a character instead. Your program may throw an error because of this unexpected input from the user.

As programmers, we should be defensive to ensure that our users are entering what we expected. We might consider “corner cases” such as -1, 0, or cat.

If we run this program and type in “cat”, we’ll suddenly see ValueError: invalid literal for int() with base 10: 'cat' Essentially, the Python interpreter does not like that we passed “cat” to the print function.

An effective strategy to fix this potential error would be to create “error handling” to ensure the user behaves as we intend.

You can learn more in Python’s documentation of Errors and Exceptions.
