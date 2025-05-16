# Example of using hash table
from DataStruct_Kit.hashtables import HashTable

if __name__ == "__main__":
    ht = HashTable()
    ht.put("name", "Alice")
    ht.put("age", 30)
    print("Name:", ht.get("name"))
    print("Age:", ht.get("age"))