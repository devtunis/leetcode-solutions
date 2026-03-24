def avg_subarrays(arr, k):
    window_sum = sum(arr[:k])
    result = [window_sum / k]

    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        result.append(window_sum / k)

    return result

print(avg_subarrays([1,3,2,6,-1,4,1,8,2], 5))
