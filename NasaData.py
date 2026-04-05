import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np

#Ariana Hrlic
#2026/04/03
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
            seasons_list = []
            pressure_list = []
            sols = []

            # display temps for each sol key
            for sol in (sol_keys):
                sol_data = data.get(sol)
                
                atmospheric_temps = sol_data.get("AT", {})

                min_temp = atmospheric_temps.get("mn", None)
                min_temp_list.append(min_temp)
                
                
                max_temp = atmospheric_temps.get("mx", None)
                max_temp_list.append(max_temp)
                
                seasons = sol_data.get("Season", None)
                seasons_list.append(seasons)

                atmoshperic_pressure = sol_data.get("PRE", None)
                pressure_list.append(atmoshperic_pressure)

                sols.append(sol)
            
               
            temperatures = { 
                "Sols" : sols, 
                "Minimum temperature" : min_temp_list ,
                "Maximum temperature" : max_temp_list , 
                "Season" : seasons_list, 
            }    

            
            df = pd.DataFrame(temperatures)
        

            print(df)
           
            #return lists to access outside of this function
            return sols, min_temp_list, max_temp_list, seasons_list

        except ValueError:
            print("There was an error with formatting the information from the json file")
    else:
        print("data was not retireved", response.status_code)


#plotting the data into graphs
def plot_Nasa_Data():
    sols, min_temp_list,seasons_list, max_temp_list = get_Nasa_Data()
   

    x = np.array(sols)

    y = np.array(min_temp_list)

   # plt.scatter(x,y)
   # plt.xlabel("Sols")
   # plt.ylabel("Minimum Temperature")

   # plt.show()


   # plt.savefig("min_temperatures.png") 



plot_Nasa_Data()
get_Nasa_Data()