import read_csv
import functools

data = read_csv.read('GOOG.csv')

def find_higher_price(dict):
    max_price = functools.reduce(lambda counter, item: counter if counter['Close'] > item['Close'] else item, dict)
    print(max_price)
    
find_higher_price(data)