class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedarr=sorted(nums)
        n=len(nums)
        r=n-1
        l=0
        while(l<r):
            
            if (sortedarr[l]+sortedarr[r])==target:
                first=nums.index(sortedarr[l])
                if (sortedarr[l]==sortedarr[r]):
                    
                    nums.remove(sortedarr[l])
                    second=nums.index(sortedarr[r])+1
                else:   
                    second=nums.index(sortedarr[r])
                return [first,second]
            elif (sortedarr[l]+sortedarr[r]>target):
                   r=r-1
            else:
                  l=l+1
        
