import math

# 定义计算自信息量的函数
def calculate_information(probability):
    if probability < 0 or probability > 1:
        raise ValueError("Probability must be between 0 and 1")
    elif probability == 0:
        return float('infinity')  # 返回无穷大
    elif probability == 1:
        return 0  # 返回0
    else:
        return -math.log2(probability)

# 定义接收输入的函数
def input_probabilities():
    probabilities = {}
    n = int(input("Enter the number of events: "))
    for i in range(n):
        event = input(f"Enter event {i+1}: ")
        probability = float(input(f"Enter probability for event {event}: "))
        if probability < 0 or probability > 1:
            raise ValueError("Probability must be between 0 and 1")
        probabilities[event] = probability
    return probabilities

# 主函数 计算自信息量并输出
probabilities = input_probabilities()

for event, probability in probabilities.items():
    information = calculate_information(probability)
    print(f"Information for event {event}: {information}")
