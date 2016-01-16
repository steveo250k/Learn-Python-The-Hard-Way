from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you  don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

"""
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')
""" 
line_all = "%s %s %s %s %s %s " % (line1, '\n', line2, '\n', line3, '\n')
target.write(line_all)

print "And finallhy, we close it."
target.close()

print "Reopen %s for reading." % filename
target = open(filename, 'r')
print target.read()


