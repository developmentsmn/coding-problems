
def returnUnique(s):

    setV = set()

    for c in s:
        if c not in setV:
            setV.add(c)
            
    return str(setV)


s = "111223444119"

print(returnUnique(s))