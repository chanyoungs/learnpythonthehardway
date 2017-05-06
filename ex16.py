from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# adding , 'w' in the open module opens the file in a writable mode. Otherwise, we cannot edit the text.
# empty parameter opens it in 'r' reading mode by default
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
# Erases all contents of the file. Q: Is this necessary? A: python truncates the file in 'w' mode automatically so no.
target.truncate()

print "Now I'm going to ask you for three lines."

# Assigns 3 lines into the three variables
line1, line2, line3 = raw_input("line 1: "), raw_input("line 2: "), raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%s\n%s\n%s" % (line1, line2, line3))

print "And finally, we close it."
target.close()
