import numpy as np
import matplotlib.pyplot as plt
import random
from tqdm import tqdm

class Hopfield():

    def __init__(self, n):
        self.n=n
        self.T=np.zeros((n,n))
    def learn(data):
        for a in data:
            self.t[]

    def test():
        pass
def show_confustion(arr1, arr2):
    for i in range(len(arr1)):
        a=arr1[i]
        for j in range(len(arr2)):
            b=arr2[j]
            cos=np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))
            if(cos!=0):
                print('%5.3f '%cos, end='')
        print()

def noisy_copy(arr, prob):
    probArr=np.random.random(arr.shape)
    outputArr=np.where(probArr<prob, 1-arr, arr)
    return outputArr

def main():
    data = np.round(np.random.random((5, 30)))
    #data = np.random.random((5, 30))
    #print(np.linalg.norm(data[1]))
    #show_confustion(data,data)
    print(noisy_copy(data, 0))

if __name__ =="__main__":
    main()