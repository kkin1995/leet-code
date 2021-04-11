def maximumWealth(accounts):
    """
    You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

    A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
    """
    no_of_customers = len(accounts)
    no_of_banks = len(accounts[0])
    maxWealth = 0
    for i in range(no_of_customers):
        wealth = 0
        for j in range(no_of_banks):
            wealth += accounts[i][j]
        if wealth > maxWealth:
            maxWealth = wealth
    return maxWealth

if __name__ == "__main__":
    test_accounts = [[1,2,3],[3,2,1]]
    test_max_wealth = 6
    if test_max_wealth == maximumWealth(test_accounts):
        print("Test Case Passed")
    else:
        print("Test Case Failed")