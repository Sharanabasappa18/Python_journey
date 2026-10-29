add = lambda a, b: a + b
print(add(5, 3))

square = lambda x: x * x
print(square(4))

double=lambda x:x+x
mul=lambda x:x*2
cube=lambda x:x*x*x
Average=lambda x,y,z:(x+y+z)/3

print("Average",Average(2,4,7))
print("cube:",cube(3))
print("mul:",mul(2))
print("add: ",double(3))

# functions map(),filter() and sorted()
## map ## => it applies a function to every item in an iterable 
numbers=[1,2,3,4,5,6]
result=list(map(lambda x:x*2,numbers))

# filter() ==> it selects items that satisfy a condition  condition 
result2=list(filter(lambda a: a%2==0,numbers))
print(result)
print(result2)