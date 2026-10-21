# Case Study 3: Social Network Using a Sparse Adjacency Matrix

## Introduction
A social network can be modeled as a graph. Each user is a vertex, and each friendship is an undirected edge. This example represents a network with one million possible user IDs while storing only the friendships that exist.

The small displayed sample uses the names SAM, RAM, JOHN, RAMESH, and SURESH. Numeric IDs are used by the program so the same structure can represent a large user range.

## Problem
Create a friendship network that can add or remove a friendship, check whether two users are friends, and display a small matrix view of the connections.

## Data Structure
A dense adjacency matrix for one million users would contain one trillion cells. Since most users have few friendships, this program stores only nonzero matrix positions using a dictionary of sets: each user ID maps to the IDs of directly connected friends. The undirected relationship is stored in both directions, so the conceptual matrix is symmetric.

The dictionary is a sparse row representation of the adjacency matrix. The displayed five-user sample is a 2D matrix view; the program does not allocate a dense million-by-million matrix.

## Working
1. Create the network with a user ID range from 1 to 1,000,000.
2. Add each friendship to both users' rows.
3. Check a friendship by looking for one user ID in the other's row.
4. Remove a friendship from both rows.
5. Display a small matrix for SAM, RAM, JOHN, RAMESH, and SURESH, where 1 means friends and 0 means no direct friendship.

## Complexity
Let `V` be the number of possible users and `E` the number of friendship pairs.

| Operation | Complexity |
|---|---|
| Add friendship | `O(1)` average |
| Check friendship | `O(1)` average |
| Remove friendship | `O(1)` average |
| Sparse storage | `O(V + E)` upper bound; this example stores only rows with friendships |
| Display a selected `k x k` sample | `O(k^2)` |

An undirected friendship is stored as two directed matrix entries, so the five sample friendships occupy 10 nonzero cells. This is far smaller than the one trillion cells in a dense matrix for one million users.

## Limitations
- The example uses a fixed user ID range and sample friendships; it is not connected to a real social network.
- Python dictionaries and sets use more memory per entry than a compact numeric matrix, but they avoid storing the many zero values.
- The displayed matrix is for a small sample only.

## Run
Requires Python 3.10 or newer. From this folder, run:

```bash
py social_network_sparse.py
```

The sample output is included in `output.txt`.
