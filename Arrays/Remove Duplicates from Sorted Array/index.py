class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        currelement = 0
        for inx in range(1, len(nums)):
            if nums[currelement] == nums[inx]:
                pass
            else:
                currelement += 1
                nums[currelement], nums[inx] = nums[inx], nums[currelement]
        return currelement+1
