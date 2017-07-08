import bs4 as bs
import urllib.request
import datetime
import matplotlib.pyplot as plt
import sqlite3

source = urllib.request.urlopen("http://www.arso.gov.si/vode/podatki/amp/H9350_t_1.html").read()
soup = bs.BeautifulSoup(source, 'html.parser')
table_cells = str(soup.find_all("td"))

current_time = datetime.datetime.now()
time_delta = current_time - datetime.timedelta(minutes=40)
hours = str(time_delta.hour)
rounded_minutes = str(int(time_delta.minute/10) * 10)  # rounds down to 10s

if rounded_minutes == '0':
    rounded_minutes = '00'

if int(hours) < 10:
    hours = '0'+hours

date = str(current_time.date())
time = hours + ':' + rounded_minutes


def get_sea_data():
    for i, item in enumerate(table_cells.split()):
        if item == hours+':'+rounded_minutes+'</td>':
            tide = table_cells.split()[i+1]
            temp = table_cells.split()[i+2]
            tide = tide.strip('<td>/')
            temp = temp.strip('<td>/')
            return tide, temp

#  plt.figure().set_facecolor('black')
plt.figure(figsize=(3, 5.5))
axes = plt.gca()
axes.axes.set_ylim([145, 290])
axes.get_xaxis().set_visible(False)
plt.bar(10, int(get_sea_data()[0]))
#  plt.show()
plt.savefig('D:\projects\python projects\webdev\KusKus\static\plima', facecolor='#79B9E1')
print(get_sea_data())

with open('data.txt', 'w') as t:
    t.write(date + '\n')
    t.write(time + '\n')
    t.write(str(get_sea_data()[0]) + '\n')
    t.write(str(get_sea_data()[1]))

print(date)
print(time)


def connect_db():
    return sqlite3.connect('D:\projects\python projects\webdev\KusKus\web_database.db')


def get_db():
    sqlite_db = connect_db()
    return sqlite_db


#  file_list = []
#  with open('D:\projects\python projects\webdev\KusKus\scripts\data.txt', 'r') as f:
#          for line in f:
#              file_list.append(line.replace('\n', ''))

db = get_db()
db.execute('INSERT INTO sea_data (datum, ura, plima, temp) VALUES (?, ?, ?, ?)', (date, time, get_sea_data()[0],
                                                                                  get_sea_data()[1]))
db.commit()
db.close()
