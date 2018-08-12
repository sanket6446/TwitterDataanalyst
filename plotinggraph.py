from matplotlib import pyplot as plt
from matplotlib.dates import date2num


#obj = Data_Cleaner()
#plot_data = obj.Get_Plot_Data_Retweet_VS_Date('clean_appl.csv')
#print plot_data
import csv
import datetime as DT
import numpy as np
import matplotlib.pyplot as plt
data = []
file_name = "F:\\TwitterData\\tradecleaning24.csv"
with open(file_name, "r") as myfile:
    mycsvfile = csv.reader(myfile)
    for row in mycsvfile:
        data.append(row)
#print data
date_var  = ""
cnt = 0
temp_date = ""
plot_data = []
for i in range(0,len(data)):
    #print data[i][1]
    obj = ""
    temp_date = date_var
    if i == 0:
        date_var = data[i][1]
        cnt+=1
    elif i == len(data)-1:
        obj = (DT.datetime.strptime(date_var, "%a %b %d %Y"), cnt)
        plot_data.append(obj)
        cnt = 0
    elif  temp_date == data[i][1]:
        cnt = cnt + 1
    elif temp_date != data[i][1]:
        obj = (DT.datetime.strptime(date_var, "%a %b %d %Y"), cnt)
        plot_data.append(obj)
        cnt = 0
        date_var = data[i][1]
        cnt+=1

print plot_data

x = [date2num(date) for (date, value) in plot_data]
y = [value for (date, value) in plot_data]

fig = plt.figure()
graph = fig.add_subplot(111)
graph.set_xlabel('Date')
graph.xaxis.label.set_color('blue')
graph.set_ylabel('Number of tweets')
graph.yaxis.label.set_color('blue')

# Plot the data as a red line with round markers
graph.plot(x,y,'r--o')
# Set the xtick locations to correspond to just the dates you entered.
graph.set_xticks(x)
# Set the xtick labels to correspond to just the dates you entered.
graph.set_xticklabels(
        [date.strftime("%d-%m-%Y") for (date, value) in plot_data]
        )
title_obj = plt.title('Date vs Number of tweets') #get the title property handler
plt.getp(title_obj)                    #print out the properties of title
plt.getp(title_obj, 'text')            #print out the 'text' property for title
plt.setp(title_obj, color='b')
plt.show()