import csv

def read(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        
        header = next(reader)
        #print(header)
        stock_price_dictionary = []
        
        for row in reader:
            iterable = zip(header,row)
            daily_stock_price = {key: value for key, value in iterable}
            
            stock_price_dictionary.append(daily_stock_price)
        
        return stock_price_dictionary