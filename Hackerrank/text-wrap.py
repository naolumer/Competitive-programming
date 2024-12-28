def wrap(string, max_width):
    answer = []
    for i in range(0, len(string), max_width):
        answer.append(string[i:i+max_width])
    return "\n".join(answer)