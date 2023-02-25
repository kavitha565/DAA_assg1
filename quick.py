import random
from timeit import default_timer as timer

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
                
def saveOutputToFile(sortedArrays, fileName, timeTaken):
    with open(fileName, "w") as f:
        for arr in sortedArrays:
            f.write(" ".join(str(ele) for ele in arr)+"\n")
        f.write(f"Time taken to sort - {timeTaken:6f} seconds")

def partition(arr,low,high,sortByLastColumn):
    pivot = arr[high][-1] if sortByLastColumn else arr[high]
    i = low-1
    for j in range(low,high):
        if(arr[j][-1]<=pivot if sortByLastColumn else arr[j]<=pivot):
            i=i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1
            
def quickSort(arr,low,high,sortByLastColumn):
    if(low<high):
        pivot = partition(arr,low,high,sortByLastColumn)
        quickSort(arr,low,pivot-1,sortByLastColumn)
        quickSort(arr,pivot+1,high,sortByLastColumn)

def sortData(inputFileName,outputFileName):
    with open(inputFileName, "r") as f:
        arrays = []
        for data in f:
            arr = [int(ele) for ele in data.split()]
            arrays.append(arr)
        beforeTime = timer()
        for i in range(len(arrays)):
                        quickSort(arrays[i],0,len(arrays[i])-1,False)

        #Sort the rows by the last column only and display each row in an ascending order as well as the last column
        quickSort(arrays,0,len(arrays)-1,True)
        timeTaken = timer() - beforeTime
        print(f"Time taken to sort array of size {len(arrays)} by quick sort is {timeTaken:6f} seconds")
        
        saveOutputToFile(arrays,outputFileName,timeTaken)



#generateListsAndSaveToFile()
sortData('arr20.txt','arrQS_O_20.txt')
sortData('arr100.txt','arrQS_O_100.txt')
sortData('arr2000.txt','arrQS_O_2000.txt')
sortData('arr6000.txt','arrQS_O_6000.txt')

