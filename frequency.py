#check the frequency of a vale in a dictionary
    #create a dictionary
my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 6
              }
    #ask the user for a value
value = int(input("Enter a value: "))
    #check the frequency of the value
count = 0
for key in my_dict:
        if my_dict[key] == value:
            count += 1
    #show the result
print("The value", value, "appears", count, "times in the dictionary")