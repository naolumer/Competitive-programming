class Solution:
    def myPow(self,x,n):

        #   Recursive solution

        # if not n:
        #     return 1
        # if n<0:
        #     return 1/self.myPow(x,-n)
        
        # if n%2:     #checking if the exponent is odd
        #     return x *self.myPow(x,n-1)
        # return self.myPow(x*x,n/2)
    
    
        # Iterative Solution

        
        if n < 0:
            n = -n
            x= 1/x
        
        poww = 1

        while n:
            if n%2:
                poww*=x
            x*=x
            n//=2
        return poww
res = Solution()
print(res.myPow(4,3))
                
        

