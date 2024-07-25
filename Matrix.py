'''
matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix)

print(len(matrix))

print(len(matrix[0]))

print((matrix[1][2]))

print()

for r in range (3):
    for c in range (3):
        print(matrix[r][c], end="")

print()
'''

'''
n = int(input("Enter the dimensions of the matrix - "))
for i in range (n):
    temp = []
    for j in range(n):
        x = int(input("Enter your element - "))
        temp.append(x)
    matrix.append(temp)

for i in range (n):
    print(matrix[i][i])
'''

matrixA = [[1,2],[3,4]]
matrixB = [[5,6],[7,8]]
addResult = [[0],[0]]
minusResult = [[0],[0]]
for i in range(0,2):
    for j in range(0,2):
        addResult[[i],[j]] = matrixA[[i],[j]] + matrixB[[i],[j]]
        minusResult[[i],[j]] = matrixA[[i],[j]] + matrixB[[i],[j]]
for i in range(2):
    for j in range(2):
        print(addResult[i],[j], end="")
    print("\n")

for i in range(2):
    for j in range(2):
        print(minusResult[i],[j], end="")
    print("\n")