from flask import Flask, render_template
from api import fetch_latest_race, fetch_drivers, fetch_race_control
from analyzer import analyze_race_control, build_prompt
from ai import generate_summary

app = Flask(__name__)


@app.route("/")
def home():

    race = fetch_latest_race()

    drivers = fetch_drivers(race["session_key"])

    race_control = fetch_race_control(race["session_key"])

    important_events = analyze_race_control(race_control)

    prompt = build_prompt(important_events)

  

    return render_template(
        "index.html",
        race=race,
        drivers=drivers,
        important_events=important_events,
        summary =None
    )
    
@app.route("/summary")
def summary():
    race = fetch_latest_race()

    drivers = fetch_drivers(race["session_key"])

    race_control = fetch_race_control(race["session_key"])

    important_events = analyze_race_control(race_control)

    prompt = build_prompt(important_events)
    
    summary = generate_summary(prompt)
    
    
    return render_template(
    "index.html",
    race=race,
    drivers=drivers,
    summary=summary,
    important_events=important_events
)
    
if __name__ == "__main__":
    app.run(debug=True)