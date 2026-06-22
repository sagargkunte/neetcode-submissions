class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = list()
        n = numRows
        for i in range(n):
            i_list = []
            i_list.append(1)
            for j in range(i-1):
                i_list.append(arr[i-1][j]+arr[i-1][j+1])
            if i > 0:
                i_list.append(1)
            arr.append(i_list)
        
        return arr