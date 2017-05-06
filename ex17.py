from sys import argv
# exists returns True or False depending on whether the file with the input filename string exists
from os.path import exists

# from_file is the filename to open, to_file is filename to write
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# We could make this a single line by doing indata = iopen(from_file).read()
in_file = open(from_file)
indata = in_file.read()

# The place to close the input file is right after you're done reading the data, and before opening the output file.
in_file.close()

# len(indata) returns the number of bytes
print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
