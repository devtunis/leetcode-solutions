package main
import "fmt"

func main() {
    Set := make(map[int]int)
    nums := [...]int{2,7,11,15}
    target := 9
    for i:=0;i<len(nums);i++ {
         current := target -nums[i]
         value,exist := Set[current]
         if(exist){
             fmt.Println(current , value)
            
             break
         }
         Set[nums[i]] = current
          
    }
 

 
   
  
}

// best Solution  

func twoSum(nums []int, target int) []int {
	seen := make(map[int]int)

	for i, num := range nums {
		if j, ok := seen[num]; ok {
			return []int{j, i}
		}
		seen[target-num] = i
	}

	return []int{}
}

