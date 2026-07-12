from flask import Flask, render_template
from api import fetch_latest_race, fetch_drivers, fetch_race_control,fetch_session_results,fetch_driver_standings,fetch_constructor_standings
from analyzer import analyze_race_control, build_prompt
from ai import generate_summary
from datetime import datetime
from coordinates import CIRCUITS



app = Flask(__name__)


@app.route("/")
def home():

    race = fetch_latest_race()
    
    coordinates = CIRCUITS.get(race["circuit_short_name"])
    
    race_date = datetime.fromisoformat(race["date_start"])

    formatted_date = race_date.strftime("%B %#d, %Y")
     
    drivers = fetch_drivers(race["session_key"])
    
    results = fetch_session_results(race["session_key"])
    
    race_control = fetch_race_control(race["session_key"])

    important_events = analyze_race_control(race_control)
    
    

    race_results = []

    for result in results:

      for driver in drivers:

        if result["driver_number"] == driver["driver_number"]:

            race_result = {
                "driver_number": driver["driver_number"],
                "position": result["position"],
                "name": driver["full_name"],
                "team": driver["team_name"],
                "points": result["points"]
            }

            race_results.append(race_result)

            break
    
    podium = race_results[:3]
    
    standings = fetch_driver_standings(race["session_key"])
    
    championship = []
      
    for standing in standings:

      for driver in drivers:

        if standing["driver_number"] == driver["driver_number"]:

            championship_driver = {
                "position": standing["position_current"],
                "name": driver["full_name"],
                "team": driver["team_name"],
                "points": standing["points_current"]
            }

            championship.append(championship_driver)

            break
    
    race = fetch_latest_race()

    constructors = fetch_constructor_standings(race["session_key"])
        
    prompt = build_prompt(important_events)
     
     
    return render_template(
        "index.html",
        race=race,
        formatted_date=formatted_date,
        drivers=drivers,
        race_results=race_results,
        championship=championship,
        constructors=constructors,
        circuits=CIRCUITS,
        podium=podium,
        important_events=important_events,
        summary =None
    )
    
@app.route("/summary")
def summary():
    race = fetch_latest_race()
    
    coordinates = CIRCUITS.get(race["circuit_short_name"])
    
    race_date = datetime.fromisoformat(race["date_start"])

    formatted_date = race_date.strftime("%B %#d, %Y")

    drivers = fetch_drivers(race["session_key"])
    
    results = fetch_session_results(race["session_key"])

    race_control = fetch_race_control(race["session_key"])

    important_events = analyze_race_control(race_control)
    
    race_results = []

    for result in results:

      for driver in drivers:

        if result["driver_number"] == driver["driver_number"]:

            race_result = {
                "driver_number": driver["driver_number"],
                "position": result["position"],
                "name": driver["full_name"],
                "team": driver["team_name"],
                "points": result["points"]
            }

            race_results.append(race_result)

            break
        
    standings = fetch_driver_standings(race["session_key"])
    
    championship = []
      
    for standing in standings:

      for driver in drivers:

        if standing["driver_number"] == driver["driver_number"]:

            championship_driver = {
                "position": standing["position_current"],
                "name": driver["full_name"],
                "team": driver["team_name"],
                "points": standing["points_current"]
            }

            championship.append(championship_driver)

            break
    
    podium = race_results[:3]
    
    constructors = fetch_constructor_standings(race["session_key"])
        
    prompt = build_prompt(important_events)
    
    summary = generate_summary(prompt)
    
    
    
    return render_template(
    "index.html",
    race=race,
    formatted_date=formatted_date,
    drivers=drivers,
    race_results=race_results,
    championship=championship,
    podium=podium,
    circuits=CIRCUITS,
    summary=summary,
    important_events=important_events,
    constructors=constructors
)
    
    
    
@app.route("/driver/<int:driver_number>")
def driver_profile(driver_number):

    race = fetch_latest_race()

    drivers = fetch_drivers(race["session_key"])
    
    standings = fetch_driver_standings(race["session_key"])
    
    driver_standing = None
    selected_driver = None
    
    

    
    for driver in drivers:

      if driver["driver_number"] == driver_number:

        selected_driver = driver

        break
    
    for standing in standings:

     if standing["driver_number"] == driver_number:

        driver_standing = standing

        break
    
    

        
    return render_template(
    "driver.html",
    driver=selected_driver,
    standing=driver_standing
)
    
    

    
    
    

if __name__ == "__main__":
    app.run(debug=True)