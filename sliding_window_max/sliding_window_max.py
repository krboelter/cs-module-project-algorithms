'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    tracker = 0
    new_l = []
    for i in range(len(nums)):
        if tracker + k - 1 < len(nums):
            temp = nums[tracker:tracker + k]
            new_l.append(max(temp))
            tracker += 1
    return new_l


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
