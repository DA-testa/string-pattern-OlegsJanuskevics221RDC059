# python3

import sys

def read_input():
    pattern = input().rstrip()
    text = input().rstrip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    positions = []
    p_len = len(pattern)
    t_len = len(text)

    # Calculate the hash of the pattern
    p_hash = 0
    for i in range(p_len):
        p_hash += ord(pattern[i]) * pow(10, p_len-i-1)

    # Calculate the hash of the initial substring of length p_len in the text
    t_hash = 0
    for i in range(p_len):
        t_hash += ord(text[i]) * pow(10, p_len-i-1)

    for i in range(t_len - p_len + 1):
        # Check if the hashes match
        if p_hash == t_hash:
            # Check if the substrings match
            if pattern == text[i:i+p_len]:
                positions.append(i)
        
        # Recalculate the hash for the next substring in the text
        if i < t_len - p_len:
            t_hash = (t_hash - ord(text[i]) * pow(10, p_len-1)) * 10 + ord(text[i+p_len])

    return positions

if _name_ == '_main_':
    text_type = input("Enter I or F: ").upper()  # Modified to take input directly
    if "F" in text_type:
        filename = "06"
        file_path = f"./test/{filename}"
        try:
            with open(file_path) as f:
                pattern = f.readline().rstrip()
                text = f.readline().rstrip()
        except Exception as e:
            print("Error:", str(e))
            sys.exit()
    elif "I" in text_type:
        pattern, text = read_input()
    
    occurrences = get_occurrences(pattern, text)
    print_occurrences(occurrences)