nums = [2, 7, 11, 15]
target = 9


def Two_sum(nums, target):
    outputline = []
    for x in range(0, len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] + nums[y] == target:
                outputline.append(x)
                outputline.append(y)
    return outputline


print(Two_sum(nums, target))


#==========================================================================================================

def Two_sum2(nums, target):
    dic = {}
    for index, values in enumerate(nums):
        difference = target - values
        if difference in dic:
            return [dic[difference], index]
        dic[values] = index


print(Two_sum2(nums, target))

#enumerate makes the list of values to index and values in the for loop.
