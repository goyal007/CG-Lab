from graphics import *
boundary=[]


def zero_to_one(x0,y0,x1,y1,color):  #slope 0 to 1
    a=y1-y0
    b=-1*(x1-x0)
    di=2*a+b
    dne=2*(a+b)
    de=2*a
    y=y0
    for x in range(x0,x1,1):
        #pixel=Point(x,y)
        #pixel.draw(win_obj,"red")
        pt = Point(x,y)
        pt.setOutline(color)
        pt.draw(win_obj)
        #time.sleep(0.01)
        if(di>0):
            y=y+1
            di=di+dne
        else:
            di=di+de
        boundary.append([x,y])
        print("point"+"["+str(x)+","+str(y)+"]") 
def zero_to_n_one(x0,y0,x1,y1,color): #slope -1 to 0
    a=y1-y0
    b=-1*(x1-x0)
    di=2*a-b
    dne=2*(a-b)
    de=2*a
    y=y0
    for x in range(x0,x1,1):
        #pixel=Point(x,y)
        #pixel.draw(win_obj,"red")
        pt = Point(x,y)
        pt.setOutline(color)
        pt.draw(win_obj)
        #time.sleep(0.01)
        if(di>0):
            di=di+de
        else:
            y=y-1
            di=di+dne
        boundary.append([x,y])
        print("point"+"["+str(x)+","+str(y)+"]")        
################################    
#  greater_one   slope <-1 and >1
def pure_greater_one(x0,y0,x1,y1,color):  #slope >1 
    b=-1*(y1-y0)
    a=x1-x0
    dne=2*(a+b)
    de=2*a
    di=2*a+b
    x=x0
    for y in range(y0,y1,1):
        #pixel=Point(x,y)
        #pixel.draw(win_obj,"red")
        pt = Point(x,y)
        pt.setOutline(color)
        pt.draw(win_obj)
        #time.sleep(0.01)
        if(di>0):
            x=x+1
            di=di+dne
        else:
            di=di+de
        boundary.append([x,y])
        print("point"+"["+str(x)+","+str(y)+"]") 
def less_negative_one(x0,y0,x1,y1,color):  #slope <-1 
    a=x1-x0
    b=-1*(y1-y0)
    di=2*a-b
    dne=2*(a-b)
    de=2*a
    x=x0
    for y in range(y0,y1,1):
        #pixel=Point(x,y)
        #pixel.draw(win_obj,"red")
        pt = Point(x,y)
        pt.setOutline(color)
        pt.draw(win_obj)
        #time.sleep(0.01)
        if(di>0):
            di=di+de
        else:
            x=x-1
            di=di+dne
        boundary.append([x,y])
        print("point"+"["+str(x)+","+str(y)+"]") 
###############################
 
def less_one(x0,y0,x1,y1,color):  #slope -1 to 1
    a=y1-y0
    b=-1*(x1-x0)
    if(a<0):
        zero_to_n_one(x0,y0,x1,y1,color)
    else:
        zero_to_one(x0,y0,x1,y1,color)
        
#the greater_one cases are mirror image of less_one cases so simply replace x and y

def greater_one(x0,y0,x1,y1,color):  #slope > 1 and <-1
    a=x1-x0
    b=-1*(y1-y0)
    if(a<0):
        less_negative_one(x0,y0,x1,y1,color)
    else:
        pure_greater_one(x0,y0,x1,y1,color)
     

def helper(x0,y0,x1,y1,color):
    boundary.append([x0,y0])
    boundary.append([x1,y1])
    
    if(abs(x0-x1)<abs(y0-y1)):              #slope > 1 and <-1
        if(y1>y0):
            greater_one(x0,y0,x1,y1,color)
        else:
            greater_one(x1,y1,x0,y0,color)
    else:
        if(x1>x0):                          #slope -1 to 1
            less_one(x0,y0,x1,y1,color)
        else:                               #we always increase x by 1 therefore start point should always less, so swap both points
            less_one(x1,y1,x0,y0,color) 
    

