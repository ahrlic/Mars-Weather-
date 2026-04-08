#script to run in Power Bi

import pandas as pd
import requests

url = "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"

response = requests.get(url)

data = response.json()

sol_keys = data.get("sol_keys", [])

min_temp_list = []
max_temp_list = []
seasons_list = []
pressure_list = []
h_wind_speed = []
sols  = []

for sol in sol_keys:
    sol_data = data.get(sol, {})
    
    atmospheric_temps = sol_data.get("AT", {})

    min_temp_list.append(atmospheric_temps.get("mn", None))
    max_temp_list.append(atmospheric_temps.get("mx", None))
    seasons_list.append(sol_data.get("Season", None))
    pressure_list.append(sol_data.get("PRE", {}).get("av", None))
    h_wind_speed.append(sol_data.get("HWS", {}).get("av", None))

    sols.append(sol)

mars_data = { 
    "Sols": sols, 
    "Minimum temperature": min_temp_list,
    "Maximum temperature": max_temp_list, 
    "Season": seasons_list,
    "Average Atmospheric Pressure": pressure_list,
    "Average Horizontal Wind Speed": h_wind_speed
}

df = pd.DataFrame(mars_data)

df