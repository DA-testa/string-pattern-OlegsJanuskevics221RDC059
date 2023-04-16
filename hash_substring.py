# python3

def read_input():
    pattern = input().rstrip()
    text = input().rstrip() 
    return pattern,text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    positions = []
    p_len = len(pattern)
    t_len = len(text)

    p_hash = 0
    for i in range(p_len):
        p_hash = p_hash + ord(pattern[i]) * pow(10,p_len-i-1)

    t_hash = 0
    for i in range(p_len):
        t_hash = t_hash + ord(text[i]) * pow(10,p_len-i-1)
    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:
            if pattern == text[i:i+p_len]:
                positions.append(i)
        if i < t_len - p_len:
            t_hash = (t_hash - ord(text[i]) * pow(10,p_len-1)) *10 +ord(text[i+p_len])
            return positions


if __name__ == '__main__':
    pattern,text = read_input()
    occurrences = get_occurrences(pattern,text)
    print_occurrences(occurrences)

