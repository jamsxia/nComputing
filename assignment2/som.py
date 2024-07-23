import numpy as np
import matplotlib.pyplot as plt
import random
class SOM():
    def __init__(self, m, n):
        self.size=m
        self.dimen=n
        self.u=np.random.random((m,m,n))
        self.u/=10
        self.u+=0.45

    def plot(self):
        for j in range(self.size):
            for k in range(self.size):
                plt.scatter(self.u[k,j,:], self.u[k,j,:], s=0.2)
                plt.plot("ro")
        plt.show()
        
    def findWinner(self,e):
        
        
    def learn(self, t, alpha, d):
        for i in range(t):
            currentAlpha=alpha(1-i/t)
            currentD=d(1-i/t)

            e=np.random.choice(self.u)

            c=self.findWinner(e)

            

            

            

            
            

def main():
    data=np.random.random((5000,2))
    ##print(arr1)
    a=SOM(5000,2)
    a.plot()
    '''plt.scatter(data[:,0], data[:,1], s=.2)
    plt.gca().set_aspect('equal')
    plt.show()'''
    

if __name__ =="__main__":
    main()
