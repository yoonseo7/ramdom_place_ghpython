# 직사각형이 아닌 형태의 사이트를 배열화하기 위한 코드입니다

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from scipy.spatial import ConvexHull

hig = 89
wid = 30

# 지정된 점들
# points = np.array([[0, 0], [0, 9], [55, 0], [48, 9]])
points = np.array([[84, 14], [88, 4], [0, 0], [0, 29]])

# ConvexHull로 주어진 점들의 볼록 껍질을 찾는다
hull = ConvexHull(points)

# 볼록 껍질의 경계를 만든다
hull_path = Path(points[hull.vertices])

# 108*47 크기의 2차원 리스트를 생성한다
arr = [[0]*wid for _ in range(hig)]

# 리스트를 순회하며 각 요소가 볼록 껍질 내부에 있는지 판별한다
for i in range(hig):
    for j in range(wid):
        if hull_path.contains_point((i, j)):
            arr[i][j] = 0
        else:
            arr[i][j] = -1

for i in arr:
    print(i, end=', ')


# ndarray로 변환하여 시각화
plt.imshow(np.array(arr), cmap='gray')
plt.show()
