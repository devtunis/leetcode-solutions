
let nums = [1,2,3,1] 
let f  = new Set()
let test  = true 
nums.forEach((item)=>  f.has(item)  ? console.log("Duplicate") : f.add(item) )
 
