'''
Input: an integer
Returns: an integer
'''
from itertools import combinations

def eating_cookies(n):
    # Your code here
    counter = 0

    if n == 0:
        counter += 1
    
    if n >= 3:
        counter += eating_cookies(n-3)

    if n >= 2:
        counter += eating_cookies(n-2)

    if n >= 1:
        counter += eating_cookies(n-1)

    return counter


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
