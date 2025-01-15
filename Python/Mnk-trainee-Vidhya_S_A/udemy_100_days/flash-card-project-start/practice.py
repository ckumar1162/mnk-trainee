def foo(a, b=[]):
    b.append(a)
    return b

print(foo(1))  # First call
print(foo(2, []))  # Second call
print(foo(3))