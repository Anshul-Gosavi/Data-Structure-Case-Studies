def format_time(minutes):
    hour = minutes // 60
    minute = minutes % 60
    return f"{hour:02d}:{minute:02d}"


def schedule_events(events, transition_minutes):
    ordered = sorted(
        events,
        key=lambda event: (
            -event["priority"],
            event["finish"] - event["start"],
            event["start"],
            event["title"],
        ),
    )
    selected = []
    decisions = []

    for event in ordered:
        conflict = None
        for scheduled in selected:
            if (event["start"] < scheduled["finish"] + transition_minutes
                    and scheduled["start"] < event["finish"] + transition_minutes):
                conflict = scheduled
                break

        if conflict is None:
            selected.append(event)
            decisions.append({
                "event": event,
                "selected": True,
                "explanation": f"priority {event['priority']}; no schedule conflict",
            })
        else:
            decisions.append({
                "event": event,
                "selected": False,
                "explanation": f"conflicts with {conflict['title']} or its transition gap",
            })

    return selected, decisions


def sample_events():
    return [
        {"title": "Data Structures Lecture", "start": 9 * 60, "finish": 9 * 60 + 50, "priority": 4, "location": "Room B204"},
        {"title": "Advisor Check-in", "start": 9 * 60 + 20, "finish": 9 * 60 + 40, "priority": 5, "location": "Office 12"},
        {"title": "Team Stand-up", "start": 10 * 60, "finish": 10 * 60 + 20, "priority": 4, "location": "Online"},
        {"title": "Design Review", "start": 10 * 60 + 25, "finish": 11 * 60 + 10, "priority": 5, "location": "Studio 3"},
        {"title": "Library Research", "start": 11 * 60, "finish": 11 * 60 + 45, "priority": 3, "location": "Library"},
        {"title": "Mentor Session", "start": 13 * 60 + 15, "finish": 14 * 60, "priority": 5, "location": "Office 8"},
        {"title": "Database Workshop", "start": 14 * 60 + 10, "finish": 15 * 60, "priority": 4, "location": "Room A110"},
    ]


def display_event(event):
    print(
        f"{format_time(event['start'])}-{format_time(event['finish'])}  "
        f"{event['title']:<24}  Priority {event['priority']}  {event['location']}"
    )


def main():
    events = sample_events()
    transition_minutes = 10
    selected, decisions = schedule_events(events, transition_minutes)

    print("CAMPUS DAY PLANNER - PRIORITY-FIRST GREEDY SCHEDULING")
    print(f"Required transition gap: {transition_minutes} minutes")
    print("\nProposed events:")
    for event in sorted(events, key=lambda item: item["start"]):
        display_event(event)

    print("\nGreedy decisions (priority, then shorter duration):")
    for decision in decisions:
          status = "SELECT" if decision["selected"] else "SKIP"
          event = decision["event"]
          print(f"{status:<6} {format_time(event['start'])}-"
              f"{format_time(event['finish'])}  {event['title']}"
              f" - {decision['explanation']}")

    print("\nFinal schedule:")
    for event in sorted(selected, key=lambda item: item["start"]):
        display_event(event)
    print(f"\nEvents scheduled: {len(selected)} of {len(events)}")


if __name__ == "__main__":
    main()
