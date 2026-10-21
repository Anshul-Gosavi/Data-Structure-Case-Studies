def shortest_route(graph, start, destination):
    if start not in graph or destination not in graph:
        raise ValueError("Start and destination must be in the map")

    distances = {place: float("inf") for place in graph}
    previous = {place: None for place in graph}
    visited = set()
    distances[start] = 0

    while len(visited) < len(graph):
        current = min(
            (place for place in graph if place not in visited),
            key=lambda place: distances[place],
        )
        if distances[current] == float("inf"):
            break

        visited.add(current)
        for neighbour, road_distance in graph[current]:
            new_distance = distances[current] + road_distance
            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                previous[neighbour] = current

    if distances[destination] == float("inf"):
        return None, float("inf")

    route = []
    current = destination
    while current is not None:
        route.append(current)
        current = previous[current]
    route.reverse()
    return route, distances[destination]


def sample_map():
    return {
        "My House": [("Temple", 3), ("School", 10)],
        "Temple": [("My House", 3), ("School", 2), ("Post Office", 5)],
        "School": [("Temple", 2), ("Post Office", 2), ("Mall", 8)],
        "Post Office": [("Temple", 5), ("School", 2), ("Railway Station", 2), ("Mall", 8)],
        "Railway Station": [("My House", 10), ("Post Office", 2), ("Park", 4), ("Mall", 3)],
        "Park": [("Railway Station", 4), ("Mall", 5)],
        "Mall": [("School", 8), ("Post Office", 8), ("Railway Station", 3), ("Park", 5)],
    }


def main():
    city_map = sample_map()
    start = "My House"
    destination = "Mall"
    route, distance = shortest_route(city_map, start, destination)

    print("CITY GPS ROUTE FINDER")
    print("Start:", start)
    print("Destination:", destination)
    if route is None:
        print("No route is available.")
    else:
        print("Shortest route:", " -> ".join(route))
        print(f"Total distance: {distance} km")


if __name__ == "__main__":
    main()
