def analyze_race_control(race_control):

    important_events = []
    seen_events = set()

    important_flags = {
        "YELLOW",
        "DOUBLE YELLOW",
        "RED",
        "CHEQUERED"
    }

    for event in race_control:

        if event["flag"] in important_flags:

            
            event_key = (event["lap_number"], event["message"])

            if event_key not in seen_events:
                seen_events.add(event_key)

                important_event = {
                    "lap": event["lap_number"],
                    "flag": event["flag"],
                    "message": event["message"]
                }

                important_events.append(important_event)

    print("\nImportant Race Events")
    print("-" * 40)

    for event in important_events:
        print(f"Lap {event['lap']:>2} | {event['flag']:<13} | {event['message']}")

    return important_events

