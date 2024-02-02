def numIdenticalPairs(nums):
    frequency_dict = {}
    good = 0

    for num in nums:
        if num in frequency_dict:
            good += frequency_dict[num]
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    return good

# Test cases
print(numIdenticalPairs([1,2,3,1,1,3]))
print(numIdenticalPairs([1,1,1,1]))
print(numIdenticalPairs([1,2,3]))
