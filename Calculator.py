def add2no(a,b):
    return a+b
def sub2no(a,b):
    return  a-b
def mul2no(a,b):
    return  a*b
def div2no(a,b):
    return  a/b
if __name__=="__main__":
   a  = int(input("enter the 1st no"))
   b = int(input("enter the 2nd no"))

   add=add2no(a,b)
   sub=sub2no(a,b)
   print(sub)
   mul=mul2no(a,b)
   print(mul)

   div=div2no(a,b)
   print(div)


