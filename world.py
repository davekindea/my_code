class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        x=int(len(nums)/2)
        nums.sort()
        sum=nums[start]+nums[end]
        for i in range(x):
            y=nums[start]+nums[end]
            if y>sum:
                sum=y
            start+=1
            end-=1
        return sum
