#def get_max_profit(stock_prices_yes):
#   for prices in stock_prices_yes:
#       return max(stock_prices_yes)-min(stock_prices_yes)

#print get_max_profit([10,7,5,8,11,9])

#######################

def get_max_profit(stock_prices_yes):
    profit=[]
    for i in range(1,len(stock_prices_yes)):
        max_profit = max(stock_prices_yes[i:])-min(stock_prices_yes[:i])
        profit.append(max_profit)
    return max(profit)

print get_max_profit([10,2,5,8,11,9])
