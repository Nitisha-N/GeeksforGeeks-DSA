    #Multyply 2 matrices su-dsa-topic-wise-week2/problem/multiply-2-matrices4144

class Solution:
    def multiply(self, mat1, mat2):
        n = len(mat1)

        result = [[0]*n for _ in range(n)]  # for _ in range is used to show that the input variable name does not matter. I.e, it will accept everything, not just "i in range" or "j in range".

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result[i][j]+= mat1[i][k] * mat2[k][j]
        return result
