# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import math

# 逆運動学の計算
def ik(L, p2):
    x, y = p2
    l1, l2 = L
    l3 = math.sqrt((x*x) + (y*y))
    th2 = math.pi - math.acos(((l1*l1) + (l2*l2) - ( l3 * l3)) / (2*l1*l2))
    th1 = math.atan2(y , x) - math.acos(((l1*l1) + (l3 * l3) - (l2*l2)) / (2*l1*l3))
    return [th1, th2]

# 順運動学の計算
def fk(L, th):
    # 各リンクの長さと関節角度の取得
    l1, l2 = L
    th1, th2 = th

    # リンク1の手先
    x1 = l1 * math.cos(th1)
    y1 = l1 * math.sin(th1)

    # リンク2の手先
    x2 = x1 + l2 * math.cos(th1 + th2)
    y2 = y1 + l2 * math.sin(th1 + th2)

    # 手先位置をNumPy配列に格納して返す
    return np.array([[0, 0], [x1, y1], [x2, y2]])


def main():
    # リンク1, 2の長さ
    L = [0.5, 0.5]
    p2 = [0.5, 0.5]
    # 第1, 2の関節角度
    #th = np.radians([90, 0])

    # 順運動学の計算
    th = ik(L, p2)
    p = fk(L, th)

if __name__ == '__main__':
    main()