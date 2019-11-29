import csv
import re

def main():
    inf = open('cost_revenue_dirty.csv')
    reader = csv.reader(inf, delimiter=',')
    of = open('cost_revenue_clean_custom.csv', 'w')

    for row in reader:
        of.write(','.join(list(map(removal, row))) + '\n')

def removal(number):
    return re.sub("\$|,", '', number)

if __name__ == '__main__':
    main()



