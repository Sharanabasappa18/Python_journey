# s="madam"   # for taking direct string 
s=input("Enter a name : ")  # for taking the string from user
reverse=""

for char in s:
    reverse=char+reverse
if s== reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
