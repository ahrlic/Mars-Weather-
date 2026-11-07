# Mars-Weather

Displays meaningful Nasa API data in regards to Mars and displays graphs using Panadas and Matplotlib libraries in python

Set up instructions: 
1. run "pip install pandas" in the terminal
2. run "pip install requests" in the terminal
3. run "pip install matplotlib" in the terminal
4. run "pip install sys" in the terminal
5. run "pip install subprocess" in the terminal
6. To run NasaData.py with the TestAPIHealth.py, replace the file path to in the subprocess with a relevant path to your file system
7. The demo key in place for the API Key has a rate limit, error code 429 refers to the limit being exceeded -> create your own API key here: https://api.nasa.gov/ or wait some time before running the program again

###Power BI: 

The Python file listed as "NasaData_Bi.py" is a script including just the data frame with the raw data from the API, that can be copy and pasted directly into PowerBi: 
Create Report -> Get Data From Another Source - > Python Script - > Load (raw data) or Transform Data (Data ready to work with) -> Save and Apply 

The data from the data frame can be then used in models / any feature of PowerBi at your convience.

See the complete PowerBI report : Nasa_Data_PowerBI_Report.pdf

###API Health Checker Automation: 

The python file listed as "TestAPIHealth.py" removes the multiple error catching lines of code in the original script. This allows both the main program file "NasaData.py" and the API Health Checker to introduce the single responsibliity principle. The API Health Checker provides additonal error checking for API/HTTP code status' and traces this by logging run time, timeouts, run instances per API request. The automation runs on a sub process to ensure the quality of the main application and avoids returing unclear error messages to a user, as well logging helps to maintain the entire program.



