# This file was created by John B.

n = -3
list = ["John", "Bread", "Eraserhead"]
dict = {
    "1": "John",
    "2": "Bread",
    "3": "Eraserhead"
}
while n < 0:
    print(list[n])
    n +=1

for i in range(len(list)):
    print(list[i])

for i in dict:
    print(dict[i])