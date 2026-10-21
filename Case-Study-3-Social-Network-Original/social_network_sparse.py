class SparseSocialNetwork:
    def __init__(self, user_count: int):
        if user_count < 1:
            raise ValueError("The network must contain at least one user")
        self.user_count = user_count
        self.friendship_count = 0
        self.rows: dict[int, set[int]] = {}

    def _validate_user(self, user_id: int) -> None:
        if not 1 <= user_id <= self.user_count:
            raise ValueError(f"User ID must be between 1 and {self.user_count}")

    def add_friendship(self, user_a: int, user_b: int) -> bool:
        self._validate_user(user_a)
        self._validate_user(user_b)
        if user_a == user_b:
            raise ValueError("A user cannot be friends with themselves")
        if self.are_friends(user_a, user_b):
            return False

        self.rows.setdefault(user_a, set()).add(user_b)
        self.rows.setdefault(user_b, set()).add(user_a)
        self.friendship_count += 1
        return True

    def remove_friendship(self, user_a: int, user_b: int) -> bool:
        self._validate_user(user_a)
        self._validate_user(user_b)
        if not self.are_friends(user_a, user_b):
            return False

        self.rows[user_a].remove(user_b)
        self.rows[user_b].remove(user_a)
        if not self.rows[user_a]:
            del self.rows[user_a]
        if not self.rows[user_b]:
            del self.rows[user_b]
        self.friendship_count -= 1
        return True

    def are_friends(self, user_a: int, user_b: int) -> bool:
        self._validate_user(user_a)
        self._validate_user(user_b)
        return user_b in self.rows.get(user_a, set())

    @property
    def stored_matrix_cells(self) -> int:
        return sum(len(neighbors) for neighbors in self.rows.values())

    def display_matrix(self, user_ids: list[int]) -> None:
        for user_id in user_ids:
            self._validate_user(user_id)

        names = {
            1001: "SAM",
            1002: "RAM",
            1003: "JOHN",
            1004: "RAMESH",
            1005: "SURESH",
        }
        print("        " + " ".join(f"{names.get(user_id, str(user_id)):>7}" for user_id in user_ids))
        for row_id in user_ids:
            row = self.rows.get(row_id, set())
            values = " ".join(f"{int(user_id in row):>5}" for user_id in user_ids)
            print(f"{names.get(row_id, str(row_id)):>7} {values}")


def sample_network() -> tuple[SparseSocialNetwork, list[int]]:
    network = SparseSocialNetwork(1_000_000)
    sample_user_ids = [1001, 1002, 1003, 1004, 1005]
    friendships = [
        (1001, 1002),
        (1001, 1004),
        (1002, 1003),
        (1003, 1005),
        (1004, 1005),
    ]
    for user_a, user_b in friendships:
        network.add_friendship(user_a, user_b)
    return network, sample_user_ids


def main() -> None:
    network, sample_user_ids = sample_network()

    print("SOCIAL NETWORK - SPARSE ADJACENCY MATRIX")
    print(f"User ID range: 1 to {network.user_count:,}")
    print(f"Stored friendship pairs: {network.friendship_count}")
    print(f"Stored nonzero matrix cells: {network.stored_matrix_cells}")
    print("\nSample matrix (1 = friends, 0 = not friends):")
    network.display_matrix(sample_user_ids)

    print("Are SAM and RAMESH friends?", network.are_friends(1001, 1004))
    print("Are RAM and RAMESH friends?", network.are_friends(1002, 1004))

    network.remove_friendship(1001, 1004)
    print("\nAfter removing the friendship between SAM and RAMESH:")
    print("Are SAM and RAMESH friends?", network.are_friends(1001, 1004))
    print(f"Stored friendship pairs: {network.friendship_count}")
    print(f"Stored nonzero matrix cells: {network.stored_matrix_cells}")


if __name__ == "__main__":
    main()
