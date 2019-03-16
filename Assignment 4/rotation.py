from graphics import *
import math


coordinate = []
def translation(tx1,ty1):
	print(coordinate)
	for i in range(c):
		coordinate[i][0]=(int)(coordinate[i][0]+tx1)
		coordinate[i][1]=(int)(coordinate[i][1]+ty1)
		
	print(coordinate)
	print()
def rotation(theta):
	for i in range(c):
		x0 =coordinate[i][0]
		y0=coordinate[i][1]
		coordinate[i][0]=(int)(x0*math.cos(math.radians(theta))-y0*math.sin(math.radians(theta)))
		coordinate[i][1]=(int)(x0*math.sin(math.radians(theta))+y0*math.cos(math.radians(theta)))
	
	print(coordinate)
	print()

print("Enter the number of vertices of polygon")
c=int(input())

for i in range(c):
    x = int(input("Enter x coordinate of vertex:"))
    y = int(input("Enter y coordinate of vertex:"))
    point=[]
    point.append(x)
    point.append(y)
    coordinate.append(point)


theta= float(input("Enter angle of rotation :theta="))

print("Enter pivot point coordinates")
a = int(input("Enter x coordinate of pivot:"))
b = int(input("Enter y coordinate of pivot:"))

win_obj=GraphWin("Rotation",700,700) #set viewport size  700,700 are device coordinates
win_obj.setBackground("Light Green")
win_obj.setCoords(-350,-350,350,350) #set window  use coordinates are set
x_axis=Line(Point(-350,0),Point(350,0))   #obj for x axis 
y_axis=Line(Point(0,-350),Point(0,350))    #obj for y axis 

x_axis.setOutline("Black")
y_axis.setOutline("Black")
x_axis.setArrow('both')
y_axis.setArrow('both')
x_axis.draw(win_obj)
y_axis.draw(win_obj)

info_x=Text(Point(320,-10),"+x axis")
info_x.draw(win_obj)
info_nx=Text(Point(-320,-10),"-x axis")
info_nx.draw(win_obj)
info_y=Text(Point(0,330),"+y axis")
info_y.draw(win_obj)
info_ny=Text(Point(0,-330),"-y axis")
info_ny.draw(win_obj)

origin=Text(Point(-10,-10),"origin")
origin.draw(win_obj)


#previous
for i in range(c-1):
    x0 = coordinate[i][0]
    y0 = coordinate[i][1]
    x1 = coordinate[i+1][0]
    y1 = coordinate[i+1][1]
    #Point(x0,y0).draw(win_obj)
    display = Text(Point(x0,y0),"("+str(x0)+","+str(y0)+")")
    display.draw(win_obj)
    line=Line(Point(x0,y0),Point(x1,y1))
    line.setOutline("blue")
    line.draw(win_obj)
x0 = coordinate[0][0]
y0 = coordinate[0][1]
x1 = coordinate[c-1][0]
y1 = coordinate[c-1][1]
#Point(x0,y0).draw(win_obj)
display = Text(Point(x1,y1),"("+str(x1)+","+str(y1)+")")
display.draw(win_obj)
line=Line(Point(x0,y0),Point(x1,y1))
line.setOutline("blue")
line.draw(win_obj)



translation(-1*a,-1*b)
rotation(theta)
translation(a,b)

#after rotation
for i in range(c-1):
    x0 = coordinate[i][0]
    y0 = coordinate[i][1]
    x1 = coordinate[i+1][0]
    y1 = coordinate[i+1][1]
    #Point(x0,y0).draw(win_obj)
    display = Text(Point(x0,y0),"("+str(x0)+","+str(y0)+")")
    display.draw(win_obj)
    line=Line(Point(x0,y0),Point(x1,y1))
    line.setOutline("red")
    line.draw(win_obj)
x0 = coordinate[0][0]
y0 = coordinate[0][1]
x1 = coordinate[c-1][0]
y1 = coordinate[c-1][1]
#Point(x0,y0).draw(win_obj)
display = Text(Point(x1,y1),"("+str(x1)+","+str(y1)+")")
display.draw(win_obj)
line=Line(Point(x0,y0),Point(x1,y1))
line.setOutline("red")
line.draw(win_obj)

win_obj.getMouse()
win_obj.close()
