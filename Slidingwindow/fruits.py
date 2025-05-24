def totalFruit(fruits):
    hash_map = {}
    left = 0
    max_fruits = 0
    temp = 0

    for right in range(len(fruits)):
        fruit = fruits[right]
        if fruit in hash_map:
            hash_map[fruit] += 1
        else:
            hash_map[fruit] = 1
        temp += 1

        while len(hash_map) > 2:
            left_fruit = fruits[left]
            hash_map[left_fruit] -= 1
            if hash_map[left_fruit] == 0:
                del hash_map[left_fruit]
            temp -= 1
            left += 1

        if temp > max_fruits:
            max_fruits = temp

    return max_fruits

fruits = [1, 2, 1, 2, 3]
print(totalFruit(fruits))  
