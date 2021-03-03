# coding:utf-8
from turtle import *
from turtledemo.clock import setup

import matplotlib.pyplot as plt
import numpy as np

print('\n'.join([''.join([('loveNana'[(x - y) % 8] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (
        y * 0.1) ** 3 <= 0 else ' ')
                          for x in range(-30, 30)])
                 for y in range(15, -15, -1)]))
print('end')

x = np.linspace(-8, 8, 1024)
y1 = 0.618 * np.abs(x) - 0.8 * np.sqrt(64 - x ** 2)  # 左部分
y2 = 0.618 * np.abs(x) + 0.8 * np.sqrt(64 - x ** 2)  # 右部分
plt.plot(x, y1, color='r')
plt.plot(x, y2, color='r')
plt.show()
print('end')

# 初始设置
setup(750, 500)
penup()
pensize(25)
pencolor("pink")
fd(-230)
seth(90)
pendown()

# 绘制桃心
circle(-50, 180)
circle(50, -180)
circle(75, -50)
circle(-190, -45)
penup()
fd(185)
seth(180)
fd(120)
seth(90)
pendown()
circle(-75, -50)
circle(190, -45)
penup()
fd(184)
seth(0)
fd(80)
seth(90)
pendown()
circle(-50, 180)
circle(50, -180)
circle(75, -50)
circle(-190, -45)
penup()
fd(185)
seth(180)
fd(120)
seth(90)
pendown()
circle(-75, -50)
circle(190, -45)
penup()
fd(150)
seth(180)
fd(300)

# 绘制箭头
pencolor("red")
pensize(10)
pendown()
fd(-500)
seth(90)
fd(30)
fd(-60)
seth(30)
fd(60)
seth(150)
fd(60)
done()
print('end')


# 绘制3D桃心
def heart_3d(x, y, z):
    return (x ** 2 + (9 / 4) * y ** 2 + z ** 2 - 1) ** 3 - x ** 2 * z ** 3 - (9 / 80) * y ** 2 * z ** 3


# 图像展示
def plot_implicit(fn, bbox=(-1.5, 1.5)):
    xmin, xmax, ymin, ymax, zmin, zmax = bbox * 3
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    A = np.linspace(xmin, xmax, 100)  # resolution of the contour
    B = np.linspace(xmin, xmax, 40)  # number of slices
    A1, A2 = np.meshgrid(A, A)  # grid on which the contour is plotted

    # plot contours in the XY plane
    for z in B:
        X, Y = A1, A2
        Z = fn(X, Y, z)
        cset = ax.contour(X, Y, Z + z, [z], zdir='z', colors=('r',))
        # [z] defines the only level to plot
        # for this contour for this value of z

    # plot contours in the XZ plane
    for y in B:
        X, Z = A1, A2
        Y = fn(X, y, Z)
        cset = ax.contour(X, Y + y, Z, [y], zdir='y', colors=('red',))

    # plot contours in the YZ plane
    for x in B:
        Y, Z = A1, A2
        X = fn(x, Y, Z)
        cset = ax.contour(X + x, Y, Z, [x], zdir='x', colors=('red',))

    # 轴
    ax.set_zlim3d(zmin, zmax)
    ax.set_xlim3d(xmin, xmax)
    ax.set_ylim3d(ymin, ymax)

    # 显示图像
    plt.show()


# 主函数
if __name__ == '__main__':
    plot_implicit(heart_3d)
