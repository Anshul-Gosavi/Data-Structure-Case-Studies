# Case Study 1: E-Commerce Sorting by Customer Payable Price

## Scenario
An online store wants customers to compare the final price they will pay, not just the listed price. Each catalog entry has a product name, category, list price, discount percentage, and rating. This program calculates the discounted price and sorts the catalog from lowest to highest payable price.

This is an original implementation of the assigned e-commerce sorting problem. It uses a reusable merge sort and a different record structure, sample catalog, sort key, and output from the nearby reference example.

## Problem and Objectives
**Input:** A catalog of product records.

**Output:** A new catalog ordered by payable price, without losing each product's other details.

- Apply divide and conquer to a practical catalog problem.
- Calculate the customer price from list price and discount.
- Preserve the original catalog and the order of products with equal prices.
- Count and report key comparisons made during merging.
- Relate the implementation to Unit I data structure and complexity concepts.

## Data Structures and ADT
Each product is stored as a dictionary with its name, category, list price, discount, and rating. A simple function calculates the payable price from the list price and discount.

Python lists store the catalog and the temporary sorted halves. These are dynamic, linear structures: they have a sequence order and can grow or shrink at runtime. The sorting operation returns an ordered list and does not change the original catalog.

## Algorithm: Divide and Conquer
Merge sort repeatedly divides the catalog into two halves, sorts each half, then merges the sorted halves by comparing payable prices. On a tie, it takes the item from the left half first. This makes the sort stable, so equal-price products retain their input order.

The function returns the sorted products and the number of price comparisons made during merging.

## Step-Count Example
For the seven-product sample, the program reports **14 payable-price comparisons** during merge operations. This is the measured comparison count for this input, not a count of every Python operation. The split and merge work can be summarized by the recurrence `T(n) = 2T(n/2) + cn`, giving `Theta(n log n)` time.

| Analysis | Complexity |
|---|---|
| Best-case running time | `Theta(n log n)` |
| Average-case running time | `Theta(n log n)` |
| Worst-case running time | `Theta(n log n)` |
| Auxiliary space | `Theta(n)` for temporary lists plus `Theta(log n)` recursion stack |
| Stable? | Yes |

**Asymptotic notation:** Big-O describes an asymptotic upper bound, Omega an asymptotic lower bound, and Theta a tight bound. For this implementation, the merge work gives a tight `Theta(n log n)` running-time bound; it is also `O(n log n)` and `Omega(n log n)`.

## Programming Construct Analysis
- A single pass through `n` records is linear: `Theta(n)`.
- Comparing every pair of records with nested loops is quadratic: `Theta(n^2)`.
- Three nested passes over `n` values are cubic: `Theta(n^3)`.
- Repeatedly halving a search range is logarithmic: `Theta(log n)`.
- Merge sort combines logarithmic division levels with linear work per level: `Theta(n log n)`.

## Algorithmic Strategy Choice
Divide and conquer fits because the ordering task can be split into independent smaller catalogs and their sorted results can be merged. A greedy strategy would make a locally cheapest-next choice, but it is not the approach used in this sort; sorting all products requires establishing a complete order.

## Sample Result
The payable-price order is:

1. Water Bottle - Rs. 1,200
2. Desk Lamp - Rs. 1,800
3. Travel Organizer - Rs. 1,800
4. Canvas Backpack - Rs. 2,880
5. Coffee Grinder - Rs. 3,570
6. Noise-Cancelling Headphones - Rs. 3,600
7. Running Shoes - Rs. 4,000

The Desk Lamp remains before the Travel Organizer because both cost Rs. 1,800 after discount and the sort is stable.

## Limitations
- The sample data is hard-coded and is not connected to a store or database.
- Discounts are whole percentages and prices are represented as floating-point values for a classroom demonstration; a real payment system should use decimal or integer minor units.
- Merge sort needs extra memory for its buffer.

## Run
Requires Python 3. From this folder, run:

```bash
py product_sorting.py
```

The example console output is included in `output.txt`.
