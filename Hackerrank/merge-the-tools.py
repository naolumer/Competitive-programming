def merge_the_tools(string, k):
    n = len(string)
    lisst = []
    for i in range(0,n,k):
        lisst.append(string[i:i+k])
    unique_ord = []
    for s in lisst:
        temp = []
        for char in s:
            if not char in temp:
                temp.append(char)
        unique_ord.append(temp)
    for chunk in unique_ord:
        print("".join(chunk))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)