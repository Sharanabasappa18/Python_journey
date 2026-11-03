import itertools
numbers=(1,2,3)
result=itertools.combinations(numbers,2)   #combinations
result=itertools.permutations(numbers,2) #permutations
for i in result:
    print(i)