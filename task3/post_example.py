import requests

url = 'http://127.0.0.1:5000/optimal_scheduling'

json_example = {
  'start_times': [10, 20, 30, 40, 50, 60],
  'end_times': [15, 25, 35, 45, 55, 65]
}

response = requests.post(url, json=json_example)
print(response.json())