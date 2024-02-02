def getConcatenation(nums):
    n = len(nums)
    len_ans = 2*n
    ans = [0] * len_ans
    for i in range(0, n):
        ans[i] = nums[i]
        ans[i + n] = nums[i]
    return ans

print(getConcatenation([1,2,1]))