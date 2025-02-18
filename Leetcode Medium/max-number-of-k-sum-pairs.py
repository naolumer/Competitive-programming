class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        lp= 0
        rp =len(nums)-1

        result =0 

        while lp<rp:
            p_sum = nums[lp] + nums[rp]

            if p_sum<k:
                lp+=1
            elif p_sum>k:
                rp-=1
            else:
                result+=1
                lp+=1
                rp-=1
        return result