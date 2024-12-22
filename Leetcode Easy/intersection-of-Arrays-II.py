from collections import Counter

def intersectionII(nums1,nums2):
    count1 = Counter(nums1)
    count2 = Counter(nums2)
    answer = []
    for key,frq in count1.items():
        if key in count2:
            for i in range(min(frq,count2[key])):
                answer.append(key)

    return answer