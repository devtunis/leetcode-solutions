import time 
from math import*

map = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

start = {"x":0,"y":11}
end = {"x":0,"y":0}


def intialize():
    map[start["x"]][start["y"]] = "*"
    map[end["x"]][end["y"]] = "F"

intialize()

def Distance(x1,x2,y1,y2):
    dx = (x2-x1)
    dy = (y2-y1)
    
    return sqrt((dx**2) + (dy**2))

def HandelMinsetWay(o):
    minValue = {
        "way":"",
        "value":o["left"]
    }
    
   
    for key, value in o.items():
        if value <= minValue["value"]:
            minValue["value"] = value
            minValue["way"] = key
    
    print("——")
    return minValue 
      
    


def display():
    for i in range(len(map)):
        for j in range(len(map)):
            print(map[i][j],end="|")
        print()
display()


            
def loop():
    Continue = True 
    while Continue:
        Min = 0.0
        eyes = {}
        
        left = start["y"]-1
        right = start["y"]+1
        up = start["x"]-1
        down = start["x"]+1
        

        eyes["left"] = Distance(start["x"],end["x"],left,end["y"])
        eyes["right"] = Distance(start["x"],end["x"],right,end["y"])
        eyes["up"] = Distance(up, end["x"], start["y"], end["y"])
        eyes["down"] = Distance(down, end["x"], start["y"], end["y"])
        
       
  
  
 
       
        result = HandelMinsetWay(eyes)
        print(result)
        
        
        if (result["way"]=="right"): 
            map[start["x"]][start["y"]+1]="->"
            start["y"]+=1
        
        if (result["way"]=="up"): 
            map[start["x"]-1][start["y"]]="^"
            start["x"]-=1
            
            
        if (result["way"]=="down"): 
            map[start["x"]+1][start["y"]]="↓"
            start["x"]+=1
        
        if (result["way"]=="left"): 
            map[start["x"]][start["y"]-1]="<"
            start["y"]-=1
   
        
            
        if (result["value"]==0.0):
            map[end["x"]][end["y"]]="$"
            Continue = False
            
        
            
        display()
               
       
        
      
        time.sleep(0.2)


loop()

