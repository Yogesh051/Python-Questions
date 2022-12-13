def name(x):
    return lambda a,b :a+b+x

num = name(10)
print(num(5,5))
