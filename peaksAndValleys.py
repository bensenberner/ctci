'''
in an array of ints, a peak is an element which is greater than or equal to the adjacent integers.
the opposite for a valley. Given an array of ints, sort it into an alternating sequence of peaks and valleys.
'''

def peakSort(arr):
    for i in range(1, len(arr), 2):
        # make sure indices don't go out of bounds
        if arr[i] < arr[i-1] or arr[i] < arr[i+1]:
            if arr[i-1] > arr[i+1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
            else:
                arr[i], arr[i+1] = arr[i+1], arr[i]

if __name__ == "__main__":
    arr = [5, 3, 1, 2, 3, 4]
    print(arr)
    peakSort(arr)
    print(arr)
