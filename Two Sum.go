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
