import requests 

BASE_URL = "https://api.openf1.org/v1"

def fetch_latest_race():
    
    
    url = f"{BASE_URL}/sessions"
    
    params = {
        "session_type": "Race"
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()  

    sessions = response.json()

    if not sessions:
        raise Exception("No race sessions found.")

    
    latest_race = sessions[-1]

    return latest_race

def fetch_drivers(session_key):
   
    url =f"{BASE_URL}/drivers"
    
    params = {
        "session_key": session_key
    }
    
    response = requests.get(url,params=params)
    response.raise_for_status()
    
    drivers = response.json()
    
    return drivers