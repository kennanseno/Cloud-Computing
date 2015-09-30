myString = raw_input("Enter a String: ")
# reverse the string
revString = reversed(myString)
# check if the string is equal to its reverse
if list(myString) == list(revString):
   print("True")
else:
   print("False")


