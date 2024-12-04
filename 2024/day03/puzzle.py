with open('input.txt', 'r') as input:
    content = input.read()

result = 0
cleaned_content = []
enabled = 1
for i in range(len(content)-6):
    if content[i] + content[i+1] + content[i+2] + content[i+3]== 'do()':
        enabled = 1
    elif content[i] + content[i+1] + content[i+2] + content[i+3] + content[i+4] + content[i+5] + content[i+6] == "don't()":
        enabled = 0
    
    if content[i]+content[i+1]+content[i+2]+content[i+3] == 'mul(' and enabled == 1:
        for y in range(15):
            if content[i+y] == ')':
                cleaned_content.append(content[i:i+y+1])
                break
    else:
        pass

for instruction in cleaned_content:
    instruction = instruction.strip('mul()').split(',')
    if len(instruction) == 2:
        num1 = instruction[0].isdigit()
        num2 = instruction[1].isdigit()
        if num1 and num2:
            result += int(instruction[0]) * int(instruction[1])
