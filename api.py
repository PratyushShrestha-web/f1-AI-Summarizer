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
    
    from datetime import datetime, timezone
    
    today = datetime.now(timezone.utc)
    
    completed_races = []
     
    for session in sessions:
        race_data = datetime.fromisoformat(session["date_start"])
        if race_data < today:
           
            completed_races.append(session)
            
    if not completed_races:
       raise Exception("No completed races found.")

    latest_race = completed_races[-1]
    
    
   
    
    return latest_race



def fetch_drivers(session_key):
   
    url =f"{BASE_URL}/drivers"
    
    params = {
        "session_key": session_key
    }
    
    response = requests.get(url,params=params)
    response.raise_for_status()
    
    drivers = response.json()
    if not drivers:
        raise Exception("No driver found.")

    
    latest_race = drivers[-1]
    return drivers

def fetch_session_results(session_key):
    
    url = f"{BASE_URL}/session_result"
    
    params= {
        "session_key":session_key
    }
    
    response = requests.get(url,params=params)
    
    
    response.raise_for_status()
    
    session_result = response.json()
    
    if not session_result:
        raise Exception("No result found.")

    
    latest_race = session_result[-1]
    
    return session_result

def fetch_race_control(session_key):
    
    url = f"{BASE_URL}/race_control"
    
    params = { 
              "session_key" :session_key
    }
    
    response = requests.get(url,params=params)
    response.raise_for_status()
    
    race_control = response.json()
    
    if not race_control:
        raise Exception("No race control found")
    
    return race_control

def fetch_driver_standings(session_key):
    
    url =f"{BASE_URL}/championship_drivers"
    
    params = {
        "session_key": session_key
    }
    
    response = requests.get(url,params=params)
    
    response.raise_for_status()
    
    return response.json()