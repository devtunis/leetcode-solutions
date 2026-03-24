def maxSum(arr, k):
    window_sum = sum(arr[:k])
    maxSum = window_sum

    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        maxSum   = max(maxSum,window_sum)

    return maxSum

print(maxSum([1,2,10,11], 2))
