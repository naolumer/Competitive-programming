def maxCoinsYouCanGet(piles):
    # sortig the piles
    piles.sort() 
    # initialize an array to store the coins i should pick from each pile
    
    coinsIget=[]
    for i in range(len(piles)-2,int(len(piles)/3)-1,-2):
        coinsIget.append(piles[i])

    return sum(coinsIget)

    
