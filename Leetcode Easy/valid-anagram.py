from collections import Counter
def isAnagram(s, t):
      
        # freq_s= {}
        # freq_t={}
        # for char in s:
        #     if char in freq_s:
        #         freq_s[char]+=1
        #     else:
        #         freq_s[char]=1
        # for char in t:
        #     if char in freq_t:
        #         freq_t[char]+=1
        #     else:
        #         freq_t[char]=1
        # return freq_t==freq_s

        # BETTER SOLUTION

        count_t = Counter(t)
        count_s = Counter(s)

        if len(s)!=len(t):
                return False

        for key,frq in count_t.items():
                if not key in count_s or not count_s[key] == frq:
                        return False
        return True

print(isAnagram("car","rat"))
