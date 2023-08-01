class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        a=[]
        for i in range (len(r)):
            z=[]
            for j in range(l[i],r[i]+1):
                z.append(nums[j])
            z.sort()
            x=z[1]-z[0]
            for k in range (1,len(z)):
                y=z[k]-z[k-1]
                if y==x:
                    if k==len(z)-1:
                        a.append(True)
                        break
                    else:
                        continue
                else:
                    a.append(False)
                    break
        return a
                    
                
                
            
        
