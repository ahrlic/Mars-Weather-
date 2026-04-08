# Mars-Weather

Displays meaningful Nasa API data and displays graphs using Panadas, Numpy and Matplotlib libraries in python

Set up instructions: 
1. run "pip install pandas" in the terminal
2. run "pip install requests" in the terminal
3. run "pip install matplotlib" in the terminal
4. The demo key in place for the API Key has a rate limit, error code 429 refers to the limit being exceeded -> create your own API key here: https://api.nasa.gov/ 
   or wait some time before running the program again

Power BI: 

The Python file listed as "NasaData_Bi.py" is a script including just the data frame with the raw data from the API, that can be copy and pasted directly into PowerBi: 
Create Report -> Get Data From Another Source - > Python Script - > Load (raw data) or Transform Data (Data ready to work with) -> Save and Apply 

The data from the data frame can be then used in models / any feature of PowerBi at your convience.

