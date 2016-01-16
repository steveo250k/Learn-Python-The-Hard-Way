from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is", first
print "Your second variable is", second
print "Your third variable is", third

print "Another way is indexes"
print "The script is called:", argv[0]
print "Your first variable is", argv[1]
print "Your second variable is", argv[2]
print "Your third variable is", argv[3]
