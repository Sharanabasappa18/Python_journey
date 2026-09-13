# name = input("what's your name? ")
# # print("hello,",name,sep="bsdk")
# print("hello, ",end="")
# name=name.strip()
# name=name.title()
# print(name)

def main():
    name=input("What s ur name?")
    print(hello(name))
def hello(to="World"):
    return f"hello, {to}"
    
if __name__=="__main__":
    main()
    