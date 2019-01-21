from graphics import *
#symmetry in ellipse
def symm(x,y):
    pixel=Point(x0+x,y0+y)
    pixel.draw(win_obj)
    pixel=Point(x0+x,y0-y)
    pixel.draw(win_obj)
    pixel=Point(x0-x,y0+y)
    pixel.draw(win_obj)
    pixel=Point(x0-x,y0-y)
    pixel.draw(win_obj)
    time.sleep(0.02)
    print("("+str(x)+","+str(y)+")")
a=int(input("enter major axis:"))
b=int(input("enter minor axis:"))
x0=int(input("enter x coordinate:"))
y0=int(input("enter y coordinate:"))


#radius=int(input("Radius of the circle:"))
#A GraphWin object represents a window on the screen

win_obj=GraphWin("ellipse user Window",700,700) #set viewport size  700,700 are device coordinates
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


pixel=Point(x0,y0)
pixel.draw(win_obj)
origin=Text(Point(-10,-10),"origin")
origin.draw(win_obj)

info=Text(Point(x0-10,y0-10),"("+str(x0)+","+str(y0)+")")
info.draw(win_obj)



x=0
y=b
symm(x,y)
#Region 1
d1=b*b-(a*a*b)+(0.25*a*a)
while((a*a*(y-0.5))>(b*b*(x+1))):
    if(d1<0):
        d1=d1+(b*b)*(2*x+3)
    else:
        d1=d1+(b*b)*(2*x+3)+(a*a)*(-2*y+2)
        y=y-1
    x=x+1
    symm(x,y)
#Region 2
d2=b*b*(x+0.5)*(x+0.5)+a*a*(y-1)*(y-1)-a*a*b*b
while(y>0):
    if (d2<0):
        d2=d2+(b*b)*(2*x+2)+(a*a)*(-2*y+3)
        x=x+1
    else:
        d2=d2+(a*a)*(-2*y+3)
    y=y-1
    symm(x,y)


win_obj.getMouse()
win_obj.close()
