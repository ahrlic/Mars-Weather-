import requests

def TestAPIHealth():

    
    response = requests.get("https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0", timeout=2) 

    data = response.json()

    if response:
      print("Success!")
    else:
      response.encoding = "uft-8"
      print("Run Instance:", response.headers['Date'], "\n")
      raise Exception(f"Non-success status code: {response.status_code}")
        
TestAPIHealth()