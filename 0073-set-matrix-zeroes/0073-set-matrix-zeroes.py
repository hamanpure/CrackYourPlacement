class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def find_zeros(matrix):
            l = []
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 0:
                        l.append([i,j])
            return l
        def make_zeros(l,matrix):
            r = l[0]
            c = l[1]
            r_length = len(matrix)
            c_length = len(matrix[0])
            for i in range(r_length):
                matrix[i][c] = 0
            for j in range(c_length):
                matrix[r][j] = 0
        zeros_index_array = find_zeros(matrix)
        for i in zeros_index_array:
            make_zeros(i,matrix)


                

        