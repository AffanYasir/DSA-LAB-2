
arr = [1, 2, 3, 4, 5]
steps = 2

def rotate_array(arr, steps):
    steps %= len(arr)
    return arr[-steps:] + arr[:-steps]

print("Output(Rotated array):", rotate_array(arr, steps))
