import requests
from requests.exceptions import Timeout


def TestAPIHealth():

    try:
        response = requests.get(
            "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0",
            timeout=2,
        )

        if response:
            print("Active")

        else:

            response.encoding = "utf-8"
            print("Run Instance:", response.headers["Date"], "\n")
            print(response.elapsed.total_seconds())

        with open("logAPIError", "a") as f:
            f.write(
                f"\n"
                f"Run Instance: {response.headers.get('Date', 'N/A')}\n"
                f"Time Elapsed: {response.elapsed.total_seconds()}\n"
                f"Status Code: {response.status_code}\n"
            )

        raise Exception(f"Non-success status code: {response.status_code}")

    except Timeout:
        print("The request timed out")


TestAPIHealth()
