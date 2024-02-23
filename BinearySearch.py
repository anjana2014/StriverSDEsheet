arr = [2, 3, 4, 10, 40]
x = 20
def binarysearch(arr,x):
    n=len(arr)
    l=0
    r=n-1
    while l<=r:
          mid=l+(r-l)//2
          if arr[mid]==x:
               return True
          elif arr[mid]<x:
               l=mid+1
          else:
               r=mid-1
    return False
               
print(binarysearch(arr,x))
