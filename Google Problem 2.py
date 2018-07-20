array = [3,5,4,2]

max_diff = 0
starting = 0
ending = 0

for i in range(len(array)):
    temp_diff = 0
    j = i
    while j < len(array):
        if array[i] <= array[j]:
            temp_diff = j - i

            if temp_diff > max_diff:

                starting = i
                ending = j
                max_diff = ending - starting
        j += 1

if ending != starting:
    print("Maximum difference: {}".format(max_diff))
    print("Starting: {} Ending: {}".format(starting, ending))