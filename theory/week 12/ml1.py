
import numpy as np
# model
# points=[(2,4),(4,2)]

# generate artificial data

true=[1,2,3,4,5]
d=len(true)
points=[]
for a in range(10000):
    x=np.random.rand(d)
    y=np.dot(x,true) +np.random.rand()
    points.append((x,y))
    


# print(points)
def FW(w):

    return sum((np.dot(w,x)-y)**2 for x,y in points)/len(points)

def df(w):
    return sum(2*(np.dot(w,x)-y)*x for x,y in points)/len(points)
# algorithm
def gradient_decent(FW,df,d):
    w=np.zeros(d)
    print("w:",w)
    for a in range(1000):
        value=FW(w)
        gradient=df(w)
        w=w-0.01*gradient
        print("w:",w,"value:",value)
        

gradient_decent(FW,df,d)