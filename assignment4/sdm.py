import numpy as np
import matplotlib.pyplot as plt
import random
from tqdm import tqdm

class SDM():
    def __init__(self, pattern, n):
        self.pattern=pattern
        self.n=n
        self.radius=0.451*ncol
        self.nPhyAdd=2000
        self.address=np.round(np.random.random((self.p, self.n)))
        self.data=np.zeros((self.p,self.n))
    def enter(self, addVector):
        # page8
        for i in range(self.p):
            keyAddress=addVector
            if(np.absolute(keyAddress- self.address[i])<=self.radius):
                ## change data
                data[p]=np.where(data[p]==1, 1+data[p], data[p]-1)

    def lookup(self, addVector):
        #page9
        for i in range(self.p):
            vec=np.zeros(self.n)
            keyAddress=addVector
            if(np.absolute(keyAddress- address)<=self.radius):
                vec=np.add(vec, data[i])
        return vec=np.where(vec>0, 1, 0)

    def learn(self):
        # radius metric by hamming distance: sum of number of location difference

    def test(self):
        pass
    
def plot(arr, ncol):
    nrow=int(arr.size/ncol)
    record=0
    for i in range(arr.size):
        if(record==ncol):
            print()
            record=0
        if(arr[i]==1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
        record+=1
    print()
def ring():
    '''array=[[0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
           [0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0],
           [0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0],
           [0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0],
           [0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0],
           [1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1],
           [1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1],
           [1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1],
           [1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1],
           [1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1],
           [1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1],
           [0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0],
           [0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0],
           [0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0],
           [0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0],
           [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0]]'''
    array=[0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,
           0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,
           0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,
           0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,
           0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0,
           1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,
           1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,
           1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,
           1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,
           1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,
           1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,
           0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0,
           0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,
           0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,
           0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,
           0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0]
    '''array2=array.copy()
    array2.reverse()
    array+=array2
    print(array)'''
    #flatten_list = [j for sub in array for j in sub]
    #print(flatten_list)
    return np.array(array)
def main():
    testpat = np.random.random_integers(0, 1, 256)
    plot(testpat,16)
    print("***********************************")
    r=ring()
    plot(r,16)

if __name__ =="__main__":
    main()