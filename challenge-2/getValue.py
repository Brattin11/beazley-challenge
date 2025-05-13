startData = {"a": {"b": {"c": 1}}, "d": {"e": 3}}

def getVal(obj, target):
    if target in obj:
        return obj[target]
    
    for key, val in obj.items():
        if not isinstance(val, dict) and key != target:
            return None
        
        result = getVal(val, target)
        if result is not None:
            return result


print(getVal(startData, "c"))


