from collections import Counter
import math

def arithmetic_encode(data, freq):
    low = 0.0
    high = 1.0
    total = sum(freq.values())
    cumulative_freq = {}
    cumulative = 0.0
    
    for char, f in freq.items():
        cumulative_freq[char] = cumulative / total
        cumulative += f
    
    for char in data:
        range_width = high - low
        high = low + range_width * (cumulative_freq[char] + freq[char] / total)
        low = low + range_width * cumulative_freq[char]
    
    return (low + high) / 2

# Example usage
data = "example text to encode"
freq = Counter(data)
encoded_value = arithmetic_encode(data, freq)
encoded_length = math.ceil(-math.log2(encoded_value))
print("Arithmetic Encoded Value:", encoded_value)
print("Arithmetic Encoded Length:", encoded_length, "bits")