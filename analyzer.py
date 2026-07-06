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


  

    for event in important_events:
       

     return important_events

def build_prompt(important_events):
    prompt = ""

    for event in important_events:
        prompt += (
            f"Lap {event['lap']:>2} | "
            f"{event['flag']:<13} | "
            f"{event['message']}\n"
        )

    return prompt