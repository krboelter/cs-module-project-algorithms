'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    moved = []
    zero = []
    for i in arr:
        if i is not 0:
            moved.append(i)
        else:
            zero.append(i)

    print(moved + zero)
    return moved + zero


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
