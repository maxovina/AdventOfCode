from pprint import pprint

content = []
with open('input.txt', 'r') as input:
    for line in input:
        numbers = [int(num) for num in line.strip().split()]
        content.append(numbers)

result1 = 0
result2 = 0

#Puzzle1
for report in content:
    if all(report[i] <= report[i + 1] and (report[i + 1] - report[i] >= 1 and report[i + 1] - report[i] <= 3) for i in range(len(report) - 1)):
        result1 += 1
    elif all(report[i] >= report[i + 1] and (report[i] - report[i + 1] >= 1 and report[i] - report[i + 1] <= 3) for i in range(len(report) - 1)):
        result1 += 1
#Puzzle 2
    else:
        for i in range(len(report)):
            temp_report = report[:i] + report[i + 1:]
            if all(temp_report[i] <= temp_report[i + 1] and (temp_report[i + 1] - temp_report[i] >= 1 and temp_report[i + 1] - temp_report[i] <= 3) for i in range(len(temp_report) - 1)):
                result2 += 1
                break
            elif all(temp_report[i] >= temp_report[i + 1] and (temp_report[i] - temp_report[i + 1] >= 1 and temp_report[i] - temp_report[i + 1] <= 3) for i in range(len(temp_report) - 1)):
                result2 += 1
                break
result2+= result1


print(result1)
print(result2)

            

        

      