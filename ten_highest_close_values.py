import read_csv
import heapq

data = read_csv.read('GOOG.csv')

def ten_highest_values(dict):
    
    closing_prices = list(map(lambda price: round(float(price['Close']), 6), dict))
    #print(closing_prices)

    ten_highest = heapq.nlargest(10, closing_prices)
    #print(ten_highest)
    
    return ten_highest

print(ten_highest_values(data))