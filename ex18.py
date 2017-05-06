# *args takes any number of arguments and saves them as a list
def print_n(*args):
    arg1, arg2, arg3 = args
    print "arg1: %r, arg2: %r, arg3: %r" % (arg1, arg2, arg3)


def print_2(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)


def print_1(arg):
    print "arg: %r" % arg


def print_0():
    print "I got nothin'."

print_n("Zed", "Shaw", "Dek")
print_2("Zed", "Shaw")
print_1("First!")
print_0()
