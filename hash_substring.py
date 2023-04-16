# python3

def read_input():
    # this function needs to acquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f(input from file) to choose which input type will follow
    input_choice = input().strip()
    if input_choice == "F":
        filename = input().strip()
        with open(filename) as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    else:
        pattern = input().strip()
        text = input().strip()
    return pattern, text

    # after input type choise
    # read two lines
    # first line is pattern
    # second line is text in which to look for pattern

    # return both lines in one return

    # this is the sample return, notice the rstrip function
    

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp algoritm
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
    # and return an iterable variable


# this part launches the function
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))