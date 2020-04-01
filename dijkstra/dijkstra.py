import numpy as np

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
    min_edge = min(l, key=l.get)

    del_list = []
    for i in edge:
        for j in edge[i]:
            if j == min_edge:
                del_list.append(i+j)
    print(del_list)