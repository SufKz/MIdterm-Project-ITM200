##### Q1
import csv
with open('C:\\Users\\Tamim\PycharmProjects\\itm200 assignments\\midterm project\\Data.csv', mode = 'r') as fCSV:
    cv = csv.reader(fCSV)
    for line in cv:
        print(line)
##### Q2
with open('C:\\Users\\Tamim\PycharmProjects\\itm200 assignments\\midterm project\\Data.csv', newline='') as csvf:
    read = csv.reader(csvf)
    next(read)

    ttl_sales = {}
    for i in read:
        year = int(i[0])
        if year < 2012 or year > 2021:
            continue
        sales_data = []
        for x in i[1:]:
            if x != '':
                sales_data.append(int(x))
        ttl_sales[year] = sum(sales_data)

with open('stats.txt', 'w') as file:
    file.write('Total Sales from 2012-2021:\n')

    for year, sales in ttl_sales.items():
        file.write(f"{year}: {sales}\n")
##### Q3
import matplotlib.pyplot as plt

years = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
sales = [1665063, 1728140, 1851645, 1867498, 1948375, 2029668, 1987373, 1921449, 1661560, 1638340]

plt.figure(1)
plt.bar(years, sales)

plt.title('Total Car Sales per Year')
plt.xlabel('Year')
plt.ylabel('Total Sales')

plt.show()
#### Q4

sales2021 = [110903, 114510, 153722, 154105, 152141, 162549]
sales2022 = [36922, 39082, 55611, 57110, 56991, 66514]

ttl_sales2021 = sum(sales2021)
ttl_sales2022 = sum(sales2022)

sgr = (ttl_sales2022 - ttl_sales2021) / ttl_sales2022

with open('C:\\Users\\Tamim\PycharmProjects\\itm200 assignments\\midterm project\\stats.txt', 'a') as f:
    f.write('Sales Growth Rate: ' + str(round(sgr, 2)))

est_sales2022 = []

for month in range(7, 13):
    month_y21 = sales2021[month - 7]

    est_sale = month_y21 * (1 + sgr)

    est_sales2022.append(est_sale)

with open('C:\\Users\\Tamim\PycharmProjects\\itm200 assignments\\midterm project\\stats.txt', 'a') as f:
    f.write('\nEstimated Sales for Last Six Months of 2022:\n')
    f.write('July 2022: ' + str(round(-est_sales2022[0])) + '\n')
    f.write('August 2022: ' + str(round(-est_sales2022[1])) + '\n')
    f.write('September 2022: ' + str(round(-est_sales2022[2])) + '\n')
    f.write('October 2022: ' + str(round(-est_sales2022[3])) + '\n')
    f.write('November 2022: ' + str(round(-est_sales2022[4])) + '\n')
    f.write('December 2022: ' + str(round(-est_sales2022[5])) + '\n')

##### Q5
import matplotlib.pyplot as plt

sales_months = ['July', 'August', 'September', 'October', 'November', 'December']
est_sales2022 = [-est_sales2022[0], -est_sales2022[1], -est_sales2022[2], -est_sales2022[3], -est_sales2022[4], -est_sales2022[5]]

plt.figure(2)
plt.bar(sales_months, est_sales2022)

plt.title('Estimated Sales for the Last Six Months of 2022')
plt.xlabel('Sales in thousands)')
plt.ylabel('Months')

plt.show()