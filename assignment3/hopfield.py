import numpy as np
import matplotlib.pyplot as plt
import random
from tqdm import tqdm

class Hopfield():

    def __init__(self, n):
        self.n=n
        self.T=np.zeros((n,n))

    def learn(self, data):

        # Accumulate weights over patterns
        for a in data:

                self.T += np.outer(2 * a - 1, 2 * a - 1)

        # Zero-out the diagonal (no self connections!)
        np.fill_diagonal(self.T, 0)


    def test(self, pattern, niter=5):
        for iter in range(niter):
            #pattern+=np.outer(pattern, self.T)
            for j in range(len(pattern)):
                for i in range(j+1, len(pattern)):
                    pattern[j]+=pattern[i]*self.T[i,j]
        return np.round(pattern)

def show_confusion(arr1, arr2):
    for i in range(len(arr1)):
        a=arr1[i]
        for j in range(i+1):
            b=arr2[j]
            cos=np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))
            if(cos!=0):
                print('%5.3f '%cos, end='')
        print()

def noisy_copy(arr, prob):
    probArr=np.random.random(arr.shape)
    outputArr=np.where(probArr<prob, 1-arr, arr)
    return outputArr

def random_array(rows, cols):

    return np.round(np.random.random((5, 30)))


def main():

    print('Part 1: Generate some training data --------------------------------------------------')
    data = random_array(5, 30)
    print(data)

    print('\nPart 2: Vector-cosine confusion matrix of an array with itself ---------------------')
    show_confusion(data, data)

    print('\nPart 3: Confusion matrix with 25% noise -----------------------------------------------')
    show_confusion(data, noisy_copy(data, 0.25))

    print('\nPart 4: Recovering small patterns with a Hopfield net -----------------------------------')
    net = Hopfield(30)
    net.learn(data)
    testData=np.round(np.random.random(30))
    print("Input:"+np.array_str(testData))
    print("Output:"+np.array_str(net.test(testData)))
    print('\n\nRecover pattern, no noise:')
    noiseData=noisy_copy(testData,0.25)
    print("Input:"+np.array_str(noiseData))
    print("Output:"+np.array_str(net.test(noiseData)))
    print("Original:"+np.array_str(testData))

if __name__ =="__main__":
    main()
