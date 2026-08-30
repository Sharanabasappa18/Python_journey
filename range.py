# # # for i in range(1,5):
# # #     print(+i)

# # a=10
# # print(a+1)

# a=[1,2,3,]
# b=[1,2,3,]
# print(a==b)
# print(a)


a=[1,2,3,4]
b=a.copy()
b.append(4)
print(id(a))
print(id(b))
print(b)
print(a)