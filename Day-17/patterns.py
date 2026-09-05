'''
n = int(input())
m = n // 2

for i in range(n):
    for j in range(n):
        if (j==0 and i<=m) or (j==n-1 and i<=m) or (i-j == m and i>=m) or (i+j==m+n-1 and i>=m) :
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''


