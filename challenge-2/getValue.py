"""
getValue.py

You have a nested object, create a function that allows for the nested object and a key and returns the value of
key.
"""

startData = {"a": {"b": {"c": 1}, "e": 5}, "f": {"g": {"h": 4}, "i": 3}}

def getVal(obj, target):
    if target in obj:
        return obj[target]
    
    for key, val in obj.items():
        # handles nested dicitonaries with top level neighbors i.e. {a: {<...>}, b: {<...>}}
        # if path ends with non-dictionary item and we haven't yet found the key, abandon this path.
        if not isinstance(val, dict) and key != target:
            return None
        result = getVal(val, target)

        if result is not None:
            return result

print(getVal(startData, "h"))



