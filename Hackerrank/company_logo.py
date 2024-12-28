from collections import Counter
s = "aabbbccde"
count = Counter(s)

sorted_counter = sorted(count.items(),key=lambda x:(-x[1],x[0]))
for key,val in sorted_counter[:3]:
    print(key,val)




