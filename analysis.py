
import statistics as stats
import matplotlib.pyplot as plt
import csv

#import data to use for analysis
filenames=["ABNB.csv","RCL.csv","EXPE.csv","MAR.csv","DAL.csv"]

for file in filenames:
    data=[]
    with open(f"data/{file}", "r") as infile:
        reader = csv.DictReader(infile)
    # save this dictReader object into a list of dictionaries to analyze
        for row in reader:
            data.append(row)

    #calculate population standard deviation
    i=0
    stock_dev=[]

    while i <len(data):
        #place in a try/except to avoid error due to holidays when stockmarket is closed
        if i+4>len(data):
            break
        #iterate for every 5days
        day1=float(data[i]["closing_price"])
        day2=float(data[i+1]["closing_price"])
        day3=float(data[i+2]["closing_price"])
        day4=float(data[i+3]["closing_price"])
        day5=float(data[i+4]["closing_price"])
        week_lst=[day1,day2,day3,day4,day5]
        stock_dev.append(stats.pstdev(week_lst))
        i+=5
    #plot data   
    plt.plot(stock_dev)
    plt.title(f"{file} Weekly Standard Deviation")
    plt.xlabel("Date",fontsize=10)
    plt.ylabel("STDEV of Closing Price")
    plt.savefig(f"{file}.png")
    plt.show()




