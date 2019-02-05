from graphics import *
##############################
#   less_one   slope -1 to 1

boundary=[]
color="black"
color1="red"  #correct
color2="blue" #clipped
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
        win_obj.plot(x,y,color)
        win_obj.plot(x,y,color)
        time.sleep(0.01)
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
        win_obj.plot(x,y,color)
        win_obj.plot(x,y,color)
        time.sleep(0.01)
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
        win_obj.plot(x,y,color)
        win_obj.plot(x,y,color)
        time.sleep(0.01)
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
        win_obj.plot(x,y,color)
        win_obj.plot(x,y,color)
        time.sleep(0.01)
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
def parameter():   
    te=0.0
    tl=1.0
    diff_p_x=x1-x0
    diff_p_y=y1-y0
    
    
    #case1
    nd=-1*diff_p_x

    if nd==0:
        return
        
    temp=(1)*(x0-xmin)/nd
    if(nd>0):
        tl=min(temp,tl)
    else:  
        te=max(te,temp)
    #case2
    nd=1*diff_p_x
    if nd==0:
        return
    
    temp=(-1)*(x0-xmax)/nd
    if(nd>0):
        tl=min(temp,tl)
    else:  
        te=max(te,temp)
    #case3
    nd=-1*diff_p_y
    if nd==0:
        return
    
    temp=(1)*(y0-ymin)/nd
    if(nd>0):
        tl=min(temp,tl)
    else:  
        te=max(te,temp)
    #case4
    nd=1*diff_p_y
    if nd==0:
        return
    temp=(-1)*(y0-ymax)/nd
    if(nd>0):
        tl=min(temp,tl)
    else:  
        te=max(te,temp)

    if te>tl:
        return 

    
    a=x0+(x1-x0)*te
    b=y0+(y1-y0)*te
    
    c=x0+(x1-x0)*tl
    d=y0+(y1-y0)*tl
    
    helper(int(a),int(b),int(c),int(d),color1)



#####################################################################################################

#A GraphWin object represents a window on the screen



t=4#sides of rectangle
lista=[]

xmin=int(input("enter xmin coordinate of window:"))
ymin=int(input("enter ymin coordinate of window:"))
xmax=int(input("enter xmax coordinate of window:"))
ymax=int(input("enter ymax coordinate of window:"))


x0=int(input("enter x0 coordinate of line to be clipped:"))
y0=int(input("enter y0 coordinate of line to be clipped:"))
x1=int(input("enter x1 coordinate of line to be clipped:"))
y1=int(input("enter y1 coordinate of line to be clipped:"))



lista.append([xmin,ymin])
lista.append([xmax,ymin])
lista.append([xmax,ymax])
lista.append([xmin,ymax])
list_ini_point=lista[0]
#x0=list_ini_point[0]
#y0=list_ini_point[1]
lista.append(list_ini_point)
#x01=x0
#y01=y0


win_obj=GraphWin("parameteric line clipping User Window",700,700) #set viewport size  700,700 are device coordinates
win_obj.setBackground("White")
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

#for rectangle
initial_point=Text(Point(xmin,ymin),"("+str(xmin)+","+str(ymin)+")")
initial_point.draw(win_obj)
final_point=Text(Point(xmax,ymax),"("+str(xmax)+","+str(ymax)+")")
final_point.draw(win_obj)




#for line
initial_point=Text(Point(x0,y0),"("+str(x0)+","+str(y0)+")")
initial_point.draw(win_obj)
final_point=Text(Point(x1,y1),"("+str(x1)+","+str(y1)+")")
final_point.draw(win_obj)

#edge_table=[]
j=0
while (j!=t):
    list_t1=lista[j]
    list_t2=lista[j+1]
    x01=list_t1[0]
    y01=list_t1[1]
    x02=list_t2[0]
    y02=list_t2[1]
    helper(x01,y01,x02,y02,color)
    j=j+1
#print(edge_table)
#scanline()
helper(x0,y0,x1,y1,color2)
parameter()

win_obj.getMouse()
win_obj.close()
