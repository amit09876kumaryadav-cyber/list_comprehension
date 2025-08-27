#write a python program to find the symmetric difference between two tuples
    #step 1: create two tuples
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
    #step 2: find the symmetric difference
symmetric_difference = tuple(set(tuple1) ^ set(tuple2))
    #step 3: show the result
print("The symmetric difference is:", symmetric_difference)