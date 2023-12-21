import read_csv

def run():
    data = read_csv.read('./GOOG.csv')
    print(data)

if __name__ == '__main__':
    run()