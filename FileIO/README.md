#File I/O 

File I/o is the ability of a program to take a file as input or create a file as output.
open is a functionality built into Python that allows you to open a file and utilize it in your program. The open function allows you to open a file such that you can read from it or write to it.

Notice that the open function opens a file called names.txt with writing enabled, as signified by the w. The code above assigns that opened file to a variable called file. The line file.write(name) writes the name to the text file. The line after that closes the file.

Testing out your code by typing python names.py, you can input a name and it saves to the text file. However, if you run your program multiple times using different names, you will notice that this program will entirely rewrite the names.txt file each time.

## With

p until this point, we have been exclusively writing to a file. What if we want to read from a file. To enable this functionality

## readline()

 readlines has a special ability to read all the lines of a file and store them in a file called lines. Running your program, you will notice that the output is quite ugly. There seem to be multiple line breaks where there should be only one.
## rstrip()

rstrip has the effect of removing the extraneous line break at the end of each line.

## CSV

CSV stands for “comma separated values”.

Notice that rstrip removes the end of each line in our CSV file. split tells the compiler where to find the end of each of our values in our CSV file. row[0] is the first element in each line of our CSV file. row[1] is the second element in each line in our CSV file.

## CSV built in function

Python’s built-in csv library comes with an object called a reader. As the name suggests, we can use a reader to read our CSV file despite the extra comma in “Number Four, Privet Drive”. 
A reader works in a for loop, where each iteration the reader gives us another row from our CSV file. This row itself is a list, 
where each value in the list corresponds to an element in that row. row[0], 
for example, is the first element of the given row, while row[1] is the second element.

## DictReader()

Notice that we have replaced reader with DictReader, which returns one dictionary at a time. Also, notice that the compiler will directly access the row dictionary, getting the name and home of each student. This is an example of coding defensively. As long as the person designing the CSV file has inputted the correct header information on the first line, we can access that information using our program.

Up until this point, we have been reading CSV files. What if we want to write to a CSV file?
To begin, let’s clean up our files a bit. First, delete the students.csv file by typing rm students.csv in the terminal window. This command will only work if you’re in the same folder as your students.csv file

## Binary Files and PIL

One more type of file that we will discuss today is a binary file. A binary file is simply a collection of ones and zeros. This type of file can store anything including, music and image data.
There is a popular Python library called PIL that works well with image files.
Animated GIFs are a popular type of image file that has many image files within it that are played in sequence over and over again, creating a simplistic animation or video effect.
