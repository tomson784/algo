# https://www.youtube.com/watch?v=X1AsMlJdiok&t=215s

import numpy as np
from pprint import pprint

l = {
    "S":0,
    "A":np.inf,
    "B":np.inf,
    "C":np.inf,
    "D":np.inf,
    "E":np.inf,
    "F":np.inf,
    "G":np.inf
}

# 確定したルート
l_ = {}

edge = {
    "S":{"A":5, "B":4, "C":1},
    "A":{"S":5, "D":2},
    "B":{"S":4, "D":5, "E":6},
    "C":{"S":1, "B":2},
    "D":{"A":2, "B":5, "F":1, "G":3},
    "E":{"B":6, "G":2},
    "F":{"D":1, "G":3},
    "G":{"D":3, "E":2, "F":4}
}

while True:
    # 未確定ノードの中からルートが最小のノードの選択
    if len(l) == 1:
        min_edge = list(l.keys())[0]
    else:
        min_edge = min(l, key=l.get)

    # 確定したノードへのルートの削除
    del_list = []
    for i in edge:
        for j in edge[i]:
            if j == min_edge:
                del_list.append(i+j)
    for i in del_list:
        del edge[i[0]][i[1]]
    for i,j in edge[min_edge].items():
        if (j + l[min_edge]) < l[i]:
            l[i] = j + l[min_edge]
    # 確定したノードへのルートの削除
    l_[min_edge] = l[min_edge]
    if len(edge) == 1:
        break
    node_min_route = min(edge[min_edge], key=edge[min_edge].get)
    del edge[min_edge]
    del l[min_edge]
    print(l)
    print(l_)
    print("-"*50)
print(l_)
