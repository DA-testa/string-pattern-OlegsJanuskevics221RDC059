# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    pattern = input().rstrip()
    text = input().rstrip() 
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return pattern,text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
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
    # and return an iterable variable
    return positions


# this part launches the functions
if __name__ == '__main__':
    pattern,text = read_input()
    occurrences = get_occurrences(pattern,text)
    print_occurrences(occurrences)

