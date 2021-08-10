# -*- coding: utf-8 -*-

import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

G = 9.80665 # 重力加速度
rho = 10 # 粒子間密度
pn = 0 #粒子数

class Particle():
    def __init__(self,pos):
        global pn
        self.n = pn
        pn += 1
        self.r = 5 #半径
        self.x = pos[0] #X座標
        self.y = pos[1] #Y座標
        self.a = 0  #角度
        self.dx = 0 #X方向増加量
        self.dy = 0 #Y方向増加量
        self.da = 0 #角度増加量
        self.vx = 0 #X方向速度
        self.vy = 0 #Y方向速度
        self.va = 0 #角速度
        self.fy = 0
        self.fx = 0
        self.fm = 0
    
        self.m = 4.0/3.0*math.pi*rho*self.r**3 # 質量
        self.Ir = math.pi*rho*self.r**4/2.0 #慣性モーメント
        
        self.en = [] #弾性力（直方向）
        self.es = [] #弾性力（せん断方向）

    def config(self):
        self.en = [0 for i in range(pn)]
        self.es = [0 for i in range(pn)]
        
    def nextStep(self,dt):
        #位置更新（オイラー差分）
        ax = self.fx/self.m
        ay = self.fy/self.m
        aa = self.fm/self.Ir
        self.vx += ax*dt
        self.vy += ay*dt
        self.va += aa*dt
        self.dx = self.vx*dt
        self.dy = self.vy*dt
        self.da = self.va*dt
        self.x += self.dx
        self.y += self.dy
        self.a += self.da

class DEM():
    
    def __init__(self):
        
        self.step = 0
        self.dt = 0.01
        
        p1 = Particle([-100,0])
        p1.vy = 30
        p1.vx = 60
        
        p2 = Particle([100,0])
        p2.vy = 30
        p2.vx = -60
        
        p3 = Particle([10,-20])
        p3.vy = 30
        p3.vx = -20
        
        p4 = Particle([-80,60])
        p4.vx = 20
        p4.vy = 5
        
        self.pe = []
        self.pe.append(p1)
        self.pe.append(p2)
        self.pe.append(p3)
        self.pe.append(p4)
        
        for p in self.pe:
            p.config()
 
    def calcForce(self):
        #2粒子間の力
        combs = [(p1, p2) for p1 in self.pe for p2 in self.pe]
        for p1,p2 in combs:
            if p1.n == p2.n:
                continue
            
            #接触判定
            lx = p1.x - p2.x
            ly = p1.y - p2.y
            ld = math.sqrt(lx**2+ly**2)
            if (p1.r+p2.r)>ld:
                #接触
                cos_a = lx/ld
                sin_a = ly/ld
                self.force2par(p1,p2,cos_a,sin_a)
            else:
                #接触しない
                p1.en[p2.n] = 0.0
                p1.es[p2.n] = 0.0
        #外力
        for p in self.pe:
            p.fy += -G * p.m #重力
    
    def force2par(self,p1,p2,cos_a,sin_a):
        kn = 10**7 #弾性係数（法線方向）
        etan = 1000 #粘性係数（法線方向）
        ks = 5000 #弾性係数（せん断方向）
        etas = 1000 #粘性係数（せん断方向）
        frc = 10 #摩擦係数
        
        #相対的変位増分
        un = +(p1.dx-p2.dx)*cos_a+(p1.dy-p2.dy)*sin_a
        us = -(p1.dx-p2.dx)*sin_a+(p1.dy-p2.dy)*cos_a+(p1.r*p1.da+p2.r*p2.da)
        #相対的速度増分
        vn = +(p1.vx-p2.vx)*cos_a+(p1.vy-p2.vy)*sin_a
        vs = -(p1.vx-p2.vx)*sin_a+(p1.vy-p2.vy)*cos_a+(p1.r*p1.va+p2.r*p2.va)
        #合力
        p1.en[p2.n] += kn*un
        p1.es[p2.n] += ks*us
        hn = p1.en[p2.n] + etan*vn
        hs = p1.es[p2.n] + etas*vs
        
        if hn <= 0.0:
            #法線力がなければ、せん断力は０
            hs = 0.0
        elif abs(hs)-frc*hn >= 0.0:
            #摩擦力以上のせん断力は働かない
            hs = frc*abs(hn)*hs/abs(hs)     
        #合力
        p1.fx += -hn*cos_a + hs*sin_a
        p1.fy += -hn*sin_a - hs*cos_a
        p1.fm -=  p1.r*hs
    
    def clacStep(self):
        for p in self.pe:
            p.fx = 0
            p.fy = 0
            p.fm = 0
            # print(p.y)
            
        self.calcForce()
        
        for p in self.pe:
            p.nextStep(self.dt)
            
        self.step += 1

def main():
    dem = DEM()

    fig, ax = plt.subplots(1, 1)
    ax.set_aspect('equal')
    ax.set_xlim((-50,50))
    ax.set_ylim((-50,50))
    ax.grid(True)

    for _ in range(10000):
        dem.clacStep()
        particle = [0 for _ in range(len(dem.pe))]
        for i in range(len(dem.pe)):
            # Draw a solid blue circle in the center
            c = patches.Circle(xy=(dem.pe[i].x, dem.pe[i].y), radius=dem.pe[i].r, fc='g', ec='g', fill=True)
            particle[i] = ax.add_patch(c)
        plt.pause(0.01)

        for i in range(len(dem.pe)):
            particle[i].remove()

if __name__ == '__main__':
    main()
