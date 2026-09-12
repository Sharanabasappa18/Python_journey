# import sys 
# print("hello my name is ",sys.argv[4])

# import sys
# try:
#     print("hello my name is ",sys.argv[4])
# except IndexError:
#     print("Too few arguments ")

# import sys
# if len(sys.argv)<2:
#     # print("Too few arguments ")
#     sys.exit("Too few arguments ")
# elif len(sys.argv)>2:
#     # print("Too many arguments")
#     sys.exit("Too many arguments")
# else:
#     print("hello, my name is ",sys.argv[1])


import sys
if len (sys.argv)<2:
    sys.exit("Too few arguments ")
# for arg in sys.argv:
for arg in sys.argv[1:]:        # slices
    print("hello,my name is ",arg)