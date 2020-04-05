import matplotlib.pyplot as plt 

def motion(event):  
    x = event.xdata
    y = event.ydata

    ln.set_data([0,1,x], [0,0,y])
    ln1.set_data(0, 0)
    ln2.set_data(1, 0)
    ln3.set_data(x, y)
    plt.draw()

plt.figure()
ln, = plt.plot([],[],'-')
ln1, = plt.plot([],[],marker='o')
ln2, = plt.plot([],[],marker='o')
ln3, = plt.plot([],[],marker='o')

plt.connect('motion_notify_event', motion)
plt.show()