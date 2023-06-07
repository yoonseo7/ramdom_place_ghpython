import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# 1. 배열과 직육면체 초기화
grid = np.zeros((47, 40, 16))  # 100x80x20 크기의 3차원 배열 초기화
cubes = {1:[6, 6, 1, 1000, 0], 2:[6, 6, 2, 1000, 0],
         3:[8, 12, 1, 1000, 0], 4:[9, 11, 1, 1000, 0], 5:[10, 9, 1, 1000, 0],
         6:[7, 7, 2, 1000, 0], 7:[9, 7, 2, 1000, 0], 8:[9, 8, 2, 1000, 0],
         9:[12, 11, 1, 1000, 0], 10:[13, 13, 1, 1000, 0], 11:[13, 12, 1, 1000, 0],
        12:[9, 12, 2, 1000, 0], 13:[9, 9, 2, 1000, 0], 14:[8, 12, 2, 1000, 0],
         }

'''# 2. 각 직육면체의 할당된 갯수 랜덤 결정
total_vol = grid.size
cube_vol = {key: value[0]*value[1]*value[2] for key, value in cubes.items()}
cube_keys = list(cubes.keys())
random.shuffle(cube_keys)  # 직육면체 순서 랜덤화

for key in cube_keys:
    max_num = total_vol // cube_vol[key]  # 최대 할당 가능 갯수
    num = random.randint(0, max_num)  # 랜덤 갯수 결정
    cubes[key][3] = num  # 할당 갯수 저장
    total_vol -= num * cube_vol[key]  # 전체 볼륨 갱신
'''

# 3. & 4. 배열에 직육면체 배치
x, y, z = 0, 0, 0
while z < grid.shape[2]:
    while y < grid.shape[1]:
        while x < grid.shape[0]:
            # 가능한 직육면체 탐색
            possible_cubes = []
            for key, (w, h, d, allocated, placed) in cubes.items():
                if placed < allocated and x + w <= grid.shape[0] and y + h <= grid.shape[1] and z + d <= grid.shape[2]:
                    # 추가된 부분: 해당 영역이 모두 0인지 확인
                    if np.all(grid[x:x+w, y:y+h, z:z+d] == 0):
                        possible_cubes.append(key)
            if not possible_cubes:  # 가능한 직육면체가 없으면 다음 위치로 이동
                x += 1
                continue

            # 가능한 직육면체 중 하나 선택
            cube_key = random.choice(possible_cubes)
            w, h, d, _, _ = cubes[cube_key]

            # 선택한 직육면체를 배열에 배치
            grid[x:x+w, y:y+h, z:z+d] = cube_key
            cubes[cube_key][4] += 1  # 배치 갯수 증가

            # 현재 위치 갱신
            x += w
        x = 0
        y += 1
    z += 1
    x = 0
    y = 0

# 5. 결과 출력
print(grid)
print(cubes)

# 6. Grid 시각화
# 커스텀 colormap 생성 (0: white, 1: red, 2: yellow, 3: green, 4: blue, 5: purple)
cmap = ListedColormap(['white', 'red', 'yellow', 'green', 'blue', 'purple'])
# 각 z-평면 순차적으로 표시
for z in range(grid.shape[2]):
    plt.imshow(grid[:, :, z], cmap=cmap)
    plt.title(f"z = {z}")
    plt.show()
