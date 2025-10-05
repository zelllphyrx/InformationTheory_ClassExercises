def calculate_char_frequency(file_path):
    char_frequency = {}
    total_chars = 0

    # 读取文件并统计每个字符的出现频率
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            for char in line:
                if char.isalnum():  # 只考虑字母和数字字符
                    char_frequency[char] = char_frequency.get(char, 0) + 1
                    total_chars += 1

    # 计算每个中文字符的概率
    char_probabilities = {}
    for char, frequency in char_frequency.items():
        char_probabilities[char] = frequency / total_chars

    return char_probabilities

def save_probabilities_to_file(char_probabilities, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for char, probability in char_probabilities.items():
            file.write(f"{char}: {probability}\n")

file_path = 'D:\Information Theory\Chinese text.txt'  # 文件路径
output_file = 'chinese_char_probabilities.txt'

char_probabilities = calculate_char_frequency(file_path)
save_probabilities_to_file(char_probabilities, output_file)