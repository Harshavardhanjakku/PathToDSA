l = list(map(int, input("Enter the list: ").split()))
if len(l) < 2:
    print("Second largest does not exist.")
else:
    largest = second_largest = float('-inf')
    for num in l:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        print("All elements are the same. Second largest does not exist.")
    else:
        print("Second largest:", second_largest)
