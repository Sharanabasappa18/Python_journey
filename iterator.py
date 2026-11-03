import itertools
numbers=(1,2,3)
result=itertools.permutations(numbers,2)
for i in result:
    print(i)