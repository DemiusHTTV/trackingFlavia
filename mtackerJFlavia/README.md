<a name="top"></a>
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-brightgreen)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/yourusername/iosife-flavia)](https://github.com/DemiusHTTV/trackingFlavia)
[![Release](https://img.shields.io/github/v/release/yourusername/iosife-flavia)](https://github.com/DemiusHTTV/trackingFlavia)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](#)
[![Getting Started](https://img.shields.io/badge/getting_started-guide-1D76DB)](#usage)

⭐ Star us on GitHub — your support motivates us a lot! 🙏😊

## 🚀 IosifeFlavia Library

**IosifeFlavia** — простая Python-библиотека для решения задачи Иосифа-Флавия (Josephus problem) и измерения использования памяти функций.

- Модуль `iosife_flavia.py` — функция `IosifeFlavia(arr, n, k)`  
- Модуль `memory_helper.py` — функция `execute_and_get_memory_usage(function, n)` для анализа памяти  

---

## 📚 Usage

### Решение задачи Иосифа-Флавия
```python
from iosife_flavia import IosifeFlavia

arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
k = 3

result = IosifeFlavia(arr.copy(), n, k)
print(f"Последний оставшийся элемент: {result}")