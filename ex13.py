# argv is the argument variable
from sys import argv

# Unpacks argv to variables. The zeroth argument is the name of the file by default
script, first, second, third, fourth = argv

print "The script is called:", script
print "Your fist variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth

a = raw_input("Input anything ")
print "You typed %r" % a
