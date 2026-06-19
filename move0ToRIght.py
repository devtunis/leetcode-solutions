t = [0,1,0,3,1,1,2,0]

k =0 
for i in range(len(t)):
   
    if t[i] != 0:
        t[i],t[k]  = t[k],t[i]
        k = k+1
print(t)
