class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=[0]*len(nums)
    
        for i in range(n):
            x[i*2]=nums[i]
            x[i*2+1]=nums[i+n]
            
        return x
        
