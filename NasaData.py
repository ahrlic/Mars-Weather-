import pandas as pd
import requests
import json

#Ariana Hrlic
#using pandas with Nasa API data 

def get_Nasa_Data():
    
    url = "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"

    response = requests.get(url) 
    
    if response.status_code == 200:
        try: 
           
            data = pd.read_json(response.json())

           
            sol_keys = data.get("sol_keys", [])

            # list of sol keys 
            for i in range(len(sol_keys)):
                 print(sol_keys.to_string)
                 print()

            # display temps for each sol key
            for sol in sol_keys:
                sol_data = data.get(sol, {})
                atmospheric_temps = sol_data.get("AT", {})
                min_temp = sol_data.get("mn", {})
                max_temp = sol_data.get("mx", {})
                
                print(f"sol: {sol}, temps: {atmospheric_temps}")
                print("min temps ", {min_temp})
                print("max temps ", {max_temp})

                
            print("data retrieved")
        except ValueError:
            print("There was an error with formatting the information from the json file")
    else:
        print("data was not retireved", response.status_code)
        
get_Nasa_Data()

