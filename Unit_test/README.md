#Unit test
Notice that we are importing the square function from square.py on the first line of code. By convention, we are creating a function called test_square. Inside that function, we define some conditions to test.

In the console window, type python test_calculator.py. You’ll notice that nothing is being outputted. It could be that everything is running fine! Alternatively, it could be that our test function did not discover one of the “corner cases” that could produce an error.
Right now, our code tests two conditions. If we wanted to test many more conditions, our test code could easily become bloated. How could we expand our test capabilities without expanding our test code?

## Assert 

Python’s assert command allows us to tell the compiler that something, some assertion, is true.
