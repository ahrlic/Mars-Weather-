import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np

#Ariana Hrlic
#2026/04/06
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
            h_wind_speed = []
            sols  = []
           

            # display temps for each sol key
            for sol in (sol_keys):
                sol_data = data.get(sol, {})
                
                atmospheric_temps = sol_data.get("AT", {})

                min_temp = atmospheric_temps.get("mn", None)
                min_temp_list.append(min_temp)
                
                
                max_temp = atmospheric_temps.get("mx", None)
                max_temp_list.append(max_temp)
                
                seasons = sol_data.get("Season", None)
                seasons_list.append(seasons)

                atmoshperic_pressure = sol_data.get("PRE", {}).get("av", None)
                pressure_list.append(atmoshperic_pressure)

                horizontal_wind_speed = sol_data.get("HWS", {}).get("av", None)
                h_wind_speed.append(horizontal_wind_speed)



                sols.append(sol)
            
               
            mars_data = { 
                "Sols" : sols, 
                "Minimum temperature" : min_temp_list ,
                "Maximum temperature" : max_temp_list , 
                "Season" : seasons_list,
                "Average Atmospheric Pressure" : pressure_list,
                "Average Horizontal Wind Speed" : h_wind_speed
            }    

            
            df = pd.DataFrame(mars_data)
        

            #to show the entire data frame
            print(df.to_string())
           
            #return lists to access outside of this function
            return sols, min_temp_list, max_temp_list, seasons_list

          
        except TypeError :
            print("The value does not have the expected type")
        
        except ValueError :
            print("The value has the wrong format")
           
    else:
        print("data was not retireved", response.status_code)


#plotting the data into graphs
def plot_Nasa_Data():

    sols, min_temp_list, max_temp_list, seasons_list = get_Nasa_Data()
   

    x = np.array(sols)

    y = np.array(min_temp_list)

   # plt.scatter(x,y)
   # plt.xlabel("Sols")
   # plt.ylabel("Minimum Temperature")

   # plt.show()


   # plt.savefig("min_temperatures.png") 



plot_Nasa_Data()
