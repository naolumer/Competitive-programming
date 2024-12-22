from collections import Counter
def containsDuplicate(nums):
    count = Counter(nums)

    for key,freq in count.items():
        if freq >= 2:
            return True
    return False