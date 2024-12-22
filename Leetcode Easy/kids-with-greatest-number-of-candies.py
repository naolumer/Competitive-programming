def kidsWithCandies(candies,extraCandies):
        answer = []
        max_c = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies>=max_c:
                answer.append(True)
            else:
                answer.append(False)
        return answer
