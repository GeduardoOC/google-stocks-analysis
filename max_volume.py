import read_csv

data = read_csv.read('GOOG.csv')

def max_volume(dict):
    max_volume_dict = list(filter(lambda volumen: int(volumen['Volume']) >= 999999999, dict))
    
    for stock in max_volume_dict:
        print("On " + stock["Date"] + " " + stock["Volume"] + " shares moved")
    
max_volume(data)