matches = [
           [1,3],[2,3],[3,6],
           [5,6],[5,7],[4,5],
           [4,8],[4,9],[10,4],
           [10,9]
           ]
def Solution(matches:list)->list:
    no_losess = set()
    Losess_one = {}
    for item in matches:
        R  = item[0]
        L  = item[1]
        
        if R not in Losess_one :
            no_losess.add(R)
        
        if  L in Losess_one:
            Losess_one[L]+=1
        else:
            Losess_one[L]=1
        if L   in  no_losess:
            no_losess.remove(L)
    
 
    return  sorted(list(no_losess)),sorted([k for k, v in Losess_one.items() if v == 1])
        
print(Solution(matches))