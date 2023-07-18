class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        a=[]
        for i in range (len(nums)):
            for j in range (i+1,len(nums)):
                x=nums[i]
                y=nums[j]
                if nums[i]>nums[j]:
                    nums[i]=y
                    nums[j]=x
                else:
                    continue
        for k in range (len(nums)):
            if nums[k]==target:
                a.append(k)
            else:
                continue
        return a
                
