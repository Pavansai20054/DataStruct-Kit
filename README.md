# DataStruct-Kit 🚀

[![PyPI Version](https://img.shields.io/pypi/v/DataStruct-Kit)](https://pypi.org/project/DataStruct-Kit/)
[![Python Versions](https://img.shields.io/pypi/pyversions/DataStruct-Kit)](https://pypi.org/project/DataStruct-Kit/)
[![License](https://img.shields.io/pypi/l/DataStruct-Kit)](https://opensource.org/licenses/MIT)


A Python package implementing essential data structures and algorithms with a focus on performance, usability, and scalability.

---

## ✨ Features

### Sorting Algorithms 📊
- **Bubble Sort**
- **Merge Sort**
- **Quick Sort**

### Searching Algorithms 🔍
- **Linear Search**
- **Binary Search**

### Data Structures 🏗️
- **HashTable**
- **Binary Tree**
- **AVL Tree**
- **Graph**

### Performance Utilities ⏱️
- **Benchmarking tools** for performance analysis.
- **Complexity analysis** for algorithm evaluation.

---

## 📦 Installation

Install DataStruct-Kit from PyPI:

```bash
pip install DataStruct-Kit
```

---

## 🚀 Quick Start

### Example Usage
```python
from DataStruct-Kit import bubble_sort, binary_search, HashTable, BinaryTree, dfs, bfs

# Sorting algorithms
data = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_data = bubble_sort(data)
print(f"Sorted data: {sorted_data}")

# Using a hash table
ht = HashTable()
ht.put("name", "DataStruct-Kit")
ht.put("version", "0.1.0")
print(f"Value: {ht.get('name')}")  # Output: DataStruct-Kit

# Working with binary trees
tree = BinaryTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    tree.insert(value)
print(f"In-order traversal: {tree.inorder()}")

# Graph algorithms
graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D': [], 'E': []}
print(f"DFS: {dfs(graph, 'A')}")  # Output: ['A', 'B', 'D', 'C', 'E']
print(f"BFS: {bfs(graph, 'A')}")  # Output: ['A', 'B', 'C', 'D', 'E']
```

---

## 📊 Performance Benchmarks

You can measure the performance of algorithms using the `measure_time` utility:

```python
from DataStruct-Kit.performance import measure_time
from DataStruct-Kit import bubble_sort, quick_sort

data = list(range(1000, 0, -1))
print(f"Bubble Sort: {measure_time(bubble_sort, data.copy()):.6f} seconds")
print(f"Quick Sort:  {measure_time(quick_sort, data.copy()):.6f} seconds")
```

---

## 📚 Documentation

Full documentation is available at: [DataStruct-Kit Documentation](https://DataStruct-Kit.readthedocs.io)

---

## 🛠️ Development

### Setting up the Development Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/Pavansai20054/DataStruct-Kit.git
   cd DataStruct-Kit
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

4. Run tests:
   ```bash
   pytest
   ```

5. Type checking (optional):
   ```bash
   pip install mypy
   mypy DataStruct-Kit/
   ```

---

## 📋 Roadmap

The following features are planned for future releases:
- Add more sorting algorithms (Heap Sort, Radix Sort).
- Implement priority queues.
- Add advanced tree structures (B-Tree, Red-Black Tree).
- Provide visualization utilities for data structures and algorithms.
- Support for parallel execution of algorithms.

---

## 🤝 Contributing

We welcome contributions! To contribute:
1. Fork the repository.
2. Create your feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/amazing-feature
   ```
5. Open a Pull Request.

For detailed guidelines, refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file.

---

## 📄 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.

---

## 📬 Contact

- **Rangdal Pavansai**: [Email](mailto:pavansai.20066@gmail.com) | [GitHub](https://github.com/Pavansai20054)  
- **Project Link**: [DataStruct-Kit on GitHub](https://github.com/Pavansai20054/DataStruct-Kit)

---


Thank you for using **DataStruct-Kit**!  
Your feedback and contributions make this project better for everyone.