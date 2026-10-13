# Time Complexity O(n)
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        set_nums = set(nums)
        longest_subs = 0
        for n in set_nums:
            if (n-1) not in set_nums:
                count = 0
                while(n+count) in set_nums:
                    count+=1
                longest_subs = max(longest_subs, count)

        return longest_subs

# Time Complexity: O(n log n)
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        sorted_nums = sorted(set(nums))
        longest_subsequent_list = []
        count = 0
        prev = 0
        nextv = 0

        for i in range(len(sorted_nums)):
            nextv = sorted_nums[i]
            if nextv-1 == prev:
                prev = nextv
                count += 1
            elif nextv == prev:
                longest_subsequent_list.append(count)
                prev = nextv
                count = 1
            else:
                longest_subsequent_list.append(count)
                prev = nextv
                count = 1
        longest_subsequent_list.append(count)
        return max(longest_subsequent_list)
        
