# there are two ways 

    # the first way is by using "max" builtin fucntin 
example = [1,2,3,4,5,2999,3,4,5,67,7]
print(max(example)) # output = '2999'

    # the second  method is using for loop and conditions(if, elif ) 

def find_max_number(arr):
    # check if arr is empty or not
    if arr == []:
        return 'empty array'
    max_number = arr[0]

    # iterate through the array element and find number greather than max_number
        # update the max_number 
    for i in range(1,len(arr)):
        if arr[i] > max_number:
            max_number = arr[i]
    

    return max_number

example2 = [0, -3, 98, 199, 5, 20]
print(find_max_number(example2))