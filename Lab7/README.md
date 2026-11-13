# Lab 7: Fuzzing for Input Validation Bugs

**Name:** Vishwas R. Moodalappa  
**SRN:** PES1UG24CS644  
**Section:** 5 K  

---

## Overview

This lab demonstrates dynamic property-based fuzz testing using Python's **Hypothesis** library. The goal is to uncover unhandled edge-case crashes (such as empty strings, `NoneType`, and invalid formatting) in an unhardened highway toll calculation module and defensively harden the application code against invalid inputs.

---

## Files in this Directory

| File | Description |
| :--- | :--- |
| `highway_toll.py` | Defensively hardened application script handling plate parsing, trip costing, and vehicle axle classification |
| `test_highway_toll.py` | Property-based fuzz test suite using Hypothesis (`@given(st.text() \| st.none())`) |
| `Report.pdf` | Lab report containing screenshots of initial execution, fuzz test failures, hardened script execution, and passing test results |

---

## How to Run

### 1. Install Dependencies
```bash
pip install hypothesis pytest
```

### 2. Run the Application
```bash
python highway_toll.py
```

### 3. Run Fuzz Tests
```bash
pytest test_highway_toll.py
```

---

## Summary of Results

- **Unhardened Code:** Hypothesis fuzzing immediately detected crashes caused by edge cases (`""`, `None`), raising `ValueError`, `AttributeError`, and `TypeError`.
- **Hardened Code:** After implementing input type checking, delimiter verification, and graceful exception handling, all 3 test cases passed successfully (`3 passed in 0.18s`).
