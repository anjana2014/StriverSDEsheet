A = [3,64, 25, 12, 22, 11,80]
def bubblesort(A):
    n=len(A)
    for i in range(n):
        for j in range(i+1,n):
            if A[i]>A[j]:
                 A[i],A[j]=A[j],A[i]
    return A
    
print(bubblesort(A))
