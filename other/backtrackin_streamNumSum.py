# Add the mathematical operators + or - before any of the digits in the decimal numeric string 123456789 such that the resulting 
# mathematical expression adds up to 100. Return all possible solutions.

# #1+2+3-4+5+6+78+9
# 1+2+34-5+67-8+9
# 1+23-4+5+6+78-9
# 1+23-4+56+7+8+9
# 1+2-3+4+5+6+78+9
# 12+3+4+5-6-7+89
# 12+3-4+5+67+8+9
# 12-3-4+5-6+7+89
# 123+4-5+67-89
# 123-4-5-6-7+8-9
# 123+45-67+8-9
# 123-45-67+89

def findGoal(goal, stringN, results, currentS, path):
    
    if goal == currentS and len(stringN) == 0:
        path = path[1:]
        results.append(path)
        
    
    for i in range(len(stringN)):
        findGoal(goal, stringN[i+1: ], results, currentS + int( stringN[:i+1] ), path+"+"+stringN[:i+1] )
        findGoal(goal, stringN[i+1: ], results, currentS - int( stringN[:i+1] ), path+"-"+stringN[:i+1] )
    return results
                
        
results = findGoal(100, "123456789", [], 0,"")

for l in results:
    print(l)
        
