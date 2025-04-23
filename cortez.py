data = 4, 6, 7, 3, 6, True, 5.6, "Hello"
#data[0] = 5 - no
print(data[1:8:2])

#print(data.count(6))
#print(len(data))
print(data)

for el in data:
    print(el)

nums = [5, 7, 8]

new_data = tuple(nums)
word = tuple("Hello world")
print(new_data, word)