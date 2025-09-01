import pandas as pd
import requests
import json
import matplotlib.pyplot as pt

#Ariana Hrlic
#2025/08/31
#using pandas with Nasa API Mars weather data 

def get_Nasa_Data():
    
    url = "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"

    response = requests.get(url) 
    
    if response.status_code == 200:
        try: 
           
            data = response.json()

            #need new frame to plot only certain data we want
            plot_values = []

  
            # list of sol keys 
            sol_keys = data.get("sol_keys", [])
            
            for i in range(len(sol_keys)):
                print(sol_keys[i])

            # display temps for each sol key
            for sol in range(len(sol_keys)):
                sol_data = data.get(sol, {})
                
            for sol in range(len(sol_keys)):
                atmospheric_temps = sol_data.get("AT", {})
                min_temp = atmospheric_temps.get("mn", {})
                max_temp = atmospheric_temps.get("mx", {})
                
                print(f"sol: {sol},min temps , {min_temp}, max temps , {max_temp} ")
              
                    
        except ValueError:
            print("There was an error with formatting the information from the json file")
    else:
        print("data was not retireved", response.status_code)
        
get_Nasa_Data()