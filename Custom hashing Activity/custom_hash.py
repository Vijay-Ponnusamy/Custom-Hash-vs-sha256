import hashlib

def custom_hash(input_str):
    HASH_LENGTH = 32
    MODULO = 97
    ascii_vals = [(ord(char) * (i + 1)) % MODULO for i, char in enumerate(input_str)]
    hash_nums = []
    for i in range(HASH_LENGTH):
        total = 0
        for j in range(i, len(ascii_vals), HASH_LENGTH):
            total += ascii_vals[j]
        hash_nums.append(total % 256)
    final_hash = ''.join(f'{val:02x}' for val in hash_nums)[:HASH_LENGTH]
    return final_hash

def sha256_hash(input_str):
    return hashlib.sha256(input_str.encode()).hexdigest()

test_cases = [
    "",
    "hello",
    "Hello",
    "sample",
    "Sample123",
    "This is a longer input string for testing",
]

print(f"{'Input':<40}{'Custom Hash':<40}{'SHA-256 (first 32 chars)'}")
print("-" * 110)
for text in test_cases:
    print(f"{text:<40}{custom_hash(text):<40}{sha256_hash(text)[:32]}")
