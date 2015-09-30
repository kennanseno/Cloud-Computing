myString = raw_input("Enter a String: ")

revString = reversed(myString)

if list(myString) == list(revString):
   print("True")
else:
   print("False")


