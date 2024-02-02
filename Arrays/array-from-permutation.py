def buildArray(nums):
    ans = [0] * len(nums)
    for i in range(0, len(nums)):
        tmp = nums[i]
        ans[i] = nums[tmp]
    return ans 

print(buildArray([0,2,1,5,3,4]))