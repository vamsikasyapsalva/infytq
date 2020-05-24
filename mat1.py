r = int(input())
mat = []
res = []
for i in range(r):
    mat.append(list(map(int,input().split()))) 
c = r+1   
for i in range(r):
    for j in range(c-2):
        if mat[i][j] == mat[i][j+1] == mat[i][j+2]:
            res.append(mat[i][j])
for i in range(r-2):
    for j in range(c):
        if mat[i+1][j] == mat[i+1][j] == mat[i+2][j]:
            res.append(mat[i][j])
for i in range(r-2):
    for j in range(c-2):
        if mat[i][j] == mat[i+1][j+1] == mat[i+2][j+2]:
            res.append(mat[i][j])
print(min(res))   
