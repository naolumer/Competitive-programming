import collections
class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_diff = float("inf")
        d = collections.defaultdict(list)

        for i in range(len(arr) - 1):
            curr_diff = arr[i+1] - arr[i]
            d[curr_diff].append([arr[i], arr[i+1]])
            min_diff = min(min_diff, curr_diff)
        
        return d[min_diff]

# ans = Solution()
# print(ans.minimumAbsDifference([1,3,6,10,15]))
    
