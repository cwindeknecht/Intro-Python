def myfunction(a,b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myfunction(1,2,) #args empty tuple, kwargs empty dict
myfunction(1,2,3,4) #args gathers non-positional arguments, kwargs empty dict
myfunction(1,2,3,4,x=5) #kwargs is a dict with a key of x and a value of 5

d = {'1':1,'2':2,'3':3}
myfunction(1,2,3,4,**d, y=5) #dict / y is kwargs
myfunction(1,2,3,4,d) #dict is part of args
myfunction(1,2,*d) #passes keys into args array
myfunction(1,2,*d.values()) #passes values into args array

# **kwargs has to be a dict
# *args can be either a list or a dict
    # if it is a dict, it will only be keys without .values() appended 