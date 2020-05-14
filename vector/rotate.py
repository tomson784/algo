import numpy as np
import matplotlib.pyplot as plt

################################
# 
#  (x1,y1)                 (x4,y4)
#     -------------------------
#     |                       |
#     |                       |
#     |                       |
#     |                       |
#     |                       |
#     |                       |
#     -------------------------
#  (x2,y2)                 (x3,y3)

# [x1,x2,x3,x4][y1,y2,y3,y4]
rect = [[0,0,1,1],[1,0,0,1]]

# plt.axes().set_aspect('equal')
# plt.xlim([-3,3])
# plt.ylim([-3,3])

# plt.plot(rect[0],rect[1],"-")
# plt.plot([rect[0][3],rect[0][0]],[rect[1][3],rect[1][0]],"-")
# plt.show()

def rotate(x,y,th):
    x_a = x*np.cos(th) - y*np.sin(th)
    y_a = x*np.sin(th) + y*np.cos(th)
    return x_a, y_a 

th = np.radians(30)

x1, y1 = rotate(rect[0][0], rect[1][0], th)
x2, y2 = rotate(rect[0][1], rect[1][1], th)
x3, y3 = rotate(rect[0][2], rect[1][2], th)
x4, y4 = rotate(rect[0][3], rect[1][3], th)

plt.axes().set_aspect('equal')
plt.xlim([-3,3])
plt.ylim([-3,3])

plt.plot(rect[0],rect[1],"-", color='black')
plt.plot([rect[0][3],rect[0][0]],[rect[1][3],rect[1][0]],"-", color='black')

plt.plot([x1,x2],[y1,y2],"-", color='red')
plt.plot([x2,x3],[y2,y3],"-", color='red')
plt.plot([x3,x4],[y3,y4],"-", color='red')
plt.plot([x4,x1],[y4,y1],"-", color='red')
plt.show()
