def move_left(e):
    if e > 0:
        e -= 1
    else:
        pass

    print " " * e, "*", " " * (50 - e), "\r",
    return e

def move_right(e):
    e += 1
    print " " * e, "*", " " * (50 - e), "\r",
    return e

def move_down(e):
    print " " * e, "*"
    return e

def shoot(e):
    for i in range(10):
        print " " * e, "*", " " * (50 - e)
        print " " * e, " *", " " * (50 - e)
    return e

def explode():
    for i in range(20):
        print " *" * 40
        print "* " * 40
