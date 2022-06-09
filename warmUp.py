#Solve me First

def solveMeFirst(a,b):
    return a+b

def simpleArraySum(ar):
    return sum(ar)

def compareTriplets(a,b):
    alicepoint = 0
    bobpoint = 0
    for pointa,pointb in zip(a,b):
        if pointa > pointb:
            alicepoint += 1
        elif pointa < pointb :
            bobpoint += 1
        else :
            pass
    return alicepoint, bobpoint