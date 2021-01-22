from functools import reduce
someVariable = [1, 2, 3]
result = reduce(lambda value1, value2: value1+value2, someVariable)
print(result)