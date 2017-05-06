print "Let's practice everything."
print 'You\'d need to know \'bout escaes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is note.
"""

print "------------------"
print poem
print "------------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five


def secret_formula(started):
    formula_beans = started * 500
    formula_jars = formula_beans / 1000
    formula_crates = formula_jars / 100
    return formula_beans, formula_jars, formula_crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point /= 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
