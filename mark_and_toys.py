"""
Mark and Jane are very happy after having their first child. 
Their son loves toys, so Mark wants to buy some. 
here are a number of different toys lying in front of him, tagged with their prices. 
Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money. 
Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.
"""

def maximumToys(prices, k):
    prices.sort()
    print(prices)
    counter = 0 
  
    for i in range(len(prices)):
        if k < prices[i]: return counter
        
        k-= prices[i]
        counter +=1