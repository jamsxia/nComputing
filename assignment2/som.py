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

       
    def findWinner(self,e):
        min=10000
        for i in range(self.size):
            for j in range(self.size):
                weight=0
                for k in range(self.dimen):
                    weight+=(e-self.u[i,j,k])**2
                weight**=1/2
                if(weight<min):
                    min=weight
                    winner=self.u[i,j,:]
                    location=(i,j)
        return location

    def adjustWeight(self, location, d,alpha):
        bound=self.size-1
        x,y=location
        for i in range(x-d,x+d):
            if(i<0 or i>bound):
                continue
            for j in range(y-d, y+d):
                if(j<0 or j>bound):
                    continue
               self.u[i,j,:]+= alpha*(e)
               
    def learn(self, T, alpha0, d0):

        # Iterate t from 0 to T
        for t in range(T):

	    # Compute current neighborhood radius d and learning rate alpha
            alpha = alpha0 * (1 - t/T)
            d = int(np.ceil(d0 * (1 - t/T)))
            
            # Pick an input e from the training set at random
            i = int(self.size * random.random())
            j = int(self.size * random.random())
            #print(self.u[i,j,:])
            #e=np.random.choice(self.u[i,j,:])
            e=np.random.choice(self.u[i,j])
            #print(e)

	    # Find the winning unit whose weights are closest to this e
            c=self.findWinner(e)
            #print(c)

            # Loop over the neighbors of this winner, adjusting their weights
            #self.adjustWeight(c,d,alpha)
	    
def plot(som, data):

    for j in range(som.size):

        for k in range(som.size):

            # Get the two-dimension weight for this neuron
            p = som.u[j, k]

            # Plot the location of the weight as a red circle
            plt.plot(p[0], p[1], 'ro')

    plt.scatter(data[:,0], data[:,1], s=.2)
    plt.gca().set_aspect('equal')
    plt.show()

def main():

    # data = np.random.random((5000, 2))

    som = SOM(8, 2)

    data = np.random.random((5000, 2))

    som.learn(4000, 0.02, 4)

    # plot(som, data) 

if __name__ =="__main__":

    main()
