add = lambda x,y: x+y
print(add(2,3))

def math(a,b,f):
    return f(a,b)

print(math(3,3,lambda x,y: x+y))
print(math(3,3,lambda x,y: x*y))