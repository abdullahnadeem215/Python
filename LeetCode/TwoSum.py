class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        found = False
        for i in range(len(nums)):
            for m in range(i+1,len(nums)):
                 if (nums[i]+nums[m]==target):
                    result.append(i)
                    result.append(m)
                    found = True
                    break
            if found==True:
                break

        return result