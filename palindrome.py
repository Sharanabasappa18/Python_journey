# s="madam"
s=input("Enter a name : ")
reverse=""

for char in s:
    reverse=char+reverse
if s== reverse:
    print("Palindrome")
else:
    print("Not Palindrome")