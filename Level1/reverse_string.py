    # to reverse string there are many possible way let me show using two ways 

# the first one using string operation [::-1]
def reverse_string(word):
    return word[::-1]

word = 'Abel'
print(reverse_string(word)) # output = "lebA"

# the second method is 
    # converting the give string into list 
    # using two pointer reverse the the string  
    # and finally join the list 

def method_two(word):
    # convert the given string into list 
    toReverse = list(word)

    # two pointer which start form starting and ending the list 
    left, right = 0 , len(word)-1

    # until the give pointer reach in the middle update their value
    while left < right:

        # swap 
        toReverse[left], toReverse[right] = toReverse[right], toReverse[left]
        left, right = left+1 , right -1
    
    # finally return the reversed list 
    return ''.join(toReverse)

word = 'Test the function'
print(method_two(word)) # output = "noitcnuf eht tseT"
