import sys
import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np

#Ariana Hrlic
#2025/10/20
#using pandas with Nasa API Mars weather data 

def get_Nasa_Data():
    
    url = "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"

    response = requests.get(url) 
    
    if response.status_code == 200:
        try: 
           
            data = response.json()

            # list declaration
            sol_keys = data.get("sol_keys", [])
            min_temp_list = []
            max_temp_list = []
            sols = []

            # display temps for each sol key
            for sol in (sol_keys):
                sol_data = data.get(sol)
                
                atmospheric_temps = sol_data.get("AT", {})

                min_temp = atmospheric_temps.get("mn", None)
                min_temp_list.append(min_temp)
                
                
                max_temp = atmospheric_temps.get("mx", None)
                max_temp_list.append(max_temp)
                
                sols.append(sol)
            
               
            temperatures = { 
                "Sols" : sols, 
                "Minimum temperature" : min_temp_list ,
                "Maximum temperature" : max_temp_list
            }    


            df = pd.DataFrame(temperatures)

            print(df)
            
            #return lists to access outside of this function
            return sols, min_temp_list, max_temp_list
        

        except ValueError:
            print("There was an error with formatting the information from the json file")
    else:
        print("data was not retireved", response.status_code)


#plotting the data into graphs
def plot_Nasa_Data():
    sols, min_temp_list, max_temp_list = get_Nasa_Data()
   
    x = np.array(sols)

    y = np.array(min_temp_list)

    plt.scatter(x,y)

    plt.show()


    plt.savefig("mars_temperatures.png") 


#get_Nasa_Data()
plot_Nasa_Data()