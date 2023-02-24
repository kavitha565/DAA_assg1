import random
from timeit import default_timer as timer

def generateListsAndSaveToFile():
    arrSizes = [20, 100, 2000, 6000, 10000]
    for size in arrSizes:
        randomArr = []
        for _ in range(size):
            arr = []
            for _ in range(3):
                arr.append(random.randint(0,99))
            randomArr.append(arr)
        with open(f"arr{size}.txt", "w") as f:
            for arr in randomArr:
                f.write(" ".join(str(ele) for ele in arr)+"\n")

def saveOutputToFile(sortedArrays, fileName):
    with open(fileName, "w") as f:
        for arr in sortedArrays:
            f.write(" ".join(str(ele) for ele in arr)+"\n")
        
def insertionSort(arr, sortByLastColumn):
    for j in range(1,len(arr)):
        key = arr[j]
        i=j-1
        if(sortByLastColumn):
            while i >= 0 and arr[i][-1] > key[-1]:
                arr[i+1] = arr[i]
                i=i-1
        else:
            while i >= 0 and arr[i] > key:
                arr[i+1] = arr[i]
                i=i-1
        arr[i+1] = key

def insertionSortByLastColumn(arr):
    for j in range(1,len(arr)):
        key = arr[j]
        i=j-1
        while i >= 0 and arr[i][-1] > key[-1]:
            arr[i+1] = arr[i]
            i=i-1
        arr[i+1] = key
    return arr

def sortData(inputFileName,outputFileName):
    with open(inputFileName, "r") as f:
        arrays = []
        for data in f:
            arr = [int(ele) for ele in data.split()]
            arrays.append(arr)
        beforeTime = timer()
        for i in range(len(arrays)):
                        insertionSort(arrays[i],False)
        #Sort the rows by the last column only and display each row in an ascending order as well as the last column
        insertionSort(arrays,True)
        timeTaken = timer() - beforeTime
        print(f"Time taken to sort array of size {len(arrays)} by insertion sort is {timeTaken:6f} seconds")
        
        saveOutputToFile(arrays,outputFileName)



generateListsAndSaveToFile()
sortData('arr20.txt','arrIS_O_20.txt')
sortData('arr100.txt','arrIS_O_100.txt')
sortData('arr2000.txt','arrIS_O_2000.txt')
sortData('arr6000.txt','arrIS_O_6000.txt')
sortData('arr10000.txt','arrIS_O_10000.txt')

