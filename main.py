#16-misol
roy = ["10", "20", "30"]
print(roy)

res = list(map(lambda x: int(x) + 10, roy ))
print(res)

#17-misol
roy = [9, 16, 25]
print(roy)

res = list(map(lambda x: x // 3, roy))
print(res)

#18-misol
roy = ["olma", "anor", "uzum"]
print(roy)

res = list(map(lambda x: x[0], roy))
print(res)

#19-misol
roy = [11, 22, 33, 44]
print(roy)

res = list(map(lambda x: str(x), roy))
print(res)

#20-misol
roy = ["python", "map", "function"]
print(roy)

res = list(map(lambda x: x * 2, roy))
print(res)
