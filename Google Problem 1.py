array = [1, 11, 3, 7, 2, 6, 5, 10, 4]

sum = 12

for i in range(len(array)):
    temp_sum = 0
    for k in range (i, len(array)):
        temp_sum += array[k]
        if temp_sum == sum:
            print("Starting: {} Ending: {}".format(i, k))
            break
        elif temp_sum > sum:
            break