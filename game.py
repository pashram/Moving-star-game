import termios, fcntl, sys, os, move

print '''
Press "a" or "d" to move left or right.
Press "f" to shoot and "x" to explode ;)
Press "q" to quit.
'''
fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
c = 0
e = 0
print " " * e, "*"

try:
    while c != 'q':
        try:
            c = sys.stdin.read(1)
            #print "Got character", repr(c)
            if c == "a":
                e = move.move_left(e)
                #print "e = ", e
            elif c == "d":
                e = move.move_right(e)
                #print "e = ", e
            elif c == "f":
                move.shoot(e)
            elif c == "x":
                move.explode()
            else:
                pass
        except IOError: pass
finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
