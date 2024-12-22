def finalPrice(prices):

    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i]>=prices[j]:
                prices[i]=prices[i]-prices[j]
                break
            else:
                continue
    return prices

    # O(n) solution using stack

    
    # stack = []
    # n = len(prices)
    # answer = prices[:]

    # for i in range(n):
    #     while stack and prices[i] <= prices[stack[-1]]:
    #         j = stack.pop()
    #         answer[j] = prices[j] - prices[i]
    #     stack.append(i)
    # return answer
