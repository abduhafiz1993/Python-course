#File I/O 

File I/o is the ability of a program to take a file as input or create a file as output.
open is a functionality built into Python that allows you to open a file and utilize it in your program. The open function allows you to open a file such that you can read from it or write to it.

Notice that the open function opens a file called names.txt with writing enabled, as signified by the w. The code above assigns that opened file to a variable called file. The line file.write(name) writes the name to the text file. The line after that closes the file.

Testing out your code by typing python names.py, you can input a name and it saves to the text file. However, if you run your program multiple times using different names, you will notice that this program will entirely rewrite the names.txt file each time.