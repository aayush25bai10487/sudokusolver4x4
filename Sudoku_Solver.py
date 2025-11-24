import numpy as np
listans=[1,2,3,4]
rows = int(input("rows: "))
col = int(input("columns: "))
matrix = np.array([],dtype=int) 
print("entries row-wise:")

for i in range(rows):   
    row = []
    for j in range(col):
        row.append(int(input()))
    matrix=np.append(matrix,row)

print("\n2D matrix is:")

matrix=matrix.reshape(rows,col)

for i in range(rows):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()

def zerocounter(board):
    return 0 in board
    
def pos_ans(board,i,j):
    pos=[]
    rowans=set(board[i,:])-{0}
    columnans=set(board[:,j])-{0}
    box_row=(i//2)*2
    box_col=(j//2)*2
    box=board[box_row:box_row+2,box_col:box_col+2]
    for a in listans:
        if a not in box and a not in rowans and a not in columnans:
            pos.append(a)
    return pos

    
def fillbox(board):
    change=False
    for i in range(rows):
        for j in range(col):
            if board[i][j]==0:
                posans=pos_ans(board,i,j)
                if len(posans)==1:
                    board[i][j]=posans[0]
                    change=True
    return change

def fillbox_recursion():
    while fillbox(matrix):
        pass
    if not zerocounter(matrix):
        return True
    for i in range(rows):
        for j in range(col):
            if matrix[i][j]==0:
                for mul_ans in pos_ans(matrix,i,j):
                    matrix[i][j]=mul_ans
                    if fillbox_recursion():
                        return True
                matrix[i][j]=0
                return False
    return True
    

if fillbox_recursion():
    print("\nSOLVED SUDOKO IS:")
    for p in range(4):
        for q in range(4):
            print(matrix[p][q],end=' ')
        print()