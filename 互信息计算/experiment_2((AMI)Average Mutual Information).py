import math
import jieba
from collections import defaultdict, Counter
import re

# 定义停用词列表
stop_words = set(["的", "了", "在", "是", "我", "有", "和", "就", "不", "人", "都", "一", "一个", "上", "也", "很", "到", "说", "要", "去", "你", "会", "着", "没有", "看", "好", "自己", "这"])

def process_text(text_file):
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()
        # 去除标点符号和空格
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\s+', '', text)
        # 分词，并去除停用词
        processed_text = [word for word in jieba.cut(text) if word.strip() and word not in stop_words]
    return processed_text

def calculate_pmi(word_counts, total_words, word1, word2, joint_counts):
    word1_count = word_counts[word1]  # 单词1的频数
    word2_count = word_counts[word2]  # 单词2的频数
    joint_count = joint_counts[(word1, word2)]  # 两个单词连在一起的频数

    p_word1 = word1_count / total_words  # 单词1的概率
    p_word2 = word2_count / total_words  # 单词2的概率
    p_joint = joint_count / total_words  # 两个单词同时出现的概率

    if p_joint == 0:  # 如果联合概率为0，则互信息为0
        return 0
    else:
        pmi = math.log2(p_joint / (p_word1 * p_word2))  # 计算互信息
        return pmi

def compute_average_mutual_information(file1, file2):
    # 处理两个文本文件
    text1 = process_text(file1)
    text2 = process_text(file2)
    
    # 合并两个文本的词汇
    combined_text = text1 + text2
    
    # 构建词典和联合频率计数
    word_counts = Counter(combined_text)
    joint_counts = defaultdict(int)

    for i in range(len(text1) - 1):
        joint_counts[(text1[i], text1[i+1])] += 1
    for i in range(len(text2) - 1):
        joint_counts[(text2[i], text2[i+1])] += 1

    total_words = len(combined_text)

    # 计算每两个相邻符号之间的互信息
    total_pmi = 0
    num_pairs = 0

    for (word1, word2), joint_count in joint_counts.items():
        pmi = calculate_pmi(word_counts, total_words, word1, word2, joint_counts)
        total_pmi += pmi
        num_pairs += 1

    # 计算平均互信息
    average_pmi = total_pmi / num_pairs if num_pairs != 0 else 0
    
    return average_pmi

# 文件路径
file1 = 'D:\\Information Theory\\Chinese text2（鲁迅 狂人日记）.txt'
file2 = 'D:\\Information Theory\\Chinese text3（朱自清 荷塘月色）.txt'

# 计算两个文本文件之间的平均互信息
average_pmi = compute_average_mutual_information(file1, file2)

# 输出平均互信息
print(f"两个文本文件之间的平均互信息: {average_pmi:.4f}")