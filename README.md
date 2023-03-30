# Project1

An analysis of 5 travel stocks from API data, March 29,2021 to March 25,2022.
Calculated weekly population standard deviation as a measure of volatility and plotted using Python packages statistics and matplotlib.

## Methodology

### Data Extraction
+ Selected ABNB (Air BNB),DAL (Delta),EXPE (Expedia),RCL (Royal Caribbean Cruises),MAR (Marriot Int) stock data from API.
+ formatted date time and added to data as new column
+ converted each stock data into its own csv 

![extract](https://github.com/JacquelineGomez06/Project1/blob/2fb9b6cd44b52acb71686c12118ca4a6c5c83b94/plots/extract.png)

### Analysis

+manually imported csv data
+calculated population standard deviation for ONLY Mon-Fri

![analysis](https://github.com/JacquelineGomez06/Project1/blob/2fb9b6cd44b52acb71686c12118ca4a6c5c83b94/plots/analysis.png)
## Visuals

![ABNB](https://github.com/JacquelineGomez06/Project1/blob/6290b98cb4b87b6bb097f0179ba90856aec4f8ac/plots/ABNB.csv.png)

![Delta](https://github.com/JacquelineGomez06/Project1/blob/6290b98cb4b87b6bb097f0179ba90856aec4f8ac/plots/DAL.csv.png)

![EXPE](https://github.com/JacquelineGomez06/Project1/blob/6290b98cb4b87b6bb097f0179ba90856aec4f8ac/plots/EXPE.csv.png)

![MAR](https://github.com/JacquelineGomez06/Project1/blob/6290b98cb4b87b6bb097f0179ba90856aec4f8ac/plots/MAR.csv.png)

![RCL](https://github.com/JacquelineGomez06/Project1/blob/6290b98cb4b87b6bb097f0179ba90856aec4f8ac/plots/RCL.csv.png)

## Results
As we can assume, stock is extremely volatile and it can be seen in the plots above.
EXPE and ABNB were the most volatile since the STDEV y-axis goes up to 12.

## Next Actions
This mini project can be expanded by adding more data points for the selected stocks or include other stocks outside of the travel.