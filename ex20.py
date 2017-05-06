from sys import argv


script, input_file = argv


# Prints f.read() which is the string of f
def print_all(f):
    print f.read()


# f.seek(0) puts the "cursor" to the 0th character of the string of f. seek can take
# a second optional argument 1(seek relative to current position) or 2 (seek relative to the end of file)
def rewind(f):
    f.seek(-10)


# f.readline(n) outputs a string from f on the line n
def print_a_line(line_count, f):
    print line_count, f.readline()

# open(input_file) is the file pointer(?) to the file name input_file is
# being assigned to the variable tame current_file
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
