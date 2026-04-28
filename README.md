# Python Expression Evaluator(calculator)

A custom-built arithmetic expression evaluator written in Python.
This program parses and evaluates mathematical expressions from a string input, supporting operator precedence and nested parentheses.

---

# Features

* ✅ Supports basic arithmetic:

  * Addition (`+`)
  * Subtraction (`-`)
  * Multiplication (`*`)
  * Division (`/`)
*  Handles **multi-digit numbers**
*  Respects **operator precedence (BODMAS)**:
* `*` and `/` before `+` and `-`
* Supports **nested parentheses**
*  Dynamically reduces expressions step-by-step

---

# How It Works

The program follows a multi-stage evaluation process:

# 1. **Bracket Resolution**

* Finds the **innermost parentheses**
* Evaluates the expression inside
* Replaces it with the result
* Repeats until no parentheses remain

# 2. **Parsing**

* Converts the expression string into:

  * A list of numbers (`l`)
  * A list of operators (`p`)

# 3. **Evaluation**

* First processes:

  * Multiplication (`*`)
  * Division (`/`)
* Then processes:

  * Addition (`+`)
  * Subtraction (`-`)

# 4. **Final Result**

* The list is reduced step-by-step until one value remains

---

# Example Inputs

```
2*(3+4)        → 14
2*(3+(4*5))    → 46
(2+3)*(4+5)    → 45
((2+3)*2)+1    → 11
```

---

# Limitations

*  No support for:

  * Negative numbers (e.g., `-3+5`)
  * Floating-point input (only integers allowed as input)
  * Spaces in input (e.g., `"2 + 3"` may break)
*  Limited input validation:

  * Invalid expressions like `2+`, `++3`, `(2+3` may cause errors
*  Division results in floats (e.g., `14/7 → 2.0`)

---

# Possible Improvements

* Add input validation and error handling (`try/except`)
* Support whitespace in expressions
* Handle negative numbers
* Extend to floating-point parsing
* Improve performance (current approach modifies lists repeatedly)
* Convert into a reusable class or module

---
# Learning Goals

This project demonstrates:

* String parsing techniques
* Manual expression evaluation
* Operator precedence handling
* List manipulation during iteration
* Basic compiler/interpreter concepts

---

# Author Notes

This project was built step-by-step to understand:

* How calculators actually work internally
* The challenges of parsing expressions
* Handling dynamic data structures during computation

