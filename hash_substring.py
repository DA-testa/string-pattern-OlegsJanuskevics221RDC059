# python3

import sys

def rabin_karp(pattern, text):
    p_len = len(pattern)
    t_len = len(text)
    p_hash = hash(pattern)
    t_hashes = [hash(text[i:i+p_len]) for i in range(t_len-p_len+1)]
    res = []
    for i in range(t_len-p_len+1):
        if p_hash == t_hashes[i]:
            if text[i:i+p_len] == pattern:
                res.append(i)
    return res

def main():
    input_choice = input().strip()
    if input_choice == "F":
        filename = input().strip()
        with open(filename) as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    else:
        pattern = input().strip()
        text = input().strip()
    res = rabin_karp(pattern, text)
    for i in res:
        print(i, end=" ")

if __name__ == "__main__":
    main()
