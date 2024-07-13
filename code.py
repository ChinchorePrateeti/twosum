def twoSum(nums, target):

    #initalize an emplty dict
    numHolder ={}

    #use a loop to loop over every element in nums list and retain index
    for index in range(len(nums)):

        #find complement of first number to make the target number
        complement_number = target - nums[index]

        #check if this complement exists in a new dict, if yes return its index along with currnet index
        if complement_number in numHolder:
            return [numHolder[complement_number],index]

        numHolder[nums[index]] = index

    return []


nums = [2, 7, 11, 15]
target = 9
call_twoSum = twoSum(nums, target)
print(call_twoSum)