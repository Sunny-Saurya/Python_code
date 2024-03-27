a = [[1,2,3],[2,4,5],[3,5,6]]
a = True
for i in range(0,3):
  for j in range(0,3):
    if a[i][j]!=a[j][i]:
      a = False
print (a)

# print("hello world")