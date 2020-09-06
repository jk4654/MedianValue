a=[86,72,79,97,81,77,80,86,82,90,79,88,86,93,84,75]
a.sort()
print(a)
if len(a) % 2 == 1 :
    print(a[round(len(a)/2)])
elif len(a) % 2 == 0 :
    print( ( a[ int(len(a)/2) ] + a[ int( (len(a)/2) - 1 )] ) /2 )