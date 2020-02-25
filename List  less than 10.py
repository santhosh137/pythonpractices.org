a=[1,1,2,3,5,8,13,21,34,55,89]

def less_than_10(a):
    count=0

    for i in a:
        if i <5:
            count=count+1
        else:
            pass
    print (count)

less_than_10(a)