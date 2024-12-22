def checkIfExists(nums):
    seen_set = set()

    for num in nums:
        if num*2 in seen_set or (num%2==0 and num//2 in seen_set):
            return True
        seen_set.add(num)
    return False
