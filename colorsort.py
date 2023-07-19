class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)-1):
            for j in range (i+1,len(nums)):
                x=nums[i]
                y=nums[j]
                if nums[i]>nums[j]:
                    nums[i]=y
                    nums[j]=x
                else:
                    continue
        return nums
