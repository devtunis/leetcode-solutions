from collections import Counter
 

word = "fefefef"
collect =""
List = []
f = Counter(word)
 
 
for i in range(len(word)):
    collect = ""
    j  = i
    test = True
    while j <len(word)-1 and test:
        if word[j]!=word[j+1] and word[j] not in collect:
            collect=collect+word[j]
        else:
            test= False
        j=j+1
    if(collect!=" " ):
        List.append(collect)
print(len(max(List)))   
  
  
 

 
 
        
    
    
    
    
     
   