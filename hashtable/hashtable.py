class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


def djb2(key):
    """
    DJB2 hash, 32-bit

    Implement this, and/or FNV-1.
    """
    hash = 5381
    for c in key:
        hash = (hash * 33) + ord(c)
    return hash & 0xFFFFFFFF


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        else:
            self.capacity = capacity
        self.bucket = [None] * capacity
        self.count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.bucket)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.count / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        bucket_index = self.hash_index(key)
        if self.bucket[bucket_index] is not None:
            cur_node = self.bucket[bucket_index]
            while cur_node is not None:
                if cur_node.key == key:
                    cur_node.value = value
                    break
                cur_node = cur_node.next
            cur_bucket = self.bucket[bucket_index]
            self.bucket[bucket_index] = HashTableEntry(key, value)
            self.bucket[bucket_index].next = cur_bucket
            self.count += 1
        else:
            self.bucket[bucket_index] = HashTableEntry(key, value)
            self.count += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        bucket_index = self.hash_index(key)
        cur_node = self.bucket[bucket_index]
        if cur_node is None:
            return
        else:
            if cur_node.key == key:
                self.bucket[bucket_index] = cur_node.next
                self.count -= 1
                return cur_node.value
            else:
                prev_node = cur_node
                cur_node = cur_node.next
                while cur_node is not None:
                    if cur_node.key == key:
                        prev_node.next = cur_node.next
                        self.count -= 1
                        return cur_node.value
                    else:
                        prev_node = cur_node
                        cur_node = cur_node.next
                return

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        bucket_index = self.hash_index(key)
        cur_node = self.bucket[bucket_index]
        while cur_node is not None:
            if cur_node.key == key:
                return cur_node.value
            cur_node = cur_node.next
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        new_bucket = self.bucket
        self.bucket = new_capacity
        self.bucket = [None] * self.bucket
        self.count = 0
        for bucket in new_bucket:
            cur_node = bucket
            while cur_node is not None:
                self.put(cur_node.key, cur_node.value)
                cur_node = cur_node.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
