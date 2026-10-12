import math
import copy
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        final_arry = []
        result = 1
        count_zeros = 0
        for i in nums:
            if i == 0:
                count_zeros +=1
            else:
                result *= i
        if count_zeros > 1:
            for i in range(len(nums)):
                final_arry.append(0)
        elif count_zeros == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    final_arry.append(result)
                else:
                    final_arry.append(0)
        else:
            for i in range(len(nums)):
                final_arry.append(int(result/nums[i]))
        return final_arry
