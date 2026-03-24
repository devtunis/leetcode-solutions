nums =[1,2,3,4,5,6,9,10,11,0,1,2,3,4,5,6,7,100,101,102,103,104,105,106,107,108]
def longestSequence(nums):
    L = 0
    R = L+1
    longestSequence = 0
    for i in range(len(nums)-1):
      
        if (abs(nums[R]-nums[R-1])>1):
            longestSequence  = max(longestSequence,len(nums[L:R]))
            
            L =R
            R =L+1
           
        else:
           
            R = R+1
  
    
 
 
    return max(longestSequence,len(nums[L:R]))
print("max longestSeuqnce",longestSequence(nums)) 


