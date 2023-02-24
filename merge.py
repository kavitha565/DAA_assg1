from timeit import default_timer as timer

def saveOutputToFile(sortedArrays, fileName):
    with open(fileName, "w") as f:
        for arr in sortedArrays:
            f.write(" ".join(str(ele) for ele in arr)+"\n")

def merge(arr,p,q,r,sortByLastColumn):
    len1 = q-p+1
    len2 = r-q
    leftArr = [0] * len1
    rightArr = [0] * len2
    for i in range(0,len1):
        leftArr[i]=arr[p+i]
    for j in range(0,len2):
        rightArr[j]=arr[q+j+1]
    i=0
    j=0
    k=p

    if(sortByLastColumn):
        while i<len1 and j<len2:
            if leftArr[i][-1]<=rightArr[j][-1]:
                arr[k]=leftArr[i]
                i=i+1
            else:
                arr[k]=rightArr[j]
                j=j+1
            k=k+1
    else:
        while i<len1 and j<len2:
            if leftArr[i]<=rightArr[j]:
                arr[k]=leftArr[i]
                i=i+1
            else:
                arr[k]=rightArr[j]
                j=j+1
            k=k+1
    
    while i<len1:
        arr[k]=leftArr[i]
        i=i+1
        k=k+1
    while j<len2:
        arr[k]=rightArr[j]
        j=j+1
        k=k+1


def mergeSort(arr,p,r,sortByLastColumn):
    if p<r:
        q = (p+r)//2
        mergeSort(arr,p,q,sortByLastColumn)
        mergeSort(arr,q+1,r,sortByLastColumn)
        merge(arr,p,q,r,sortByLastColumn)

def sortData(inputFileName,outputFileName):
    with open(inputFileName, "r") as f:
        arrays = []
        for data in f:
            arr = [int(ele) for ele in data.split()]
            arrays.append(arr)
        beforeTime = timer()
        for i in range(len(arrays)):
                        mergeSort(arrays[i],0,len(arrays[i])-1,False)

        #Sort the rows by the last column only and display each row in an ascending order as well as the last column
        mergeSort(arrays,0,len(arrays)-1,True)
        timeTaken = timer() - beforeTime
        print(f"Time taken to sort array of size {len(arrays)} by merge sort is {timeTaken:6f} seconds")
        
        saveOutputToFile(arrays,outputFileName)



#generateListsAndSaveToFile()
sortData('arr20.txt','arrMS_O_20.txt')
sortData('arr100.txt','arrMS_O_100.txt')
sortData('arr2000.txt','arrMS_O_2000.txt')
sortData('arr6000.txt','arrMS_O_6000.txt')
sortData('arr10000.txt','arrMS_O_10000.txt')

