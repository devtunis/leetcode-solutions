t = [4,3,2,1]

for i in range(1,len(t)):
    key = t[i]
    
    j = i
    while j>0 and t[j-1]>key:
        t[j]  = t[j-1]
        j-=1
    t[j] = key
print(t)
