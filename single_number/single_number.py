'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    arr.sort()
    compareList = []

    if len(arr) == 0:
        return None

    for i, num in enumerate(arr): # if index is needed when running a four loop, enumerate()
        if num in compareList:
            compareList.remove(num)
        else:
            compareList.append(num)
    
    return compareList[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")