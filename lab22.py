print(" *** Quadratic Solver ***")
print(" *   ax^2 + bx + c = 0  *")
print(" ************************")
inp=input("Enter a b c : ")
a,b,c=inp.split()
a=int(a)
b=int(b)
c=int(c)
try:
    x= (-b+((b**2)-(4*a*c))**0.5)//(2*a)
    y= (-b-((b**2)-(4*a*c))**0.5)//(2*a)
    x=int(x)
    y=int(y)
    if x==y:
        print(f"x = {x}")
    else :
        print(f"x1 = {y}")
        print(f"x2 = {x}")
except:
    print("Skip this case !!!")