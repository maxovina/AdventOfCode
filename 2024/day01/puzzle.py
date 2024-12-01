with open('input.txt', 'r') as input:
    content = input.read().split()
    list1 = content[::2]
    list2 = content[1::2]
    
list1.sort()
list2.sort()
#Puzzle 1
distances1 = sum([int(list1[i]) - int(int(list2[i])) if list1[i] > list2[i] else int(list2[i]) - int(list1[i])  for i in range(len(list1))])
#Puzzle 2
distances2 = sum([int(i) * list2.count(i) for i in list1])

print(distances1)
print(distances2)