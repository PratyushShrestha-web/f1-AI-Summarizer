from flask import Flask, render_template, jsonify
from api import fetch_latest_race, fetch_drivers, fetch_race_control,fetch_session_results,fetch_driver_standings,fetch_constructor_standings
from analyzer import analyze_race_control, build_prompt
from ai import generate_summary
from datetime import datetime
from coordinates import CIRCUITS
import json
import os

SUMMARY_FILE = "data/summary_cache.json"
app = Flask(__name__)

def get_dashboard_data(generate_ai=False):

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

                race_results.append({
                    "driver_number": driver["driver_number"],
                    "position": result["position"],
                    "name": driver["full_name"],
                    "team": driver["team_name"],
                    "points": result["points"]
                })

                break

    podium = race_results[:3]

    standings = fetch_driver_standings(race["session_key"])

    championship = []

    for standing in standings:

        for driver in drivers:

            if standing["driver_number"] == driver["driver_number"]:

                championship.append({
                    "position": standing["position_current"],
                    "name": driver["full_name"],
                    "team": driver["team_name"],
                    "points": standing["points_current"]
                })

                break

    constructors = fetch_constructor_standings(race["session_key"])

    summary = None

    if generate_ai:

        prompt = build_prompt(important_events)

        summary = generate_summary(prompt)

    return {

        "race": race,

        "formatted_date": formatted_date,

        "drivers": drivers,

        "race_results": race_results,

        "championship": championship,

        "constructors": constructors,

        "circuits": CIRCUITS,

        "podium": podium,

        "important_events": important_events,

        "summary": summary

    }
    
    
@app.route("/")
def home():

    data = get_dashboard_data()

    return render_template(
        "index.html",
        **data
    )
    
@app.route("/summary")
def summary():

    data = get_dashboard_data()

    return render_template(
        "index.html",
        **data
    )
@app.route("/api/summary")
def api_summary():

    try:

        # Check whether a valid cached summary exists
        if os.path.exists(SUMMARY_FILE):

            with open(SUMMARY_FILE, "r", encoding="utf-8") as file:

                cached_data = json.load(file)

            if "summary" in cached_data:

                print("Using cached AI summary")

                return jsonify({
                    "summary": cached_data["summary"]
                })


        # No valid cached summary exists
        print("Generating new AI summary...")

        data = get_dashboard_data(generate_ai=True)

        summary = data["summary"]


        # Make sure data folder exists
        os.makedirs("data", exist_ok=True)


        # Save summary
        with open(SUMMARY_FILE, "w", encoding="utf-8") as file:

            json.dump({

                "summary": summary

            }, file, indent=4)


        print("AI summary saved successfully")

        return jsonify({

            "summary": summary

        })


    except Exception as e:

        print("API SUMMARY ERROR:", e)

        return jsonify({

            "error": str(e)

        }), 500
    
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