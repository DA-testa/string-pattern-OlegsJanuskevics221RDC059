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

    p_hash = 0
    for i in range(p_len):
        p_hash += ord(pattern[i]) * pow(10, p_len-i-1)

    t_hash = 0
    for i in range(p_len):
        t_hash += ord(text[i]) * pow(10, p_len-i-1)

    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:
            if pattern == text[i:i+p_len]:
                positions.append(i)
        
        if i < t_len - p_len:
            t_hash = (t_hash - ord(text[i]) * pow(10, p_len-1)) * 10 + ord(text[i+p_len])

    return positions

if __name__ == '__main__':
    text_type = input().strip().upper()
    if "F" in text_type:
        filename = input().strip()
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
        try:
    filename = input().strip()
    except EOFError:
        print("No input provided.")
        sys.exit()
    
    occurrences = get_occurrences(pattern, text)
    print_occurrences(occurrences)