#####################################################################################################
def intersect(s,p,clipedge):
    #horizontal
    if clipedge[0][1] == clipedge[1][1]: 
        y = clipedge[1][1]
        x = s[0] + (y - s[1])*(p[0]-s[0])/(p[1]-s[1])
    else:#vertical
        x = clipedge[1][0]
        y = s[1] + (x - s[0])*(p[1]-s[1])/(p[0]-s[0])

    return [int(x),int(y)]

def inside(point,clipedge):
    if clipedge[1][0] > clipedge[0][0]: # bottom
        if point[1] >= clipedge[0][1]:
            return 1
    if clipedge[1][1] > clipedge[0][1]: # right
        if point[0] <= clipedge[1][0]:
            return 1
    if clipedge[1][0] < clipedge[0][0]: # top
        if point[1] <= clipedge[0][1]:
            return 1
    if clipedge[1][1] < clipedge[0][1]: # left
        if point[0] >= clipedge[1][0]:
            return 1
    return 0

def polygon_clip(in_vertex_array,inlen,clipedge):
    out_vertex_array=[]
    s=in_vertex_array[inlen-1]
    for i in range(inlen):
        p=in_vertex_array[i]
        if (inside(p,clipedge)):
            if(inside(s,clipedge)):
                out_vertex_array.append(p)
            else:
                intersect_point=intersect(s,p,clipedge)
                out_vertex_array.append(intersect_point)
                out_vertex_array.append(p)
        elif (inside(s,clipedge)):
            intersect_point=intersect(s,p,clipedge)
            out_vertex_array.append(intersect_point)
        s=p
    return out_vertex_array
    



#------------------------------------------------------------------------------------------------------------
x_min = int(input("Enter min x coordinate for window: "))
y_min = int(input("Enter min y coordinate for window: "))
x_max = int(input("Enter max x coordinate for window: "))
y_max = int(input("Enter max y coordinate for window: "))

print("Enter the number of vertices of polygon")
c=int(input())
coordinate = []
for i in range(c):
    x = int(input("Enter x coordinate of vertex:"))
    y = int(input("Enter y coordinate of vertex:"))
    point=[]
    point.append(x)
    point.append(y)
    coordinate.append(point)
temp=[]
temp=coordinate[0]
coordinate.append(temp)
print(coordinate)

win_obj=GraphWin("sutherland Hodgeman User Window",700,700) #set viewport size  700,700 are device coordinates
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

rectangle = Rectangle(Point(x_min,y_min),Point(x_max,y_max))
rectangle.draw(win_obj)
display = Text(Point(x_max+20,y_max+20),"("+str(x_max)+","+str(y_max)+")")
display.draw(win_obj)
display = Text(Point(x_min-20,y_min-20),"("+str(x_min)+","+str(y_min)+")")
display.draw(win_obj)

#previous
for i in range(c):
    x0 = coordinate[i][0]
    y0 = coordinate[i][1]
    x1 = coordinate[i+1][0]
    y1 = coordinate[i+1][1]
    Point(x0,y0).draw(win_obj)
    helper(x0,y0,x1,y1,"yellow")

coordinate = polygon_clip(coordinate,len(coordinate),[[x_min,y_min],[x_max,y_min]])
coordinate = polygon_clip(coordinate,len(coordinate),[[x_max,y_min],[x_max,y_max]])
coordinate = polygon_clip(coordinate,len(coordinate),[[x_max,y_max],[x_min,y_max]])
coordinate = polygon_clip(coordinate,len(coordinate),[[x_min,y_max],[x_min,y_min]])

c=len(coordinate)
temp=[]
temp=coordinate[0]
coordinate.append(temp)
print(coordinate)
for i in range(c):
    x0 = coordinate[i][0]
    y0 = coordinate[i][1]
    x1 = coordinate[i+1][0]
    y1 = coordinate[i+1][1]
    Point(x0,y0).draw(win_obj)
    display = Text(Point(x0-20,y0-20),"("+str(x0)+","+str(y0)+")")
    display.draw(win_obj)
    helper(x0,y0,x1,y1,"red")



win_obj.getMouse()
win_obj.close()
