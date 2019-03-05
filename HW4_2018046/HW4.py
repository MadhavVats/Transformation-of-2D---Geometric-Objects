# name=madhav vats
# roll no.=2018046
# section=A-6
import matplotlib.pyplot as plt
from matplotlib.patches import CirclePolygon
from math import *
instructions=[]
x=0
count=0
flag=0
y=0
zz=""
kkok=0
a=0
b=0
r=0
while zz!="quit":
    if count==0:
        zz=input()
        instructions.append(zz)
        count=count+1
        continue
    if count==1 and instructions[0]=="disc":
        a,b,r=map(int,input().split())
        kkok=1
    elif (count==1 or count==2) and instructions[0]=="polygon":
        if flag==0:
            x=list(map(int,input().split()))
            flag=1

        else:
            y=list(map(int,input().split()))
    if count>2:
        zz=input()
        instructions.append(zz)
    count=count+1
def matmult(l1,l2):
    new=[]
    for i in range(len(l1)):
        lis = []
        for k in range(len(l2[0])):
            sum=0
            for l in range(len(l1[i])):
                sum=sum+l2[l][k]*l1[i][l]

            lis.append(sum)
        new.append(lis)
    return new

def scale(lis,sx,sy):
    return matmult([[sx,0,0],[0,sy,0],[0,0,1]],lis)
def rotate(lis,x):
    x=radians(x)
    return matmult([[cos(x),-sin(x),0],[sin(x),cos(x),0],[0,0,1]],lis)
def translate(lis,dx,dy):
    return matmult([[1,0,dx],[0,1,dy],[0,0,1]],lis)

if instructions[0]=="disc":
#    a,b,r=map(int,instructions[1].split())
    circle = CirclePolygon((a,b), radius = r)
    plt.gca().add_patch(circle)
    verts = circle.get_path().vertices
    x=list(verts[:,0])
    y=list(verts[:,1])
    plt.axis('scaled')

instructions=instructions[1:-1]

k = str(instructions[0])
k = k[2:]
#xs, ys = map(int, k.split())
ins=instructions
r1=r
r2=r
while len(ins)!=0:
    llp=len(x)
    asdf=[1]*llp

    if ins[0][0]=="S":
        k=str(ins[0])
        k=k[2:]
        xs,ys=map(int,k.split())
        x,y=scale([x,y,asdf],xs,ys)[0],scale([x,y,asdf],xs,ys)[1]
        if kkok==1:
            r1=r*xs
            r2=r*ys
            print(a,b,r1,r2)
            print("")
        else:
            print(x)
            print(y)
            print("")
        x.append(x[0])
        y.append(y[0])
        plt.plot(x, y)
        plt.axis('scaled')
        plt.show()
    if ins[0][0]=="R":
        k = str(ins[0])
        k = k[2:]
        de=int(k)
        x,y=rotate([x,y,asdf],de)[0],rotate([x,y,asdf],de)[1]
        if kkok==1:
            print(a,b,r1,r2)
            print("")
        else:
            print(x)
            print(y)
            print("")
        x.append(x[0])
        y.append(y[0])
        plt.plot(x, y)
        plt.axis('scaled')
        plt.show()
    if ins[0][0]=="T":
        k = str(ins[0])
        k = k[2:]
        xs,ys = map(int, k.split())
        x,y=translate([x,y,asdf],xs,ys)[0],translate([x,y,asdf],xs,ys)[1]
        if kkok==1:
            a=a+xs
            b=b+ys
            print(a,b,r1,r2)
        else:
            print(x)
            print(y)
            print("")
        x.append(x[0])
        y.append(y[0])
        plt.plot(x, y)
        plt.axis('scaled')
        plt.show()
    del ins[0]


x.append(x[0])
y.append(y[0])
plt.plot(x,y)
plt.axis('scaled')
plt.show()
