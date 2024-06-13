import requests

# Replace with your actual API URL and prompt
api_url = "http://127.0.0.1:8000/get_coupon/1"
prompt = "how much is the discount"

# Data can be sent as a dictionary or JSON-encoded string
data = {"prompt": prompt}

response = requests.get(api_url, json=data)

if response.status_code == 200:
  generated_text = response.json()["text"]
  print(generated_text)
else:
  print("Error:", response.status_code, response.text)
