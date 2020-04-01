# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import math

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

    # 第1, 2の関節角度
    # th = np.radians([90, 90])

    th = np.radians([np.random.randint(-180,180), np.random.randint(-180,180)])
    print("th1 : {}  | th2 : {}".format(th[0],th[1])) 

    # 順運動学の計算
    p = fk(L, th)

    # グラフ描画位置の設定
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    # plt.subplots_adjust(left=0.1, bottom=0.15)
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    # グラフ描画
    ax.grid()
    ax.plot(p.T[0], p.T[1], "-o", lw=5)
    ax.plot(p.T[0,0], p.T[1,0], marker='.', markersize=20)
    ax.plot(p.T[0,1], p.T[1,1], marker='.', markersize=20)
    ax.plot(p.T[0,2], p.T[1,2], marker='.', markersize=20)
    plt.show()


if __name__ == '__main__':
    main()