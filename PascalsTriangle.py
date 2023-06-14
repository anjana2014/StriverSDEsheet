class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1, numRows+1):
            
            result.append(self.generateRow(i))
            
        return result

    def generateRow(self, row: int) -> List[int]:
        ans = 1
        temprow=[1]
        for i in range(1,row):
            ans = ans * (row - i)
            ans = ans // (i)
            temprow.append(ans)
        return temprow
