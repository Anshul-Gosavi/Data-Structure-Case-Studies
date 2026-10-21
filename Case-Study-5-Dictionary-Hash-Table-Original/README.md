# Case Study 5: Computer Word Dictionary Using Hashing

## Introduction
A dictionary stores words and their meanings. This small computer-terms dictionary uses a hash table to find a word's bucket and separate chaining to keep words that map to the same bucket.

## Problem
Store words and meanings, search for a word, update its meaning, and delete it. A collision happens when two different words map to the same bucket.

## Hash Table
The table has five buckets. The hash function adds each letter's character code multiplied by its position, then takes the remainder after division by the bucket count. For example, `array` and `graph` map to the same bucket in this sample. Each bucket is a list, so both words are kept using separate chaining.

The sample has six entries and five buckets, so its load factor is `6 / 5 = 1.2`. The table has a fixed size and does not rehash or resize.

## Operations
- Add a word, or update its meaning if it already exists.
- Search for a word without scanning every bucket.
- Delete a word from its bucket.
- Display all buckets and their entries.

## Complexity
| Operation | Average | Worst case |
|---|---|---|
| Add, search, delete | `O(1)` | `O(n)` |
| Display table | `O(m + n)` | `O(m + n)` |

Here, `n` is the number of words and `m` is the number of buckets. A poor distribution can put many words in one bucket, causing the worst case.

## Limitations
This is a short learning example. Its hash function is not intended for production, and the table does not grow automatically when more words are added.

## Run
Requires Python 3. Run this command from the case-study folder:

```bash
py word_hash_dictionary.py
```

The sample output is in `output.txt`.
