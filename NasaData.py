import pandas as pd
import requests
import json
import matplotlib.pyplot as pt

#Ariana Hrlic
#2025/10/12
#using pandas with Nasa API Mars weather data 

def get_Nasa_Data():
    
    url = "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"

    response = requests.get(url) 
    
    if response.status_code == 200:
        try: 
           
            data = response.json()
            

            # list of sol keys 
            sol_keys = data.get("sol_keys", [])

            # display temps for each sol key
            for sol in (sol_keys):
                sol_data = data.get(sol)
                
                atmospheric_temps = sol_data.get("AT", {})
                min_temp = atmospheric_temps.get("mn", None)
                max_temp = atmospheric_temps.get("mx", None)
                
               
            temperatures = { "Minimum temperature" : [min_temp] ,
                           "Maximum temperature" : [max_temp]
            }    


            df = pd.DataFrame(temperatures)

            print(df)


        except ValueError:
            print("There was an error with formatting the information from the json file")
    else:
        print("data was not retireved", response.status_code)
        
get_Nasa_Data()