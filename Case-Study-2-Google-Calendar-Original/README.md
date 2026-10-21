# Case Study 2: Priority-First Calendar Scheduling

## Scenario
A student has more proposed meetings, classes, and personal activities than can fit into an uninterrupted day. Some events matter more than others, and travel or setup time is needed between appointments. This program uses a greedy rule to build a feasible calendar: consider higher-priority events first, then favor shorter events, and accept an event only if it does not conflict with an accepted event or its transition gap.

This is intentionally different from the separate activity-selection example: it does not order events by earliest finish or aim to maximize the number of events. It models a priority-based calendar preference instead.

## Problem and Objectives
- Represent a one-day calendar as event records with start, finish, priority, and location.
- Schedule non-conflicting events with a required transition gap.
- Greedily consider priority 5 before priority 1; use shorter duration and then earlier start to break ties.
- Show why each proposed event was selected or skipped.
- Analyze the behavior and limitations of a local greedy choice.

## Data Structures and ADT
Each event is stored as a dictionary containing its title, start time, finish time, priority, and location. The event list is a dynamic, linear data structure. `schedule_events` returns the accepted events and a dictionary explaining the decision for every proposal.

The input list is not changed. The program uses simple functions, dictionaries, and lists to demonstrate the scheduling process.

## Greedy Strategy
1. Sort proposals by descending priority, then by shorter duration, earlier start, and title.
2. Consider each proposal once in that order.
3. Compare it with accepted events. Reject it if it overlaps an accepted event or comes within the required transition gap.
4. Otherwise, accept it. Display the decisions in greedy order and the final accepted schedule chronologically.

The local choice is to preserve a higher-priority event whenever there is a conflict. This is a practical heuristic for the stated preference, not a globally optimal solution for every calendar.

## Sample Outcome
The sample uses seven proposed events, a 10-minute transition gap, and priorities from 1 (lowest) to 5 (highest). The scheduler accepts four events: Advisor Check-in, Design Review, Mentor Session, and Database Workshop. It skips lower-priority or conflicting proposals and prints the conflicting event in its explanation.

## Complexity
For `n` proposed events:

| Operation | Complexity |
|---|---|
| Sort by priority and tie-breakers | `O(n log n)` |
| Check each event against accepted events | `O(n^2)` worst case |
| Total running time | `O(n^2)` worst case |
| Additional storage | `O(n)` |

The conflict checks dominate in the worst case because each proposal may be compared with many accepted events.

## Limitations
- Priority-first greedy scheduling does not guarantee the maximum event count or maximum total priority; changing a locally preferred event can sometimes produce a better overall calendar.
- Priorities are manually assigned and do not include dependencies, reminders, time zones, travel distances, or user availability.
- This is a one-day educational simulation, not a connection to Google Calendar.

## Run
Requires Python 3. From this folder, run:

```bash
py calendar_scheduler.py
```

The sample console output is included in `output.txt`.
