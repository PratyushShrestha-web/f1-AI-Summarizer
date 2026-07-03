def analyze_race_control(race_control):

 important_events = []

 for event in race_control:
    important_event = {
        "lap": event["lap_number"],
        "flag": event["flag"],
        "message": event["message"]
    }

    important_events.append(important_event)

 return important_events