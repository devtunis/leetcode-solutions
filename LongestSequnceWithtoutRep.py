nums =[0,0,0,0,0,1,2,3,4,5,6,7,7,7,7,7,8,9,10,11,12,13 ,101,102,102,104,105,106,107,108,109,110,111,112,113,114]
def LongestSequnceWithtoutRep(nums):
    L = 0
    R = L+1
    LongestSequnce = 0
 
    nums = set(nums)
    nums = list(nums)
    
    
    for i in range(len(nums)-1):
        
       
      
        if (abs(nums[R]-nums[R-1])>1):
            LongestSequnce  = max(LongestSequnce,len(nums[L:R]))
            
         
            L =R
            R =L+1
           
        else:
            
            lastIndex = R
            R = R+1
           
       
  
    
 
 
    return {"max":max(LongestSequnce,len(nums[L:R]))}
print("max LongestSequnceWithtoutRep",LongestSequnceWithtoutRep(nums)) 


