import pandas as pd
import requests
from requests.exceptions import Timeout
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import sys

# Ariana Hrlic
# 2026/09/05
# using pandas with Nasa API Mars weather data

result = subprocess.run(
    [sys.executable, "PowerBI/TestAPIHealth.py"], capture_output=True, text=True
)


def get_Nasa_Data():

    if result.returncode == 0:

        response = requests.get(
            "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0",
            timeout=2,
        ).json()

        # list declaration
        sol_keys = response.get("sol_keys", [])
        min_temp_list = []
        max_temp_list = []
        seasons_list = []
        pressure_list = []
        h_wind_speed = []
        sols = []

        # display temps for each sol key
        for sol in sol_keys:
            sol_data = response.get(sol, {})

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
                "Sols": sols,
                "Minimum temperature": min_temp_list,
                "Maximum temperature": max_temp_list,
                "Season": seasons_list,
                "Average Atmospheric Pressure": pressure_list,
                "Average Horizontal Wind Speed": h_wind_speed,
            }

        df = pd.DataFrame(mars_data)

        # to show the entire data frame
        print(df.to_string())

        # return lists to access outside of this function
        return sols, min_temp_list, max_temp_list, seasons_list

    else:
        print(f"Error occurred: {result.stdout}")
        exit()


get_Nasa_Data()

# plotting the data into graphs
# def plot_Nasa_Data():

#     sols, min_temp_list, max_temp_list, seasons_list = get_Nasa_Data()

#     x = np.array(sols)

#     y = np.array(min_temp_list)


# plt.scatter(x,y)
# plt.xlabel("Sols")
# plt.ylabel("Minimum Temperature")

# plt.show()


# plt.savefig("min_temperatures.png")


# plot_Nasa_Data()
