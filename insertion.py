import random
import time

def generateListsAndSaveToFile():
    arrSizes = [20, 100, 2000, 6000]
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
        
def insertionSort(arr):
    for j in range(1,len(arr)):
        key = arr[j]
        i=j-1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i=i-1
        arr[i+1] = key
    return arr

def insertionSortByLastColumn(arr):
    for j in range(1,len(arr)):
        key = arr[j]
        i=j-1
        while i >= 0 and arr[i][-1] > key[-1]:
            arr[i+1] = arr[i]
            i=i-1
        arr[i+1] = key
    return arr

def sortData(inputFileName,outputFileName,sortType):
    with open(inputFileName, "r") as f:
        unsortedArrays = []
        sortedArrays = []
        sortedArraysByColumn = []
        for data in f:
            arr = [int(ele) for ele in data.split()]
            unsortedArrays.append(arr)
        startTime = time.time()
        for i in range(len(unsortedArrays)):
                match sortType:
                    case "insertion":
                        sortedArrays.append(insertionSort(unsortedArrays[i]))

        #Sort the rows by the last column only and display each row in an ascending order as well as the last column
        sortedArraysByColumn = insertionSortByLastColumn(sortedArrays)
        endTime = time.time()
        timeTaken = endTime - startTime
        print(f"Time taken to sort array of size {len(sortedArraysByColumn)} by {sortType} sort is {timeTaken:6f} seconds")
        
        saveOutputToFile(sortedArraysByColumn,outputFileName)



generateListsAndSaveToFile()
sortData('arr20.txt','arrIS_O_20.txt','insertion')
sortData('arr100.txt','arrIS_O_100.txt','insertion')
sortData('arr2000.txt','arrIS_O_2000.txt','insertion')
sortData('arr6000.txt','arrIS_O_6000.txt','insertion')

