# Write a function is_even that will return true if the passed in number is even.

# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"
def evenChecker(x):
    if int(x) % 2 is 0:
        return "Even"
    return "Odd"

print(evenChecker(num))