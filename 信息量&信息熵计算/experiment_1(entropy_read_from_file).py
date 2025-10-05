import math

def calculate_entropy(probabilities):
    entropy = 0
    for probability in probabilities.values():
        entropy += probability * calculate_information(probability)
    return entropy

def calculate_information(probability):
    if probability < 0 or probability > 1:
        raise ValueError("Probability must be between 0 and 1")
    elif probability == 0:
        return float('infinity')
    elif probability == 1:
        return 0
    else:
        return -math.log2(probability)

def read_probabilities_from_file(file_path):
    probabilities = {}
    with open(file_path, 'r') as file:
        for line in file:
            char, prob = line.strip().split(':')
            probabilities[char.strip()] = float(prob.strip())
    return probabilities

file_path = 'english_char_probabilities.txt' 
probabilities = read_probabilities_from_file(file_path)
entropy = calculate_entropy(probabilities)
print("Entropy:", entropy)
