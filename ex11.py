# ',' at the end of the print line means the user inputs on the same line as opposed to the next line
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

# Interestingly, if you include inverted comma in an input, the output comes out with an escape character
# This is so that when the reader reads it, the reader can know that that inverted comma is still inside the string
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
