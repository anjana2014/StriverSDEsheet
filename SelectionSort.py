A = [3,64, 25, 12, 22, 11,80]
def selectionsort(A):
    n=len(A)
    for i in range(n):
        minindex=i
        for j in range(i+1,n):
            if A[minindex]>A[j]:
                 minindex=j
        A[i],A[minindex]=A[minindex],A[i]
    return A
    
print(selectionsort(A))
