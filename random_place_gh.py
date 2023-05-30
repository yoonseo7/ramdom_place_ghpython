import random
import rhinoscriptsyntax as rs

wid = 108
hig = 47
dip = 80

# 1. 배열과 직육면체 초기화
grid = [[[0]*dip for _ in range(hig)] for _ in range(wid)]

for x in range(len(grid)):
    for y in range(len(grid[x])):
        grid[x][y] = [grid[x][y]]*dip
        

cubes = {1:[6, 6, 5, 1000, 0], 2:[6, 6, 10, 1000, 0],
         3:[8, 12, 5, 1000, 0], 4:[9, 11, 5, 1000, 0], 5:[10, 9, 5, 1000, 0],
         6:[7, 7, 10, 1000, 0], 7:[9, 7, 10, 1000, 0], 8:[9, 8, 10, 1000, 0],
         9:[12, 11, 5, 1000, 0], 10:[13, 13, 5, 1000, 0], 11:[13, 12, 5, 1000, 0],
        12:[9, 12, 10, 1000, 0], 13:[9, 9, 10, 1000, 0], 14:[8, 12, 10, 1000, 0],
         }
cube_centers = {key: [] for key in cubes.keys()}  # 직육면체의 중앙 좌표를 저장하는 사전


# 3. & 4. 배열에 직육면체 배치
x, y, z = 0, 0, 0
while z < dip:
    while y < hig:
        while x < wid:
            # 가능한 직육면체 탐색
            possible_cubes = []
            for key, (w, h, d, allocated, placed) in cubes.items():
                if placed < allocated and x + w <= wid and y + h <= hig and z + d <= dip:
                    # 추가된 부분: 해당 영역이 모두 0인지 확인
                    c = 1
                    for x1 in range(x, x+w):
                        for y1 in range(y, y+h):
                            for z1 in range(z, z+d):
                                if grid[x1][y1][z1]:
                                    c = 0
                                    break
                            if c == 0:
                                break
                    if c:
                        possible_cubes.append(key)
            if not possible_cubes:  # 가능한 직육면체가 없으면 다음 위치로 이동
                x += 1
                continue

            # 가능한 직육면체 중 하나 선택
            cube_key = random.choice(possible_cubes)
            w, h, d, _, _ = cubes[cube_key]

            # 선택한 직육면체를 배열에 배치
            for i in range(x, x+w):
                for j in range(y, y+h):
                    for k in range(z, z+d):
                        grid[i][j][k] = cube_key
            
            cubes[cube_key][4] += 1  # 배치 갯수 증가

            # 직육면체의 중앙 좌표를 저장
            center_x, center_y, center_z = x + w//2, y + h//2, z + d//2
            cube_centers[cube_key].append(rs.CreatePoint(center_x, center_y, center_z))

            # 현재 위치 갱신
            x += w
        x = 0
        y += 1
    z += 1
    x = 0
    y = 0

# 5. 결과 출력
#print(grid)
print(cubes)



p1 = cube_centers[1]
p2 = cube_centers[2]
p3 = cube_centers[3]
p4 = cube_centers[4]
p5 = cube_centers[5]
p6 = cube_centers[6]
p7 = cube_centers[7]
p8 = cube_centers[8]
p9 = cube_centers[9]
p10 = cube_centers[10]
p11 = cube_centers[11]
p12 = cube_centers[12]
p13 = cube_centers[13]
p14 = cube_centers[14]
