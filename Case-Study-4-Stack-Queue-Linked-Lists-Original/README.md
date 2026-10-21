# Case Study 4: Stack and Queue Using Linked Lists

## Introduction
A stack and a queue are linear data structures. A stack follows LIFO (Last In, First Out), while a queue follows FIFO (First In, First Out). This program implements both using a singly linked list.

## Problem
Create a stack of plates and a queue of customers. Demonstrate adding, viewing, and removing items from each structure.

## Data Structure
Each linked-list node stores a value and a link to the next node. The stack keeps a `top` node. The queue keeps `front` and `rear` nodes.

## Operations
- Stack: `push`, `pop`, `peek`, and display from top to bottom.
- Queue: `enqueue`, `dequeue`, `peek`, and display from front to rear.
- `pop` and `dequeue` return `None` when their structure is empty.

## Complexity
| Operation | Time |
|---|---|
| Stack push, pop, peek | `O(1)` |
| Queue enqueue, dequeue, peek | `O(1)` |
| Display | `O(n)` |
| Storage for `n` items | `O(n)` |

## Run
Requires Python 3. Run this command from the case-study folder:

```bash
py linked_stack_queue.py
```

The sample output is in `output.txt`.
