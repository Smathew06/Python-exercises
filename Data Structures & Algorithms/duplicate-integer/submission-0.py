class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check={}
        for i in range(len(nums)):
            check[nums[i]]= check.get(nums[i],0)+1
            if check[nums[i]]>1:
               return True

        return False

       
        
            
        