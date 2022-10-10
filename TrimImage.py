image = []
minx, miny, maxx, maxy = 0, 0, 0, 0
while (buff := input().split()):
    if buff[2] == '0' or buff[3] == '0':
        continue

    image.append((
        list(map(int, buff[:-1])), 
        buff[-1]
    ))
    minx = min(minx, image[-1][0][0] + image[-1][0][2], image[-1][0][0])
    maxx = max(maxx, image[-1][0][0] + image[-1][0][2], image[-1][0][0])

    miny = min(miny, image[-1][0][1] + image[-1][0][3], image[-1][0][1])
    maxy = max(maxy, image[-1][0][1] + image[-1][0][3], image[-1][0][1])

for i in range(len(image)):
    image[i][0][0] -= minx
    image[i][0][1] -= miny

    if image[i][0][2] < 0:
        image[i][0][0] += image[i][0][2]
        image[i][0][2] = abs(image[i][0][2])

    if image[i][0][3] < 0:
        image[i][0][1] += image[i][0][3]
        image[i][0][3] = abs(image[i][0][3])


image_field = [['.' for _ in range(maxx - minx)] for _ in range(maxy - miny)]

for rect in image:
    for i in range(rect[0][2]):
        for j in range(rect[0][3]):
            image_field[j + rect[0][1]][i + rect[0][0]] = rect[-1]

minx = min(x[0][0] for x in image)
miny = min(y[0][1] for y in image)
maxx = max(x[0][0] + x[0][2] for x in image)
maxy = max(y[0][1] + y[0][3] for y in image)

for i in range(miny, maxy):
    for j in range(minx, maxx):
        print(image_field[i][j], end='')
    print()
