from graphics import *

def symmetry(x,y):
    pixel=Point(x0+x,y0+y)
    pixel.draw(win_obj)
    pixel=Point(x0+y,y0+x)
    pixel.draw(win_obj)
    pixel=Point(x0+y,y0-x)
    pixel.draw(win_obj)
    pixel=Point(x0+x,y0-y)
    pixel.draw(win_obj)
    pixel=Point(x0-x,y0-y)
    pixel.draw(win_obj)
    pixel=Point(x0-y,y0-x)
    pixel.draw(win_obj)
    pixel=Point(x0-y,y0+x)
    pixel.draw(win_obj)
    pixel=Point(x0-x,y0+y)
    pixel.draw(win_obj)
    time.sleep(0.02)
    print("("+str(x)+","+str(y)+")")



x0=int(input("enter x coordinate of center:"))
y0=int(input("enter y coordinate of center:"))
radius=int(input("Radius of the circle:"))
#A GraphWin object represents a window on the screen

win_obj=GraphWin("circle user Window",700,700) #set viewport size  700,700 are device coordinates
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

center_coord=Point(x0,y0)
center_coord.draw(win_obj)

origin=Text(Point(-10,-10),"origin")
origin.draw(win_obj)

center_text=Text(Point(x0-10,y0-10),"("+str(x0)+","+str(y0)+")")
center_text.draw(win_obj)


di=1-radius
xp=0.0
yp=radius+0.0
while(yp>xp):
	xp=xp+1
	if(di>0):
		yp=yp-1
		di=di+2*(xp-yp)+5
	else:
		di=di+2*xp+3
	symmetry(xp,yp)
win_obj.getMouse()
win_obj.close()
