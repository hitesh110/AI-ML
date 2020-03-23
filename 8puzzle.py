goal =[1,2,3,4,5,6,7,8,0]
class graph :
    target=int()
    stop=0
    n = -1
    c = 1
    node = int()
    parent = int()
    a = {}
    a[1] = int ()
    a[2] = int ()
    a[3] = int ()
    a[4] = int ()
    a[5] = int ()
    a[6] = int ()
    a[7] = int ()
    a[8] = int ()
    a[9] = int () 
    b = int()
    lock = []
def up(obb = graph(),p = int()) :
    print("up")
    check=0
    size=len(graph.lock)
    if(size!=0):
        for i in range(size):
            y=graph.lock[i]
            y=y+3
            if(y>0):
                if obj[graph.n].a[y]==0:
                    check=1
    if obj[graph.n].a[1]!=0 and obj[graph.n].a[2]!=0 and obj[graph.n].a[3]!=0 and check==0:
        temp=obj[graph.n].b
        temp=temp-3
        obj[graph.n].a[obj[graph.n].b]=obj[graph.n].a[temp]
        obj[graph.n].a[temp]=0
        obj[graph.n].b=temp
        print(obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9])
      
def down(obb = graph(),p = int()) :
    print("down")
    check=0
    size=len(graph.lock)
    if(size!=0):
        for i in range(size):
            y=graph.lock[i]
            y=y-3
            if(y>0):
                if obj[graph.n].a[y]==0:
                    check=1
    if obj[graph.n].a[7]!=0 and obj[graph.n].a[8]!=0 and obj[graph.n].a[9]!=0 and check==0:
        temp=obj[graph.n].b
        temp=temp+3
        obj[graph.n].a[obj[graph.n].b]=obj[graph.n].a[temp]
        obj[graph.n].a[temp]=0
        obj[graph.n].b=temp
        print(obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9])

def right(obb = graph(),p = int()) :
    print("right")
    check=0
    size=len(graph.lock)
    if(size!=0):
        for i in range(size):
            y=graph.lock[i]
            y=y-1
            if(y>0):
                if obj[graph.n].a[y]==0:
                    check=1
    if obj[graph.n].a[3]!=0 and obj[graph.n].a[6]!=0 and obj[graph.n].a[9]!=0 and check==0:
        temp=obj[graph.n].b
        temp=temp+1
        obj[graph.n].a[obj[graph.n].b]=obj[graph.n].a[temp]
        obj[graph.n].a[temp]=0
        obj[graph.n].b=temp
        print(obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9])

def left(obb = graph(),p = int()) :
    print("left")
    check=0
    size=len(graph.lock)
    if(size!=0):
        for i in range(size):
            y=graph.lock[i]
            y=y+1
            if(y>0):
                if obj[graph.n].a[y]==0:
                    check=1
    if obj[graph.n].a[1]!=0 and obj[graph.n].a[4]!=0 and obj[graph.n].a[7]!=0 and check==0:
        temp=obj[graph.n].b
        temp=temp-1
        obj[graph.n].a[obj[graph.n].b]=obj[graph.n].a[temp]
        obj[graph.n].a[temp]=0
        obj[graph.n].b=temp
        print(obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9])

def lock(index = int()):
    graph.lock.append(index)

def unlock():
    graph.lock.pop()
    
obj = {}
graph.n = graph.n+1
obj[graph.n] = graph()
obj[graph.n].node=graph.n
obj[graph.n].parent=-1
obj[graph.n].a[1]=5
obj[graph.n].a[2]=2
obj[graph.n].a[3]=6
obj[graph.n].a[4]=7
obj[graph.n].a[5]=0
obj[graph.n].a[6]=8
obj[graph.n].a[7]=4
obj[graph.n].a[8]=1
obj[graph.n].a[9]=3
obj[graph.n].b=5
up()
up()
left()
left()
temp=int()
y=1
for i in range(9):
    if obj[graph.n].a[y]==1:
        temp=y
    y=y+1
print(graph.lock)
#temp=6
#print("   ")
print(temp)
print("firsttttt")
if temp==1:
    print("")
if temp==2:
    right()
if temp==3:
    right()
    right()
    down()
    left()
    left()
    up()
    right()
if temp==4:
    down()
if temp==5:
    down()
    right()
    up()
    left()
    down()
if temp==6:
    down()
    right()
    right()
    up()
    left()
    left()
    down()
    right()
    up()
    left()
    down()

if temp==7:
    down()
    down()
    right()
    up()
    up()
    left()
    down()
if temp==8:
    down()
    right()
    down()
    left()
    up()
    right()
    up()
    left()
    down()
if temp==9:
    down()
    right()
    right()
    down()
    left()
    up()
    right()
    down()
    left()
    left()
    up()
    right()
    up()
    left()
    down()
    
lock(1)
right()
right()
up()
up()
left()
left()
y=1
for i in range(9):
    if obj[graph.n].a[y]==3:
        temp=y
    y=y+1
print(obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9])   
print("yesyesyes")
print(y)
#temp=y
print("seconddddd")
if temp==3 :
    right()
if temp==4:
    down()
    left()
    down()
    right()
    right()
    up()
    up()
    left()
    down()
if temp==5:
    down()
if temp==6:
    down()
    right()
    up()
    left()
    down()
if temp==7:
    down()
    down()
    left()
    up()
    right()
    down()
    right()
    up()
    up()
    left()
    down()
if temp==8:
    down()
    down()
    right()
    up()
    up()
    left()
    down()
if temp==9:
    down()
    right()
    down()
    left()
    up()
    right()
    up()
    left()
    down()
    
#lock(2)
right()
right()
up()
up()

y=1
for i in range(9):
    if obj[graph.n].a[y]==2:
        temp=y
    y=y+1
print(temp)
print("thirdddddddd")
if temp==6:
    #unlock(2)
    left()
    down()
    down()
    right()
    up()
    left()
    up()
    right()
    down()
    down()
    left()
    up()
    right()
if temp==4:
    down()
    left()
    left()
if temp==5:
    print('')
if temp==7:
    down()
    down()
    left()
    left()
    up()
    right()
    down()
if temp==8:
    down()
    left()
    down()
if temp==9:
    down()
    down()
    left()
    up()
    right()
lock(2)
lock(5)
down()
right()
right()
up()
up()
unlock()
unlock()
left()
down()
lock(2)
lock(3)


left()
left()
up()
up()
y=1
for i in range(9):
    if obj[graph.n].a[y]==4:
        temp=y
    y=y+1

print(temp)
#temp=y
print("fourthhhhhh")
if temp==5:
    right()
if temp==6:
    right()
    right()
    down()
    left()
    left()
    up()
    right()
if temp==7:
    down()
if temp==8:
    right()
    down()
    left()
    up()
    right()
if temp==9:
    right()
    right()
    down()
    left()
    up()
    right()
    down()
    left()
    left()
    up()
    right()
lock(4)
down()
left()
left()

y=1
for i in range(9):
    if obj[graph.n].a[y]==5:
        temp=y
    y=y+1
#temp=y
print(temp)
print("fifthhhhhh")
if temp==5:
    print("")
if temp==6:
    right()
    up()
    right()
if temp==8:
    unlock()
    up()
    right()
    down()
    right()
    up()
    left()
    left()
    down()
    right()
    up()
    right()
    lock(4)
if temp==9:
    right()
    right()
    up()
    left()
    down()
#lock(4)
lock(5)
down()
left()
left()
unlock()
unlock()
print(graph.lock)
up()
right()

while obj[graph.n].a[6]!=6:
    down()
    right()
    up()
    left()
left()
down()
right()
right()

print(obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9])   