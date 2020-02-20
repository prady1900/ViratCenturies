import csv

file1 = open("E:\\Python1\\DATA\\CSV\\table-1.csv", "r", newline='')
reader = csv.reader(file1)
header = next(reader)  # first is header

data = [row for row in reader]
dates_table1 = []
dates_table2 = []
for row in data:
    date = int(row[-3][-4:])
    dates_table1.append(date)

file2 = open("E:\\Python1\\DATA\\CSV\\table-2.csv", "r", newline='')
reader1 = csv.reader(file2)
header1 = next(reader1)  # first is header

data1 = [row for row in reader1]
for row in data1:
    date = int(row[-3][-4:])
    dates_table2.append(date)

final_list = dates_table1 + dates_table2

final_list.sort()
years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
counts = []
for j in range(len(years)):
    count = final_list.count(years[j])
    counts.append(count)


avg = round(sum(counts) / len(counts))
total_centuries_tn = sum(counts)

f_years = []
prev_year = years[-1]
while total_centuries_tn < 100:
    total_centuries_tn += avg
    counts.append(avg)
    prev_year = prev_year + 1
    years.append(str(prev_year))


with open("E:\Python1\DATA\CSV\Overall_Centruies.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["YEAR", "No. of Centuries"])

    for (y, c) in zip(years, counts):
        writer.writerow([y, c])

    f.close()

print(years)
print(counts)
# print(header)
# print(data[0])

#check
