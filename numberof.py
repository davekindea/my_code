class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        y=[]
        for i in range (len(nums)):
            x=0
            for j in range (len(nums)):
                if nums[i]>nums[j]:
                    x+=1
                else:
                    continue
            y.append(x)
            
        return y
