# to show how return function works
"""def my_function(f_name, l_name):
    firstname=f_name.title()
    lastname=l_name.title()
    return f"{firstname} {lastname}"
name=my_function("usha","k")
print(name)"""
#docstring
def usha(n1,n2):
    """adds two number"""
    print(n1+n2)
print(usha.__doc__)
usha(5,10)