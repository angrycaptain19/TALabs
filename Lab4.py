from numpy import random
import time

blessRNG1K = random.randint(1500, size=1000)
bub11 = blessRNG1K.copy()
ins11 = blessRNG1K.copy()
sel11 = blessRNG1K.copy()
blessRNG10K = random.randint(10500, size=10000)
bub110 = blessRNG10K.copy()
ins110 = blessRNG10K.copy()
sel110 = blessRNG10K.copy()
blessRNG100K = random.randint(100500, size=100000)
bub1100 = blessRNG100K.copy()
ins1100 = blessRNG100K.copy()
sel1100 = blessRNG100K.copy()

pogChamp1K = [x for x in range(0, 1000)]
bub21 = pogChamp1K.copy()
ins21 = pogChamp1K.copy()
sel21 = pogChamp1K.copy()
pogChamp10K = [x for x in range(0, 10000)]
bub210 = pogChamp10K.copy()
ins210 = pogChamp10K.copy()
sel210 = pogChamp10K.copy()
pogChamp100K = [x for x in range(0, 100000)]
bub2100 = pogChamp100K.copy()
ins2100 = pogChamp100K.copy()
sel2100 = pogChamp100K.copy()


def main():
    start_time = time.time()
    bubbleSort(bub11)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    bubbleSort(bub110)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    bubbleSort(bub1100)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    insertionSort(ins11)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    insertionSort(ins110)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    insertionSort(ins1100)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    selectionSort(sel11)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    selectionSort(sel110)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    selectionSort(sel1100)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    bubbleSort(bub21)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    bubbleSort(bub210)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    bubbleSort(bub2100)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    insertionSort(ins21)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    insertionSort(ins210)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    insertionSort(ins2100)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    selectionSort(sel21)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    selectionSort(sel210)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    selectionSort(sel2100)
    print("--- %s seconds ---" % (time.time() - start_time))



def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == '__main__':
    main()
