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
                
                print(f"sol: {sol}, temps: {atmospheric_temps}")
 
                #plot min and max values to new frame 
                
                '''
                plot_values.append({
                    "Sol" : sol,
                    "Min Temp" : min_temp,
                    "Max Temps" : max_temp
            
                })
                
                diagram_frame = pd.DataFrame(plot_values)
                diagram_frame.plot(kind='scatter', x='Min Temp', y='Max Temp')
                 #check if there are any duplicate values in the established data frame - one of pandas most promient methods
                if diagram_frame.duplicated.any(): 
                   diagram_frame = diagram_frame.drop_duplicates

                #the data frame doesnt have a show method, use matplotlib for doing visuals/ plotting values
                pt.show()
                '''
        except ValueError:
            print("There was an error with formatting the information from the json file")
    else:
        print("data was not retireved", response.status_code)
        
get_Nasa_Data()

