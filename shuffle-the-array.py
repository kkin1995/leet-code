def shuffle(nums, n):
    """
    Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

    Return the array in the form [x1,y1,x2,y2,...,xn,yn].
    """
    xs = nums[0:n]
    ys = nums[n:]
    shuffled_array = []
    for i in range(n):
        shuffled_array.extend((xs[i], ys[i]))
    return shuffled_array

if __name__ == "__main__":
    test_nums = [2,5,1,3,4,7]
    test_shuffled_array = [2, 3, 5, 4, 1, 7]
    test_n = 3
    if test_shuffled_array == shuffle(test_nums, test_n):
        print("Test Case Passed")
    else:
        print("Test Case Failed")