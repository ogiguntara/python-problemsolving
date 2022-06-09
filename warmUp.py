#Solve me First

def solveMeFirst(a,b):
    return a+b

def simpleArraySum(ar):
    return sum(ar)

def compareTriplets(a,b):
    alicepoint = 0
    bobpoint = 0
    for pointa,pointb in zip(a,b): #pairing using zip function
        if pointa > pointb:
            alicepoint += 1
        elif pointa < pointb :
            bobpoint += 1
        else :
            pass
    return alicepoint, bobpoint

def aVeryBigSum(ar):
    return sum(ar)

def diagonalDifference(arr):
    primary = 0
    secondary = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j :
                primary += arr[i][j]
            if i+j == len(arr[i])-1:
                secondary += arr[i][j]
    return abs(primary-secondary)