import random
import time
import numpy as np
import matplotlib.pyplot as plt

def createList(size):
    arr=[None]*size
    for i in range(size):
        arr[i]=random.random()
    return arr

def dotProduct(arr1, arr2):
    if (len(arr1)!=len(arr2)):
        return
    returnVal=0
    for i in range(len(arr1)):
        returnVal+=arr1[i]*arr2[i]
    return returnVal

def main():
    #arr1=createList(1000000)
    #arr2=createList(1000000)
    arr1=createList(2)
    arr2=createList(2)
    startTime=time.time()
    dotValue=dotProduct(arr1, arr2)
    endTime=time.time()
    duration=endTime-startTime

    npArr1=np.asarray(arr1)
    npArr2=np.asarray(arr2)
    startNpTime=time.time()
    npDotValue=np.dot(npArr1, npArr2)
    endNpTime=time.time()
    durationNp=endNpTime-startNpTime
    #print(arr1)
    #print(arr2)
    #print(dotValue)
    #print(npDotValue)
    print(duration)
    print(durationNp)

    ## part3
    timeMine=np.empty(0)
    timeNp=np.empty(0)
    sizeCount=np.empty(0)
    for i in range(1000000, 10000000, 1000000):
        sizeCount=np.append(sizeCount, i)
        arr1=createList(i)
        arr2=createList(i)
        npArr1=np.asarray(arr1)
        npArr2=np.asarray(arr2)
        
        startTime=time.time()
        dotValue=dotProduct(arr1, arr2)
        endTime=time.time()
        duration=endTime-startTime
        timeMine=np.append(timeMine, duration)

        startNpTime=time.time()
        npDotValue=np.dot(npArr1, npArr2)
        endNpTime=time.time()
        durationNp=endNpTime-startNpTime
        timeNp=np.append(timeNp, durationNp)

    plt.plot(sizeCount, timeMine, label="My dot product")
    plt.plot(sizeCount, timeNp, label="numpy")    
    plt.xlabel('number of values')
    plt.ylabel('times(sec)')
    plt.legend()
    plt.show()


if __name__ =="__main__":
    main()
