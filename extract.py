from config import key
import requests as req
import time
import csv
#loop through stocks,request data,import results as json
stocks=["DAL","ABNB","MAR","HTZ","RCL"]
for stock in stocks:
    url=f"https://api.polygon.io/v2/aggs/ticker/{stock}/range/1/day/2021-03-29/2022-03-25?adjusted=true&sort=desc&limit=120&apiKey={key}"
    data=req.get(url)
    json_data=data.json()
    results=json_data["results"]
    #loop results to get closing prices with dates
    stock_data=[]
    for day in results:
        c_price=day["c"]
        t_price=day["t"]
        real_time=time.strftime('%Y-%m-%d',time.localtime(t_price/1000))
        #create a dictionary of real_time and c_price
        stock_dict={
        'date':real_time, 
        'closing_price':c_price
        }
        #append dict to stock_data
        stock_data.append(stock_dict)


    with open(f"{stock}.csv","w",newline='') as outfile:
        writer=csv.DictWriter(outfile,fieldnames=["date","closing_price"])
        writer.writeheader()
        for row in stock_data:
            writer.writerow(row)


