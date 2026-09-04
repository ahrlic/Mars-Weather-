import requests
from requests.exceptions import Timeout

def TestAPIHealth():

  try: 
    response = requests.get("https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0", timeout=2).json() 

    total_records = len(response)

    if response:
      print("Active")
    else:
      response.encoding = "uft-8"
      print("Run Instance:", response.headers['Date'], "\n")
      print(f"Total records: {total_records}", "\n")  
      raise Exception(f"Non-success status code: {response.status_code}")

  except Timeout:
     print("The request timed out")
        
TestAPIHealth()