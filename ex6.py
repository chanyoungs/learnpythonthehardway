# Adds an integer placeholder (%f for float placeholder)
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# Adds multiple integer placeholders and is placed with the items in parentheses separated by commas
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# Printing %r(raw data) prints the string x with quotes around to show that it was a string
print "I said: %r." % x
# Printing %s prints the string y without quotes
print "I also said: '%s'." % y

hilarious = False
# You can make a variable with an unfilled placeholder
joke_evaluation = "Isn't that joke so funny?! %r"

# You can print a variable and adding the item to be filled in the placeholder at this instance
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# You can concatenate prints with '+' but you can concatenate with an automatic space with ','
print w + e
