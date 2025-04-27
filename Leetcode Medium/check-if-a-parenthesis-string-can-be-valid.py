class Solution:
    
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False

        open_ = []
        lock = []
        for i in range(len(s)):
            if locked[i] == '0':
                open_.append(i)
            elif s[i] == '(':
                lock.append(i)
            else:
                if lock:
                    lock.pop()
                elif open_:
                    open_.pop()
                else:
                    return False
        
        while open_ and lock and lock[-1] < open_[-1]:
            open_.pop()
            lock.pop()
        
        if lock or len(open_) % 2 == 1:
            return False

        return True