class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r,c = len(matrix), len(matrix[0])
        row,col = False,False
       
        for i in range(r):
            for j in range(c):
                if(matrix[i][j]==0):
                    if i==0: row = True
                    if j==0: col = True
                    matrix[i][0], matrix[0][j]= 0,0
        
        for i in range(1,r):
            for j in range(1,c):
                if(matrix[i][0]==0 or matrix[0][j]==0): matrix[i][j]=0
                
        if(row):
            for i in range(c):matrix[0][i]=0
        if(col):
            for i in range(r):matrix[i][0]=0
        