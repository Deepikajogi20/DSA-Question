class Solution(object):
    def pivotIndex(self,nums:List[int])->int:
      left=0
      right=0
      for i in range(0,len(nums)):
          left=sum(nums[:i])
          right=sum(nums[i+1:])
          if left==right:      
             return i
          i=i+1
      return -1
       
    
        
        
      
          
            
           
            
                
     
         
        
        