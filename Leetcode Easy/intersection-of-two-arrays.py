from collections import Counter

def intersection(nums1,nums2):
    count1= Counter(nums1)
    count2 = Counter(nums2)
    answer = []
    for key,freq in count1.items():
        if key in count2:
            answer.append(key)
    return answer