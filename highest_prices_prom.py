import read_csv
import ten_highest_close_values
import functools

data = read_csv.read('GOOG.csv')

def highest_prices_prom(dict):
    prices_sum = functools.reduce(lambda counter, item: counter + item, dict)
    #print(prices_sum)
    
    prom = prices_sum/len(dict)
    print("The average of the 10 highest closes: " + str(prom))
    
highest_prices_prom(ten_highest_close_values.ten_highest_values(data))