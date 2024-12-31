def mutate_string(string, position, character):
    
    sl = [c for c in string]
    sl[position] = character
    new_str = "".join(sl)
    return new_str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)