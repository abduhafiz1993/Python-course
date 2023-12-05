#Unit test
Notice that we are importing the square function from square.py on the first line of code. By convention, we are creating a function called test_square. Inside that function, we define some conditions to test.

In the console window, type python test_calculator.py. You’ll notice that nothing is being outputted. It could be that everything is running fine! Alternatively, it could be that our test function did not discover one of the “corner cases” that could produce an error.
Right now, our code tests two conditions. If we wanted to test many more conditions, our test code could easily become bloated. How could we expand our test capabilities without expanding our test code?

## Assert 

Python’s assert command allows us to tell the compiler that something, some assertion, is true.

## Pytest

pytest is a third-party library that allows you to unit test your program. That is, you can test your functions within your program.
To utilize pytest please type pip install pytest into your console window.
Before applying pytest to our own program.

## Organizing Tests into Folders

Unit testing code using multiple tests is so common that you have the ability to run a whole folder of tests with a single command.
First, in the terminal window, execute mkdir test to create a folder called test.
Then, to create a test within that folder, type in the terminal window code test/test_hello.py. Notice that test/ instructs the terminal to create test_hello.py in the folder called test.
