# Tests for hash table
from DataStruct_Kit.hashtables import HashTable


def test_hashtable():
    """Tests hash table operations."""
    ht = HashTable()
    ht.put("key1", "value1")
    ht.put("key2", "value2")
    assert ht.get("key1") == "value1"
    assert ht.get("key2") == "value2"
    assert ht.get("key3") is None