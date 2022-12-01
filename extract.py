#import key from config
#URL that gets open and close price for ABNB 4/1/2021
from config import key
import requests as req
import time

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
        real_time=time.strftime('%Y-%m-%d',time.localtime(closing["t"]/1000))
        

    #create a dictionary of real_time and c_price
    price_time={
        'date':real_time, 
        'closing_price':c_price
    }
    #append dict to stock_data
    stock_data.append(price_time)

with open(f"{stock}.csv","w",newLine='') as outfile:
    writer=csv.DictWriter(outfile,fieldnames=["Date","Closing_Price"])
    writer.writeheader()
    for row in stock_data:
        writer.writerow(row)

        