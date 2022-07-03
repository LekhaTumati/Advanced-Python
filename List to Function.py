
def count(lst):

    even = 0
    odd = 0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+= 1
    return even, odd

lst = [10,20,37,40,50,60,73,81]

even, odd = count(lst)
#print('Even : { } and Odd : { }'.format(even, odd))
print("Even: ", even)
print("Odd: ", odd)