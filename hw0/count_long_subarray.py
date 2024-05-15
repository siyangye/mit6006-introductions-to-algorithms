'''
An increasing subarray of an integer array is any consecutive sequence of ar-
ray integers whose values strictly increase. Write Python function count long subarrays(A)
which accepts Python Tuple A = (a0 , a1 , . . . , an−1 ) of n > 0 positive integers, and returns the
number of longest increasing subarrays of A, i.e., the number of increasing subarrays with length at
least as large as every other increasing subarray. For example, if A = (1,3,4,2,7,5,6,9,8),
your program should return 2 since the maximum length of any increasing subarray of A is three
and there are two increasing subarrays with that length: speciﬁcally, subarrays (1,3,4) and
(5,6,9). You can download a code template containing some test cases from the website.
'''
def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    max_len = 0
    curr_len = 1
    for i in range(len(A)-1):
        if A[i+1] > A[i]:
            curr_len += 1 
        else: #new start of another sub array
            if max_len < curr_len:
                max_len = curr_len
                count = 1
            elif max_len == curr_len:
                count += 1
            curr_len = 1 #update the curr_len,last curr_len didn't get compared. 
    # final check: the last subarray if it is a max:
    if max_len == curr_len:
        count += 1 
    elif curr_len > max_len:
        count = 1 

    return count

test_cases = [
    ((1, 2, 3, 1, 2), 1), # (1, 2, 3) is the longest increasing subarray, appears once
    ((1, 3, 5, 2, 4, 6, 1), 2), # (1, 3, 5) and (2, 4, 6) are the longest, each appears once
    ((1,), 1), # Single element is trivially the longest
    ((1, 2, 3, 4, 5), 1), # The whole array is increasing
    ((5, 4, 3, 2, 1), 5), # Each element is an increasing subarray of length 1
    ((1, 2, 1, 2, 1, 2), 3), # Three increasing subarrays of length 2
    (
        (2, 2, 4, 1, 4),
        2,
    ),
    (
        (7, 8, 5, 7, 7, 3, 2, 8),
        3,
    ),
    (
        (7, 7, 9, 1, 2, 11, 9, 6, 2, 8, 9),
        2,
    ),
    (
        (4, 18, 10, 8, 13, 16, 18, 1, 9, 6, 11, 13, 12, 5, 7, 17, 13, 3),
        1,
    ),
    (
        (11, 16, 10, 19, 20, 18, 3, 19, 2, 1, 8, 17, 7, 13, 1, 11, 1, 18, 19, 9, 7, 19, 24, 2, 12),
        4,
    ),
]

# Running the test cases
for i, (input_data, expected_output) in enumerate(test_cases):
    result = count_long_subarray(input_data)
    print(f"Test case {i+1}: {'Passed' if result == expected_output else 'Failed'} (Output: {result}, Expected: {expected_output})")
