def divide_arr(arr):
    if len(arr) < 2:
        print(f"Base condition reached with {arr}")
        return arr[:]
    else:
        middle = len(arr)//2
        print("Current list to work with:", arr)
        print("Left split:", arr[:middle])
        print("Right split:", arr[middle:])
        l1 = divide_arr(arr[:middle])
        l2 = divide_arr(arr[middle:])
        # implied return None

l = [8, 6, 2, 5]
divide_arr(l)
