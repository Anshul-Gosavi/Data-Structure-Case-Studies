class WordDictionary:
    def __init__(self, bucket_count=5):
        self.buckets = [[] for _ in range(bucket_count)]

    def bucket_index(self, word):
        total = 0
        for position, character in enumerate(word.lower()):
            total += (position + 1) * ord(character)
        return total % len(self.buckets)

    def add(self, word, meaning):
        index = self.bucket_index(word)
        for entry in self.buckets[index]:
            if entry[0].lower() == word.lower():
                entry[1] = meaning
                return
        self.buckets[index].append([word, meaning])

    def search(self, word):
        index = self.bucket_index(word)
        for stored_word, meaning in self.buckets[index]:
            if stored_word.lower() == word.lower():
                return meaning
        return None

    def delete(self, word):
        index = self.bucket_index(word)
        for entry in self.buckets[index]:
            if entry[0].lower() == word.lower():
                self.buckets[index].remove(entry)
                return True
        return False

    def display(self):
        for index, bucket in enumerate(self.buckets):
            if bucket:
                entries = "; ".join(f"{word}: {meaning}" for word, meaning in bucket)
            else:
                entries = "empty"
            print(f"Bucket {index}: {entries}")


def main():
    dictionary = WordDictionary()
    words = [
        ("array", "A group of values stored in order."),
        ("stack", "A structure that follows last in, first out."),
        ("queue", "A structure that follows first in, first out."),
        ("graph", "A structure made of vertices and edges."),
        ("tree", "A structure that stores data in parent-child form."),
        ("node", "An item that can link to other items."),
    ]

    for word, meaning in words:
        dictionary.add(word, meaning)

    print("COMPUTER WORD DICTIONARY")
    print("Hash table with separate chaining:")
    dictionary.display()

    print("\nSearch for 'graph':", dictionary.search("graph"))
    print("Search for 'heap':", dictionary.search("heap") or "Word not found")
    print("Delete 'node':", dictionary.delete("node"))
    print("Search for 'node' after deletion:", dictionary.search("node") or "Word not found")


if __name__ == "__main__":
    main()
