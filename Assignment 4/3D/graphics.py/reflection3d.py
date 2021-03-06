from graphics import *
import math

f=open("file.txt","r")
c=int(f.readline())
vertex1 = []
f=open("file.txt","r")
c=int(f.readline())
vertex1=[]
vertex2=[]
for i in range(c):
	number_string=f.readline().split(' ')
	number_Array=[int(i) for i in number_string]
	point=[]
	point.append(number_Array[0])
	point.append(number_Array[1])
	point.append(number_Array[2])
	vertex1.append(point)
	point=[]
	point.append(number_Array[3])
	point.append(number_Array[4])
	point.append(number_Array[5])
	vertex2.append(point)
	

win_obj=GraphWin("Reflection Window",1000,1000) 
win_obj.setBackground("Yellow")
win_obj.setCoords(-400,-400,600,600)
x_axis=Line(Point(-400,0),Point(600,0)) 
y_axis=Line(Point(0,-400),Point(0,600))
z_axis=Line(Point(400,400),Point(-400,-400))      

x_axis.setOutline("Black")
y_axis.setOutline("Black")
z_axis.setOutline("Black")
x_axis.setArrow('both')
y_axis.setArrow('both')
z_axis.setArrow('both')
x_axis.draw(win_obj)
y_axis.draw(win_obj)
z_axis.draw(win_obj)

info_x=Text(Point(580,-10),"+x axis")
info_x.draw(win_obj)
info_x=Text(Point(-380,-10),"-x axis")
info_x.draw(win_obj)
info_y=Text(Point(-10,580),"+y axis")
info_y.draw(win_obj)
info_y=Text(Point(-10,-380),"-y axis")
info_y.draw(win_obj)
info_ny=Text(Point(-280,-380),"+z axis")
info_ny.draw(win_obj)
info_ny=Text(Point(380,380),"-z axis")
info_ny.draw(win_obj)
origin=Text(Point(-10,-10),"origin")
origin.draw(win_obj)


def drawLine(x0,y0,z0,x1,y1,z1,color):
	ax, ay = x0-(z0*0.3), y0-(z0*0.3)
	bx, by = x1-(z1*0.3), y1-(z1*0.3)
	print(ax,",",ay)
	print(bx,",",by)
	line=Line(Point(ax,ay),Point(bx,by));
	line.setFill(color)
	line.setWidth(3)
	line.draw(win_obj)


def drawSolid(vertex1,vertex2):
	for i in range(c):
		x0 = vertex1[i][0]
		y0 = vertex1[i][1]
		z0 = vertex1[i][2]
		x1 = vertex2[i][0]
		y1 = vertex2[i][1]
		z1 = vertex2[i][2]
		drawLine(x0,y0,z0,x1,y1,z1,"red")

drawSolid(vertex1,vertex2)
##########   Translation ##############
tx=int(input("Enter Tx:"))
ty=int(input("Enter Ty:"))
tz=int(input("Enter Ty:"))
vertex3=[]
vertex4=[]
for i in range(c):
	point=[]
	x0 = vertex1[i][0]+tx
	point.append(x0)
	y0 = vertex1[i][1]+ty
	point.append(y0)
	z0 = vertex1[i][2]+tz
	point.append(z0)
	vertex3.append(point)
	point=[]
	x1 = vertex2[i][0]+tx
	point.append(x1)
	y1 = vertex2[i][1]+ty
	point.append(y1)
	z1 = vertex2[i][2]+tz
	point.append(z1)
	vertex4.append(point)

drawSolid(vertex3,vertex4)

vertex1=vertex3
vertex2=vertex4

###############  Rotation ################################
flag=int(input("Enter 1 for Reflection about XZ plane, 2 for XY-plane ,3 for YZ-plane:"))

## Along XZ-plane  #####

if(flag==1):
	
	vertex3=[]
	vertex4=[]
	for i in range(c):
		point=[]									#For vertex1 of side i
		x0 = vertex1[i][0]
		point.append(x0)
		y0 = -vertex1[i][1]
		point.append(y0)
		z0 = vertex1[i][2]
		point.append(z0)
		vertex3.append(point)
		point=[]										#For vertex2 of side i
		x1 = vertex2[i][0]
		point.append(x1)
		y1 = -vertex2[i][1]
		point.append(y1)
		z1 = vertex2[i][2]
		point.append(z1)
		vertex4.append(point)
	drawSolid(vertex3,vertex4)

## Along XY-plane  #####

if(flag==2):
	vertex3=[]
	vertex4=[]
	for i in range(c):
		point=[]									#For vertex1 of side i
		x0 = vertex1[i][0]
		point.append(x0)
		y0 = vertex1[i][1]
		point.append(y0)
		z0 = -vertex1[i][2]
		point.append(z0)
		vertex3.append(point)
		point=[]										#For vertex2 of side i
		x1 = vertex2[i][0]
		point.append(x1)
		y1 = vertex2[i][1]
		point.append(y1)
		z1 = -vertex2[i][2]
		point.append(z1)
		vertex4.append(point)
	drawSolid(vertex3,vertex4)
## Along YZ-plane   #####

if(flag==3):
	vertex3=[]
	vertex4=[]
	for i in range(c):
		point=[]									#For vertex1 of side i
		x0 =- vertex1[i][0]
		point.append(x0)
		y0 = vertex1[i][1]
		point.append(y0)
		z0 = vertex1[i][2]
		point.append(z0)
		vertex3.append(point)
		point=[]										#For vertex2 of side i
		x1 =  -vertex2[i][0]
		point.append(x1)
		y1 = vertex2[i][1]
		point.append(y1)
		z1 = vertex2[i][2]
		point.append(z1)
		vertex4.append(point)
	drawSolid(vertex3,vertex4)
#########################################################
win_obj.getMouse()
win_obj.close()

