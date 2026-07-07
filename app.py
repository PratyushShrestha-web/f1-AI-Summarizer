from flask import Flask, render_template
from api import fetch_latest_race, fetch_drivers, fetch_race_control,fetch_session_results
from analyzer import analyze_race_control, build_prompt
from ai import generate_summary
from datetime import datetime




app = Flask(__name__)


@app.route("/")
def home():

    race = fetch_latest_race()
    
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
                "position": result["position"],
                "name": driver["full_name"],
                "team": driver["team_name"],
                "points": result["points"]
            }

            race_results.append(race_result)

            break
    
    podium = race_results[:3]
    
        
    prompt = build_prompt(important_events)

  

    return render_template(
        "index.html",
        race=race,
        formatted_date=formatted_date,
        drivers=drivers,
        race_results=race_results,
        podium=podium,
        important_events=important_events,
        summary =None
    )
    
@app.route("/summary")
def summary():
    race = fetch_latest_race()
    
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
                "position": result["position"],
                "name": driver["full_name"],
                "team": driver["team_name"],
                "points": result["points"]
            }

            race_results.append(race_result)

            break
    
    podium = race_results[:3]
    
    prompt = build_prompt(important_events)
    
    summary = generate_summary(prompt)
    
    
    return render_template(
    "index.html",
    race=race,
    formatted_date=formatted_date,
    drivers=drivers,
    race_results=race_results,
    podium=podium,
    summary=summary,
    important_events=important_events
)
    
if __name__ == "__main__":
    app.run(debug=True)