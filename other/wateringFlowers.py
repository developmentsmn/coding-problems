#Two friends watering a garden of flowers

# [3,4,2]
    
# c1:2
# c2:3



def friendsWatering(flowers, capacity1:int, capacity2:int) -> int:
    
    counterR =1
    counterL =1
    
    indexR = 0
    indexL = (len(flowers)-1)
    
    c1 = capacity1
    c2 = capacity2
    
    while( indexR <= indexL):
        
        requiredR = flowers[indexR]
        requiredL = flowers[indexL]
        
        if indexR == indexL:
            
            if (capacity1+capacity2) < requiredR:
                counterR+=1
        else:
            
            if requiredR > capacity1:
                capacity1 = c1
                counterR+=1
            
            if requiredL > capacity2:
                capacity2 = c2
                counterL+=1
            
            capacity1 = capacity1 - requiredR
            capacity2 = capacity2 - requiredL
        
        indexR+=1
        indexL-=1
            
            
    return counterR+counterL
        
        
    
    
    