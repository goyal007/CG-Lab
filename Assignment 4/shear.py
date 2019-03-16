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
		coordinate[i][0]=(int)(x0*math.cos(theta)-y0*math.sin(theta))
		coordinate[i][1]=(int)(x0*math.sin(theta)+y0*math.cos(theta))
	
	print(coordinate)
	print()
	

def shear(shx1,shy1):
        print(coordinate)
        for i in range(c):

                temp_x=coordinate[i][0]
                temp_y=coordinate[i][1]
                coordinate[i][0]=(int)(temp_x+shx1*temp_y)
                coordinate[i][1]=(int)(temp_y+shy1*temp_x)
		
        print(coordinate)


print("Enter the number of vertices of polygon")
c=int(input())

for i in range(c):
    x = int(input("Enter x coordinate of vertex:"))
    y = int(input("Enter y coordinate of vertex:"))
    point=[]
    point.append(x)
    point.append(y)
    coordinate.append(point)

print("enter 1 for shear in x-axis and 2 for shear in y axis and 3 for arbitrary line")
temp=(int)(input())


if temp==1:
	shx = float(input("Enter shear factor in x direction:shx="))
	shy=0
elif temp==2:
	shx=0
	shy = float(input("Enter shear factor in y direction:shy=")) 


win_obj=GraphWin("Shear",700,700) #set viewport size  700,700 are device coordinates
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


#previos
for i in range(c-1):
    x0 = coordinate[i][0]
    y0 = coordinate[i][1]
    x1 = coordinate[i+1][0]
    y1 = coordinate[i+1][1]
    #Point(x0,y0).draw(win_obj)
    display = Text(Point(x0,y0),"("+str(x0)+","+str(y0)+")")
    display.draw(win_obj)
    line=Line(Point(x0,y0),Point(x1,y1))
    line.setFill("blue")
    line.draw(win_obj)
x0 = coordinate[0][0]
y0 = coordinate[0][1]
x1 = coordinate[c-1][0]
y1 = coordinate[c-1][1]
#Point(x0,y0).draw(win_obj)
display = Text(Point(x1,y1),"("+str(x1)+","+str(y1)+")")
display.draw(win_obj)
line=Line(Point(x0,y0),Point(x1,y1))
line.setFill("blue")
line.draw(win_obj)

if temp==1:
	shear(shx,shy)	
elif temp==2:
	shear(shx,shy)
elif temp==3:
        shx = float(input("Enter shear factor in x direction:shx="))
        shy = float(input("Enter shear factor in y direction:shy="))
        print("Enter coordinates of line about which shear is to taken")	
        a0=float(input("enter x0 coordinate of shear line"))
        b0=float(input("enter y0 coordinate of shear line"))
        a1=float(input("enter x1 coordinate of shear line"))
        b1=float(input("enter y1 coordinate of shear line"))
        
        if a1-a0 ==0:
                theta = (90*math.pi)/180
        elif b1-b0==0:
                theta=0
        else:
                theta=math.atan((b1-b0)/(a1-a0))
        translation(-a0,-b0)

        if theta ==0:   #shear parallel to x axis
                rotation(-theta)
                shear(shx,0)
                rotation(theta)
        else:
                theta=math.radians(90)-theta
                rotation(theta)
                shear(0,shy)
                rotation(-theta)
        
        translation(a0,b0)


#after shear
for i in range(c-1):
    x0 = coordinate[i][0]
    y0 = coordinate[i][1]
    x1 = coordinate[i+1][0]
    y1 = coordinate[i+1][1]
    #Point(x0,y0).draw(win_obj)
    display = Text(Point(x0,y0),"("+str(x0)+","+str(y0)+")")
    display.draw(win_obj)
    line=Line(Point(x0,y0),Point(x1,y1))
    line.setFill("red")
    line.draw(win_obj)
x0 = coordinate[0][0]
y0 = coordinate[0][1]
x1 = coordinate[c-1][0]
y1 = coordinate[c-1][1]
#Point(x0,y0).draw(win_obj)
display = Text(Point(x1,y1),"("+str(x1)+","+str(y1)+")")
display.draw(win_obj)
line=Line(Point(x0,y0),Point(x1,y1))
line.setFill("red")
line.draw(win_obj)

win_obj.getMouse()
win_obj.close()
