def maxPrice(self, prices):

    minPrice = prices[0]
    maxProfit = 0

    for i in range(len(prices)):

        curPrice = prices[i]

        if curPrice < minPrice:
            minPrice = curPrice
        
        potential_profit = curPrice - minPrice

        if potential_profit > maxProfit:
            maxProfit = potential_profit

        return maxProfit