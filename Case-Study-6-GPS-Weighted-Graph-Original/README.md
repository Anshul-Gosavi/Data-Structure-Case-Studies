# Case Study 6: City Route Finder Using a Weighted Graph

## Introduction
A map can be represented as a weighted graph. Places are vertices, roads are edges, and each road has a distance. This small program finds a shortest route from My House to the Mall.

## Problem
Store a few city locations and road distances, then find and display the shortest route between two locations.

## Data Structure and Algorithm
The road map is an adjacency list: each location stores its neighboring locations and the distance to each one. The roads in this example work in both directions. Dijkstra's algorithm keeps the shortest known distance to each place and repeatedly visits the closest unvisited place.

The implementation uses a simple scan to choose the next place, making the steps easy to follow.

## Sample Route
The shortest route in the sample map is:

`My House -> Temple -> School -> Post Office -> Railway Station -> Mall`

Total distance: **12 km**.

## Complexity
For `V` locations and `E` roads, this simple implementation takes `O(V^2 + E)` time because it scans locations to find the next closest place. The map and distance information use `O(V + E)` space.

Dijkstra's algorithm requires non-negative road distances. This is an educational example and does not use live GPS, traffic, or real map data.

## Run
Requires Python 3. Run this command from the case-study folder:

```bash
py city_routes.py
```

The sample output is in `output.txt`.
