import numpy as np
import matplotlib.pyplot as plt
import random
from tqdm import tqdm

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
                    weight=np.sum((e-self.u[i,j,:])**2)
                    weight**=1/2
                    if(weight<min):
                        min=weight
                        winner=self.u[i,j,:]
                        location=(i,j)
        return location

    def adjustWeight(self, location, d,alpha,e):
        bound=self.size-1
        x,y=location
        for i in range(x-d,x+d):
            if(i<0 or i>bound):
                continue
            for j in range(y-d, y+d):
                if(j<0 or j>bound):
                    continue
                self.u[i,j,:]+= alpha*(e-self.u[i,j,:])
               
    def learn(self, data,T, alpha0, d0):

        # Iterate t from 0 to T
        for t in tqdm(range(T)):

	        # Compute current neighborhood radius d and learning rate alpha
            alpha = alpha0 * (1 - t/T)
            d = int(np.ceil(d0 * (1 - t/T)))
            
            # Pick an input e from the training set at random

            e=data[np.random.randint(len(data))]

	        # Find the winning unit whose weights are closest to this e
            c=self.findWinner(e)

            # Loop over the neighbors of this winner, adjusting their weights
            self.adjustWeight(c,d,alpha,e)
	    
def plot(som, data):

    for j in range(som.size):

        for k in range(som.size):

            # Get the two-dimension weight for this neuron
            p = som.u[j, k]

            # Plot the location of the weight as a red circle
            plt.plot(p[0], p[1], 'ro')

            # Plot line to neighbor in adjacent row
            if j < som.size - 1:
                nbr = som.u[j+1, k]
                xs = [p[0], nbr[0]]
                ys = [p[1], nbr[1]]
                plt.plot(xs, ys, 'b')
            if k < som.size - 1:
                nbr = som.u[j, k+1]
                xs = [p[0], nbr[0]]
                ys = [p[1], nbr[1]]
                plt.plot(xs, ys, 'b')


    plt.scatter(data[:,0], data[:,1], s=.2)
    plt.gca().set_aspect('equal')
    plt.title("som")
    plt.show()

def main():

    som = SOM(8, 2)

    data = np.random.random((5000, 2))
    r = (data[:,0]-.5)**2 + (data[:,1]-.5)**2
    logicalOutput=np.logical_and(r<0.2, r>0.1)
    print(type(logicalOutput))
    #data=np.select(logicalOutput,data)
    data=np.where(logicalOutput, data)
    print(data)
    
    #som.learn(data, 4000, 0.02, 4)

    plot(som, data) 

if __name__ =="__main__":

    main()
