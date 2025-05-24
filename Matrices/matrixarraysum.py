def finalsum(matrix,array):
    for i in range(len(matrix)):
        s=0
        for j in range(len(matrix[0])):
            if matrix[i][j]:
                s+=array[j]
        print(s)

arr=[7,6,5,2,1]
matrix=[[1,0,0,1,1],[1,0,0,0,1],[0,0,0,1,0],[1,0,0,0,0],[1,0,0,0,1]]
finalsum(matrix,arr)