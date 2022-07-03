
a = 10
print(id(a))
def something():
    a=9
    x = globals()['a']
    print("in fun", a)
    print(id(x))

    globals()['a'] = 15

something()

print("ouutside" ,a)