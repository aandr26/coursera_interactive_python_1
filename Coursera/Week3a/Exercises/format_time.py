# Define a function that returns formatted minutes and seconds

###################################################
# Time formatting function
# Student should enter function on the next lines.

def format_time(number):
    minutes = number // 60
    print ("These are the minutes: " + str(minutes))
    print ("This is the number: " + str(number))
    print ("")
    seconds = number % 60
    print (minutes + seconds)

###################################################
# Tests

print (format_time(23))
print (format_time(1237))
print (format_time(0))
print (format_time(1860))

###################################################
# Output to console
#0 minutes and 23 seconds
#20 minutes and 37 seconds
#0 minutes and 0 seconds
#31 minutes and 0 seconds
