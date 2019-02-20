import editdistance, os, numpy

# obtain directory from user
dir = input("Directory: ")

data = []

for root, dirs, files in os.walk(dir):
    print(files)
    for i in files:
        with open(dir + "/" + i) as file:
            data.append(file.read()) # populate data list with the mapped RNA of each species

n = len(data)

matrix = [[0] * n for i in range(n)]

for y in range(0, n):
    for x in range(y,n):
        if x != y:
            dist = editdistance.eval(data[x], data[y])
            matrix[y][x] = dist
            matrix[x][y] = dist
        else:
            matrix[x][y] = 0.0

print(matrix)
