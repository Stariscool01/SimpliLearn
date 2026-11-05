#Demo1A
import sys
randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occured.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)

#Catching specific exceptions & else clause
try:
    fh = open("c:\testlife", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: cannot find file or read data")
except ValueError:
    print("Could not convert data to an integer.")
else:
    print("Written content in the file successfully")
    fh.close()

#Clean up actions
try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
except:
    print("Error Occured")
finally:
    print("There may or may not have been an exception.")
    print("The inverse: ", inverse)

#raising exception
def readFile(fname):
    if fname.endswith(".txt"):
        print("success")
    else:
        raise ValueError("filename must end with txt")
# readFile("a.d");
# readFile("a.txt");


#Demo1B
#Custom exception
#define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass
class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass
class VAlueTooLargeError(Error):
    """Raised when the input is too large"""
    pass

number = 10

while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise VAlueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except VAlueTooLargeError:
        print("This value is too large, try again!")
        print()
print("Congratulations! You guessed it correctly.")