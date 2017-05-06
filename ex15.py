# Imports argv which takes argument from running this file
from sys import argv

# Assigns file name to script and the argument to the filename
script, filename = argv

# Opens the file with the given filename and assigns it to txt
txt = open(filename)

print "Here's your file %r:" % filename
# Tells txt to read itself so that txt.read() is a string and then prints it
print txt.read()
# It's important to close text after use(apparently)
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt.close()