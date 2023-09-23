# Get seconds from user
seconds = int(input("Enter a number of seconds: "))

# Calculate days
days = seconds // (24 * 60 * 60)
# Calculate hours
hours = (seconds % (24 * 60 * 60)) // (60 * 60)
# Calculate minutes
minutes = (seconds % (60 * 60)) // 60
# Calculate seconds
seconds = seconds % 60

# Print result
print(str(seconds) + " seconds is " + str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes and " + str(seconds) + " seconds")