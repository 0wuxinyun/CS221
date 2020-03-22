# building intution:
import numpy as np

# preparation datasets:
'''
(−1) pretty bad
(+1) good plot
(−1) not good
(+1) pretty scenery
'''

# ("pretty", "good", "bad", "plot", "not", "scenery")

def get_x(string):
    x=["pretty", "good", "bad", "plot", "not", "scenery"]
    xi=[0]*len(x)
    for i in string.split():
        indexn=x.index(i)
        xi[indexn]=1
    return np.array(xi)

W=np.array([0]*6)
Y=np.array([-1,+1,-1,+1])
X=[]
raw=['pretty bad','good plot','not good','pretty scenery']
for string in raw:
    X.append(get_x(string))


# Stochastic gradient descent:
def Margin(W,x,y):
    return W.dot(x)*y

def Loss(margin):
    return max(0,1-margin)

def Gradient(x,y,margin):
    if Loss(margin)!=0:
        return -x*y
    else:
        return 0
def SGD(Loss,Margin,X,Y,W):
    lrate=0.5
    for t in range(100):
        for i in range(len(Y)):
            x=X[i]
            y=Y[i]
            margin=Margin(W,x,y)
            g=Gradient(x,y,margin)
            W=W-lrate*g
        print('iteration {}: w = {}, F(w) = {}'.format(t,W, Loss(margin)))
     return W           
SGD(Loss,Margin,X,Y,W)          
 
