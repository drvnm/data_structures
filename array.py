data = [2200, 2350, 2600, 2130, 2190,]
feb = data[1] - data[0]
print("feb:", feb)
first_quarter = data[0] + data[1] + data[2]
print("first_quarter:", first_quarter)
print("2000" if 2000 in data else "You didnt spend 2000")
data.append(1980)
print("nieuwe data:", data)
data[3] = data[3] - 200
print("nieuwe data:", data)


########################### 2
print('\n2')
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
print("length of list:", len(heros))
heros.append('black panther')
del(heros[-1])
heros.insert(2, 'black panther') 
print(heros)


########################### 3
ordered_nums = [i for i in range(1000) if i % 2 == 0]
print(ordered_nums)