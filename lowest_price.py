import read_csv
import functools

data = read_csv.read('GOOG.csv')

def find_lowest_price(dict):
    min_price = functools.reduce(lambda counter, item: counter if counter['Close'] < item['Close'] else item, dict)
    print(min_price)
    
find_lowest_price(data)

    