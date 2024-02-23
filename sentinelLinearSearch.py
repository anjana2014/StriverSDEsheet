arr = [2, 3, 4, 10, 40]
x = 40
def senlinearsearch(arr,x):
    n=len(arr)
    last=arr[n-1]
    arr[n-1]=x
    i=0
    while arr[i]!=x:
          i+=1
    arr[n-1]=last
    if i<n-1 or arr[n-1]==x:
        return i
    else:
        return -1
               
print(senlinearsearch(arr,x))

# intially instead of last element we place our key element and store the last element in seperate variable to place it again back.Once it is done we traverse until the elements in i is not equal to key .
#place back the last element into the place .Now if the i value is less than n-1 or last element equal to key then the element is found at i otherwise element is not present in the array
