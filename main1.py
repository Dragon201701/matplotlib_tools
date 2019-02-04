import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import xlrd
from _overlapped import NULL

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']
colorindex = 0

def toint(f):
    trunc = int(f)
    diff = f - trunc

    # trunc is one too low
    if abs(f - trunc - 1) < 0.00001:
        return trunc + 1
    # trunc is one too high
    if abs(f - trunc + 1) < 0.00001:
        return trunc - 1
    # trunc is the right value
    return trunc

def getcolor():
    global colorindex
    colorlist = ['orange', 'yellow', 'blue', 'brown', 'green']
    color = colorlist[colorindex]
    if(colorindex == len(colorlist)-1):
        colorindex = 0
    else:
        colorindex+=1
    return color
def plot_opaque_cube_old(x=10, y=20, z=30, dx=40, dy=50, dz=60):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')


    xx = np.linspace(x, x+dx, 2)
    yy = np.linspace(y, y+dy, 2)
    zz = np.linspace(z, z+dz, 2)

    xx, yy = np.meshgrid(xx, yy)

    ax.plot_surface(xx, yy, z)
    ax.plot_surface(xx, yy, z+dz)

    yy, zz = np.meshgrid(yy, zz)
    ax.plot_surface(x, yy, zz)
    ax.plot_surface(x+dx, yy, zz)

    xx, zz = np.meshgrid(xx, zz)
    ax.plot_surface(xx, y, zz)
    ax.plot_surface(xx, y+dy, zz)
    # ax.set_xlim3d(-dx, dx*2, 20)
    # ax.set_xlim3d(-dx, dx*2, 20)
    # ax.set_xlim3d(-dx, dx*2, 20)
    plt.title("Cube")
    plt.show()
def plot_opaque_cube(x=10, y=20, z=30, dx=40, dy=50, dz=60):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')


    xx = np.linspace(x, x+dx, 2)
    yy = np.linspace(y, y+dy, 2)
    zz = np.linspace(z, z+dz, 2)
    print(xx)
    print(yy)
    print(zz)
    xx, yy = np.meshgrid(xx, yy)
    print(xx)
    print(yy)
    ax.plot_surface(xx, yy, zz)
    #figure surf(xx,yy,zz)
    #ax.plot_surface(xx, yy, z)
    #ax.plot_surface(xx, yy, z+dz)

    #yy, zz = np.meshgrid(yy, zz)
    #ax.plot_surface(x, yy, zz)
    #ax.plot_surface(x+dx, yy, zz)

    #xx, zz = np.meshgrid(xx, zz)
    #ax.plot_surface(xx, y, zz)
    #ax.plot_surface(xx, y+dy, zz)
    # ax.set_xlim3d(-dx, dx*2, 20)
    # ax.set_xlim3d(-dx, dx*2, 20)
    # ax.set_xlim3d(-dx, dx*2, 20)
    plt.title("Cube")
    plt.show()
def plot_linear_cube2(x, y, z, dx, dy, dz, color='red'):
    #fig = plt.figure()
    #ax = Axes3D(fig)
    xx = [x, x, x+dx, x+dx, x]
    yy = [y, y+dy, y+dy, y, y]
    kwargs = {'alpha': 1, 'color': color}
    #print('plot_linear_cube with color:', color, 'start point: ',x,' ',y,' ',z, 'size: ',dx,'',dy,'',dz)
    ax.plot3D(xx, yy, [z]*5, **kwargs)
    ax.plot3D(xx, yy, [z+dz]*5, **kwargs)
    ax.plot3D([x, x], [y, y], [z, z+dz], **kwargs)
    ax.plot3D([x, x], [y+dy, y+dy], [z, z+dz], **kwargs)
    ax.plot3D([x+dx, x+dx], [y+dy, y+dy], [z, z+dz], **kwargs)
    ax.plot3D([x+dx, x+dx], [y, y], [z, z+dz], **kwargs)
    #plt.title('Cube')
    #plt.show()
def plot_linear_cube(x, y, z, dx, dy, dz):
    #fig = plt.figure()
    #ax = Axes3D(fig)
    xx = [x, x, x+dx, x+dx, x]
    yy = [y, y+dy, y+dy, y, y]
    color = getcolor()
    kwargs = {'alpha': 1, 'color': color}
    #print('plot_linear_cube with color:', color, 'start point: ',x,' ',y,' ',z, 'size: ',dx,'',dy,'',dz)
    ax.plot3D(xx, yy, [z]*5, **kwargs)
    ax.plot3D(xx, yy, [z+dz]*5, **kwargs)
    ax.plot3D([x, x], [y, y], [z, z+dz], **kwargs)
    ax.plot3D([x, x], [y+dy, y+dy], [z, z+dz], **kwargs)
    ax.plot3D([x+dx, x+dx], [y+dy, y+dy], [z, z+dz], **kwargs)
    ax.plot3D([x+dx, x+dx], [y, y], [z, z+dz], **kwargs)
    #plt.title('Cube')
    #plt.show()

def plot_box(x, y, z, size, alignmatrix):
    # align is a 3*3 list with binary value. 
    # size is a list [length, width, height]
    outline = [0,0,0] # dx, dy, dz
    #print(alignmatrix, "\n")
    print('plotbox size:', size, 'alignment: ', alignmatrix)
    for i in range(0, 3):
        align = alignmatrix[i]
        #print(align, "\n")
        for j in range(0,3):
            #print("align[j]: ",align[j], "int(): ", int(align[j]))
            if(round(align[j]) == 1):
                outline[j] = round(size[i])
    #print(outline)
    color = getcolor()
    plot_linear_cube2(x, y, z, outline[0], outline[1], outline[2], color)
        
if __name__ == '__main__':
    #plot_opaque_cube(x=10, y=20, z=30, dx=40, dy=50, dz=60)
    plot_opaque_cube(x=10, y=20, z=30, dx=40, dy=50, dz=60)
    fig = plt.figure()
    ax = Axes3D(fig)
    #plot_linear_cube(0, 0, 0, 100, 80, 60)
    workbook = xlrd.open_workbook('test_data4.xls')
    sheet1 = workbook.sheet_by_index(0)
    numrows = sheet1.nrows
    size = [0,0,0]
    alignment = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(0, numrows):
        data = sheet1.row_values(i)
        if(data[15] == 0): continue
        if(data == NULL | len(data)!=16): continue
        # print(data[3:6])
        if(data[0] == 'Container'): 
            container = sheet1.row_values(i+1)
            plot_linear_cube2(0, 0, 0, container[0], container[1], container[2], 'red')
            break
        else:
            x = round(data[0])
            y = round(data[1])
            z = round(data[2])
            plot_box(x,y,z,data[3:6],[data[6:9], data[9:12], data[12:15]])
            
    plot_linear_cube2(0, 0, 0, 24, 20, 20, 'red')
    plt.xlim((0,25))
    plt.ylim((0,25))
    plt.axis('equal')
    #plt.title('Cube')
    plt.axis('scaled')
    plt.yticks(np.arange(0, 25, 5))
    plt.xticks(np.arange(0, 25, 5))
    plt.axis('square')
    plt.show()
    pass