import requests
import json

def create_packet_log(packet):
    print('create packet log')
    url = "http://127.0.0.1:8000/packet/"

    payload = json.dumps(packet)
    headers = {
    'Content-Type': 'application/json'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
    except Exception as e:
        print('error occur : ', str(e))