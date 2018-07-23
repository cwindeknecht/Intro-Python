import sys
import os

# Module "sys"
#
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for arg in sys.argv:
    print("Argument:", arg)

# Print out the plaform from sys:
print("Platform:", sys.platform)

# Print out the Python version from sys:
print("Python Version:", sys.version)

# Module "os"
#
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("Current Process ID: ", os.getpid())

# Print the current working directory (cwd):
print("Current Working Directory:", os.getcwd())

# Print your login name
print("Login Name:", os.getlogin())
