def runningSum(nums):
    length_of_nums = len(nums)
    runningSum = []
    totalSum = 0
    for i in range(length_of_nums):
        totalSum += nums[i]
        runningSum.append(totalSum)
    return runningSum

if __name__ == "__main__":
    test_nums = [1, 2, 3, 4]
    test_runningSum = [1, 3, 6, 10]
    if test_runningSum == runningSum(test_nums):
        print("Test Case Passed")
    else:
        print("Test Case Failed")